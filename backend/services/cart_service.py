from extensions import db
from models.cart import Cart, CartItem
from utils.utils import get_user_id_by_email , get_menu_price

class CartService:
    @staticmethod
    def get_cart_for_customer(user_email):
        customer_id = get_user_id_by_email(user_email)
        return Cart.query.filter_by(customer_id=customer_id).first()

    @staticmethod
    def create_cart(customer_id, restaurant_id):
        cart = Cart(customer_id=customer_id, restaurant_id=restaurant_id)
        db.session.add(cart)
        db.session.commit()
        return cart

    @staticmethod
    def add_to_cart(user_email, menu_id, quantity , restaurant_id):
        customer_id = get_user_id_by_email(user_email)
        cart = Cart.query.filter_by(customer_id = customer_id).first()
        if cart and cart.restaurant_id != restaurant_id :
            db.session.delete(cart)
            db.session.commit()
        if cart is None :
            cart = Cart(customer_id=customer_id , restaurant_id = restaurant_id)
            db.session.add(cart)  
        db.session.commit()
        cart_id = cart.id
        existing_item = CartItem.query.filter_by(cart_id=cart_id, menu_id=menu_id).first()
        if existing_item:
            existing_item.quantity += quantity
        else:
            new_item = CartItem(cart_id=cart_id, menu_id=menu_id, quantity=quantity)
            db.session.add(new_item) 
        cart.total_value = CartService.calculate_cart_total(cart_id)
        db.session.commit()
        return cart

    @staticmethod
    def delete_from_cart(cart_id, menu_id):
        cart = Cart.query.get(cart_id)

        if cart is None:
            return None

        item_to_delete = CartItem.query.filter_by(cart_id=cart_id, menu_id=menu_id).first()

        if item_to_delete:
            db.session.delete(item_to_delete)
            cart.total_value = CartService.calculate_cart_total(cart_id)
            db.session.commit()

        return cart

    @staticmethod
    def calculate_cart_total(cart_id):
        cart_items = CartItem.query.filter_by(cart_id=cart_id).all()
        total = sum( get_menu_price(item.menu_id)* item.quantity for item in cart_items)
        return total
