from market import app, db
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/market', method=['GET', 'POST'])
@login_required
def market_page():
	purchase_form = PurchaseItemForm()
	if request.method == 'POST':
		purchased_item = request.form.get('purchased_item')
		p_item_object = Item.query.filter_by(name=purchased_item).first()
		if p_item_object:
			if current_user.can_purchase(p_item_object):
				p_item_object.buy(current_user)
				flash(
					f"Congratulations! You purchased {p_item_object.name}"
					f"for {p_item_object.price}", category='success')
			else:
				flash(
					f"Unfortunately, you don't have enough money"
					f"to purchase {p_item_object.name}", category='danger')
		return redirect(url_for('market_page'))
	if request.method == 'GET':
		items = Item.query.filter_by(owner=None)
		return render_template('market.html', items=items,
                         purchase_form=purchase_form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
	form = RegisterForm()
	if form.validate_on_submit():
		user_to_create = User(
		username=form.username.data,
		email_address=form.email_address.data,
		password=form.password1.data
		)
		db.session.add(user_to_create)
		db.session.commit()
		login_user(user_to_create)
		flash(
			f'Account create successfully! You are now logged'
			f'in as {user_to_create.username}', category='success')
		return redirect(url_for('market_page'))
	if form.errors != {}:
		for err_msg in form.errors.values():
			flash(f'Ocorreu um erro ao criar o usuário: {err_msg[0]}', category='danger')
	return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
	form = LoginForm()
	if form.validate_on_submit():
		attempted_user = User.query.filter_by(username=form.username.data).first()
		if attempted_user and \
			attempted_user.check_password_correction(
							attempted_password=form.password.data):
			login_user(attempted_user)
			flash(
				f'Success! You are logged in as:'
				f'{attempted_user.username}', category='success')
			return redirect(url_for('market_page'))
		else:
			flash(
				'Username and password are incorrect!'
				f'Please try again.', category='danger')
	return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
	logout_user()
	flash('You have been logged out!', category='info')
	return redirect(url_for('home_page'))
