from extensions import db
from models.order import Order, OrderItem
from utils.utils import get_user_id_by_email
from models.cart import Cart
from DTO.order_dto import OrderDto
from flask import jsonify
class OrderService:
    @staticmethod
    def place_order(user_email):
        customer_id = get_user_id_by_email(user_email)
        cart = Cart.query.filter_by(customer_id = customer_id).first()
        
        if cart :
            order = Order(customer_id=customer_id , restaurant_id = cart.restaurant_id , status = "Order Placed")
            db.session.add(order)
            for item in cart.items:
        
                order_item = OrderItem(
                    order_id=order.id,
                    menu_id=item.menu_id,
                    quantity = item.quantity,
                   
                )
                db.session.add(order_item)
                db.session.delete(item)
                db.session.commit()
                
        cart.total_value = 0
        db.session.commit()
        return jsonify(message = "Ordered placed successfully")


    @staticmethod
    def get_orders_for_customer(user_email):
        customer_id = get_user_id_by_email(user_email)
        print(customer_id)
        return Order.query.filter_by(customer_id=customer_id).all()

    @staticmethod
    def update_order(request_data):
        try :
            order_id = request_data["order_id"]
            order_status = request_data["order_status"]
            order = Order.query.get(order_id)
            order.status = order_status
            db.session.commit()
            return jsonify(message = "Status Changed") 
        except Exception as e :
            db.session.rollback()
            return jsonify(message = f'{e}')
        
        
    @staticmethod
    def get_orders_by_owner(restaurant_id):
    
        try :
            orders = Order.query.filter_by(restaurant_id = restaurant_id)
            return OrderDto.get_order_data(orders)
        except Exception as e :
            return f'{e}'