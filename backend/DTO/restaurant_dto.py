from models.user import User
class RestaurantDto:
    @staticmethod
    def get_restaurant_data_from_model(restaurant):
        if restaurant:
            return {
                'id': restaurant.id,
                'name': restaurant.name,
                'location': restaurant.location,
                'cuisine': restaurant.cuisine,
                'owner_id': restaurant.owner_id
            }
        else:
            return {}

    @staticmethod
    def get_restaurant_data_from_request(request_data):
        email = request_data.get("email" , "")
        user = User.query.filter_by(email = email).first()
        owner_id = user.id
        name = request_data.get("name", "")
        location = request_data.get("location", "")
        cuisine = request_data.get("cuisine", "")
        
        
        return name, location, cuisine, owner_id
