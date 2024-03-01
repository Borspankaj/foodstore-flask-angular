from models.user import User
from models.menu import Menu
def get_user_id_by_email(user_email) :
    user = User.query.filter_by(email = user_email).first()
    return user.id

def get_menu_price(menu_id) :
    menu = Menu.query.get(menu_id)
    return menu.price