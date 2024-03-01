from models.menu import Menu
class MenuDto:
    @staticmethod
    def get_menu_data_from_model(menu_item):
        if menu_item:
            return {
                'menu_id' : menu_item.id ,
                'restaurant_id': menu_item.restaurant_id,
                'dish_name': menu_item.dish_name,
                'price': menu_item.price,
                'description': menu_item.description
            }
        else:
            return {}

    @staticmethod
    def get_menu_data_from_request(request_data):
        restaurant_id = request_data.get("restaurant_id", None)
        dish_name = request_data.get("dish_name", "")
        price = request_data.get("price", 0.0)
        description = request_data.get("description", None)
        
        return restaurant_id, dish_name, price, description

    @staticmethod
    def get_dish_name(menu_id) :
        menu = Menu.query.get(menu_id)
        return menu.dish_name
    
    @staticmethod
    def get_menu_price(menu_id) :
        menu = Menu.query.get(menu_id) 
        return menu.price