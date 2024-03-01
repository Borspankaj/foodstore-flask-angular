from repository.menu_repository import MenuRepository
from DTO.menu_dto import MenuDto

class MenuService:
    @staticmethod
    def get_menu(menu_id):
        menu_item = MenuRepository.get_menu(menu_id)
        menu_data = MenuDto.get_menu_data_from_model(menu_item)
        return menu_data

    @staticmethod
    def create_menu(request_data):
        restaurant_id, dish_name, price, description = MenuDto.get_menu_data_from_request(request_data)
        new_menu_item = MenuRepository.add_menu(restaurant_id=restaurant_id, dish_name=dish_name, price=price, description=description)
        menu_data = MenuDto.get_menu_data_from_model(new_menu_item)
        return menu_data

    @staticmethod
    def update_menu(request_data, menu_id):
        restaurant_id, dish_name, price, description = MenuDto.get_menu_data_from_request(request_data)
        menu_item = MenuRepository.update_menu(menu_id=menu_id, restaurant_id=restaurant_id, dish_name=dish_name, price=price, description=description)
        if menu_item:
            menu_data = MenuDto.get_menu_data_from_model(menu_item)
            return menu_data
        return None

    @staticmethod
    def delete_menu(menu_id):
        success = MenuRepository.delete_menu(menu_id)
        return success
    
    @staticmethod
    def get_menus_for_restaurant(restaurant_id):
        menu_items = MenuRepository.get_menus_for_restaurant(restaurant_id)
        menu_data_list = [MenuDto.get_menu_data_from_model(menu_item) for menu_item in menu_items]
        return menu_data_list
    
    
