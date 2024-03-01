from flask_restful import Resource, reqparse
from services.restaurant_service import RestaurantService

class RestaurantResource(Resource):
    def get(self,  restaurant_id ):
        restaurant_data = RestaurantService.get_restaurant(restaurant_id)
        if restaurant_data:
            return restaurant_data
        else:
            return {'message': 'Restaurant not found'}, 404

    def post(self):
        request_data = reqparse.request.get_json()
        
        try:
            response_data = RestaurantService.create_restaurant(request_data)
            return {'message': 'Restaurant created successfully', 'data': response_data}, 201
        except Exception as e:
            return {'message': 'Internal error', 'error': str(e)}

    def put(self, restaurant_id):
        request_data = reqparse.request.get_json()
        
        restaurant_data = RestaurantService.update_restaurant(request_data, restaurant_id)
        if restaurant_data:
            return {'message': 'Restaurant updated successfully', 'data': restaurant_data}, 200
        else:
            return {'message': 'Restaurant not found'}, 404

    def delete(self, restaurant_id):
        success = RestaurantService.delete_restaurant(restaurant_id)
        if success:
            return {'message': 'Restaurant deleted successfully'}
        else:
            return {'message': 'Restaurant not found'}, 404

class SearchResource(Resource) :
    def get(self) :
        try:
            response_data = RestaurantService.get_all_restuarants()
            return {'message': 'Restaurant fetched', 'data': response_data}, 201
        except Exception as e:
            return {'message': 'Internal error', 'error': str(e)} , 404
        
    def post(self) :
        request_data = reqparse.request.get_json()
        try:
            response_data = RestaurantService.search_restaurants(request_data["keyword"])
            return {'message': 'Restaurant fetched', 'data': response_data}, 201
        except Exception as e:
            return {'message': 'Internal error', 'error': str(e)} , 404
        
            
class OwnerResource(Resource) :
    def get(self , user_email) :
        try:
            response_data = RestaurantService.get_my_restaurants(user_email)
            return {'message': 'Restaurant fetched', 'data': response_data}, 201
        except Exception as e:
            return {'message': 'Internal error', 'error': str(e)} , 404
        