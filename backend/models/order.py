from extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)
    status = db.Column(db.String)
    
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False) 
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    
