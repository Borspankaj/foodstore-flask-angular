from flask_restful import Resource , reqparse
from services.menu_service import MenuService
class MenuResource(Resource) :
    
    def get(self, menu_id):
        menu_data = MenuService.get_menu(menu_id)
        if menu_data:
            return menu_data
        else:
            return {'message': 'Menu item not found'}, 404
        
    def post(self):
        request_data = reqparse.request.get_json()
        try:
            response_data = MenuService.create_menu(request_data)
            return {'message': 'Menu item created successfully', 'data': response_data}, 201
        except Exception as e:
            return {'message': 'Internal error', 'error': str(e)}
        
    def put(self, menu_id):
        request_data = reqparse.request.get_json()
        
        response_data = MenuService.update_menu(request_data, menu_id)
        if response_data:
            return {'message': 'Menu item updated successfully', 'data': response_data}, 200
        else:
            return {'message': 'Menu item not found'}, 404

    def delete(self, menu_id):
        success = MenuService.delete_menu(menu_id)
        if success:
            return {'message': 'Menu item deleted successfully'}
        else:
            return {'message': 'Menu item not found'}, 404
        
        
class RestrauntMenuResource(Resource) :
    def get(self, restaurant_id):
        menu_data = MenuService.get_menus_for_restaurant(restaurant_id)
        if menu_data:
            return menu_data
        else:
            return {'message': 'Menu not found'}, 404
    