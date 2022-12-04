from market import db


class Item(db.Model):   # type: ignore
    __tablename__ = 'item'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'
