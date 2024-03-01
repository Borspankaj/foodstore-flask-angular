from extensions import db
from models.restaurant import Restaurant
from models.user import User
class RestaurantRepository:
    @staticmethod
    def get_restaurant(restaurant_id):
        return Restaurant.query.get(restaurant_id)

    @staticmethod
    def add_restaurant(name, location, cuisine, owner_id):
        restaurant = Restaurant(name=name, location=location, cuisine=cuisine, owner_id=owner_id)
        db.session.add(restaurant)
        db.session.commit()
        return restaurant

    @staticmethod
    def update_restaurant(restaurant_id, **kwargs):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            for key, value in kwargs.items():
                setattr(restaurant, key, value)
            db.session.commit()
            return restaurant
        return None

    @staticmethod
    def delete_restaurant(restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_all_restaurants() :
        return Restaurant.query.all()

    @staticmethod
    def get_my_restaurants(user_email) :
        user = User.query.filter_by(email = user_email).first()
        owner_id  =user.id
        return Restaurant.query.filter_by(owner_id = owner_id)
    
