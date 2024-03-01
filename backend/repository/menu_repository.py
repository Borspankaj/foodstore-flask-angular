from extensions import db
from models.menu import Menu

class MenuRepository:
    def get_menu(menu_id):
        return Menu.query.get(menu_id)

    def add_menu(restaurant_id, dish_name, price, description=None):
        menu_item = Menu(restaurant_id=restaurant_id, dish_name=dish_name, price=price, description=description)
        db.session.add(menu_item)
        db.session.commit()
        return menu_item

    def update_menu(menu_id, **kwargs):
        menu_item = Menu.query.get(menu_id)
        if menu_item:
            for key, value in kwargs.items():
                setattr(menu_item, key, value)
            db.session.commit()
            return menu_item
        return None

    def delete_menu(menu_id):
        menu_item = Menu.query.get(menu_id)
        if menu_item:
            db.session.delete(menu_item)
            db.session.commit()
            return True
        return False

    
    def get_menus_for_restaurant(restaurant_id):
        return Menu.query.filter_by(restaurant_id=restaurant_id).all()