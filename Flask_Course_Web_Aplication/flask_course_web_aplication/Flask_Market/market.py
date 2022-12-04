from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
        return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '456978123645', 'price': 500},
        {'id': 2, 'name': 'iPhone', 'barcode': '456987654321', 'price': 900},
        {'id': 3, 'name': 'iPad', 'barcode': '456987659451', 'price': 150}
    ]
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
