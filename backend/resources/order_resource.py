from flask_restful import Resource, reqparse
from services.order_service import OrderService
from DTO.order_dto import OrderDto
class OrderResource(Resource) :
    
    def get(self , user_email) :
        try:
            print(1)
            order = OrderService.get_orders_for_customer(user_email)
            print("----")
            if order:
                print("==")
                order_data = OrderDto.get_order_data(order)
                return order_data, 200
            else:
                return {"message": "Order not found"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
    
    def post(self):
        try:
            request_data = reqparse.request.get_json()
            user_email = request_data["email"]
            OrderService.place_order(user_email)
            return {"message": "Order placed successfully"}, 201
        except Exception as e:
            print(e)
            return {"message": str(e)}, 500
        
    def put(self) :

        request_data = reqparse.request.get_json()
        try:
            OrderService.update_order(request_data)
            return {"message": "Order status changed successfully"}, 200
        except Exception as e:
            return {"message": str(e)}, 500
        
class OrderItemResource(Resource) :
    
    def get(self, restaurant_id) :
        
        try :
            orders = OrderService.get_orders_by_owner(restaurant_id)
            print(orders)
            return { "data" : orders} , 200
        except Exception as e :
            return { "message" : "Error"} , 500