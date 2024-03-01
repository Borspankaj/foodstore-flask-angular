from extensions import db 
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text)