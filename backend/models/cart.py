from extensions import db

class Cart(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    total_value = db.Column(db.Float, default=0.0)
    items = db.relationship('CartItem' , backref='cart' , lazy = True)
    
class CartItem(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer,db.ForeignKey('menu.id') , nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    