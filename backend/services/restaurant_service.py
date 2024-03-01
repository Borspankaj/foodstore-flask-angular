from repository.restaurant_repository import RestaurantRepository
from DTO.restaurant_dto import RestaurantDto

class RestaurantService:

    @staticmethod
    def get_restaurant(restaurant_id):
        restaurant = RestaurantRepository.get_restaurant(restaurant_id)
        if restaurant:
            return RestaurantDto.get_restaurant_data_from_model(restaurant)
        return None

    @staticmethod
    def create_restaurant(request_data):
        name, location, cuisine, owner_id = RestaurantDto.get_restaurant_data_from_request(request_data)
        new_restaurant = RestaurantRepository.add_restaurant(name=name, location=location, cuisine=cuisine, owner_id=owner_id)
        return RestaurantDto.get_restaurant_data_from_model(new_restaurant)

    @staticmethod
    def update_restaurant(request_data, restaurant_id):
        name, location, cuisine, owner_id = RestaurantDto.get_restaurant_data_from_request(request_data)
        updated_restaurant = RestaurantRepository.update_restaurant(restaurant_id=restaurant_id, name=name, location=location, cuisine=cuisine, owner_id=owner_id)
        if updated_restaurant:
            return RestaurantDto.get_restaurant_data_from_model(updated_restaurant)
        return None

    @staticmethod
    def delete_restaurant(restaurant_id):
        return RestaurantRepository.delete_restaurant(restaurant_id)


    @staticmethod
    def get_all_restuarants() :
        restaurants = RestaurantRepository.get_all_restaurants()
        data = [RestaurantDto.get_restaurant_data_from_model(rest) for rest in restaurants]
        return data
    
    @staticmethod
    def get_my_restaurants(user_email) :
        restaurants = RestaurantRepository.get_my_restaurants(user_email=user_email)
        data = [RestaurantDto.get_restaurant_data_from_model(rest) for rest in restaurants]
        return data
    
    @staticmethod
    def search_restaurants(keyword) :
        keyword = keyword.lower()
        restaurants = RestaurantRepository.get_all_restaurants()
        data = [RestaurantDto.get_restaurant_data_from_model(rest) for rest in restaurants if (
            keyword in rest.name.lower() or
            keyword in rest.location.lower() or
            keyword in rest.cuisine.lower()
        )]
        return data