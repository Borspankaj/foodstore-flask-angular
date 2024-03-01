from flask import request
from flask_restful import Resource , reqparse
from services.cart_service import CartService
from DTO.cart_dto import CartDto
from DTO.menu_dto import MenuDto
class CartResource(Resource):
    def get(self, user_email):
        cart = CartService.get_cart_for_customer(user_email)

        if cart:
            
            cart_data = {
                'id': cart.id,
                'customer_id': cart.customer_id,
                'restaurant_id': cart.restaurant_id,
                'total_value': cart.total_value,
                'items': [
                    {
                        'menu_id': item.menu_id,
                        'quantity': item.quantity , 
                        'price' : MenuDto.get_menu_price(item.menu_id) ,
                        'dish_name' : MenuDto.get_dish_name(item.menu_id)}  
                    for item in cart.items
                ]
            }
            return cart_data, 200
        else:
            return {'message': 'Cart not found'}, 404

    def post(self):
        data = request.get_json()
        customer_id = data.get('customer_id')
        restaurant_id = data.get('restaurant_id')

        if not customer_id or not restaurant_id:
            return {'message': 'Customer ID and Restaurant ID are required'}, 400

        cart = CartService.create_cart(customer_id, restaurant_id)

       
        cart_data = {
            'id': cart.id,
            'customer_id': cart.customer_id,
            'restaurant_id': cart.restaurant_id,
            'total_value': cart.total_value,
            'items': []
        }

        return cart_data, 201

class CartItemResource(Resource):
    def post(self, user_email):
        request_data = reqparse.request.get_json()
        
        menu_id , quantity , restaurant_id = CartDto.get_cart_data_from_request(request_data)
        print(request_data)
        cart = CartService.add_to_cart(user_email, menu_id, quantity , restaurant_id)

        if cart:
           
            cart_data = {
                'id': cart.id,
                'customer_id': cart.customer_id,
                'restaurant_id': cart.restaurant_id,
                'total_value': cart.total_value,
                'items': [
                    {
                        'menu_id': item.menu_id,
                        'quantity': item.quantity , 
                        'price' : MenuDto.get_menu_price(item.menu_id) ,
                        'dish_name' : MenuDto.get_dish_name(item.menu_id)}  
                    for item in cart.items
                ]
            }
            return cart_data, 200
        else:
            return {'message': 'Cart not found'}, 404

    def delete(self, user_email, menu_id):
        cart = CartService.delete_from_cart(user_email, menu_id)

        if cart:
           
            cart_data = {
                'id': cart.id,
                'customer_id': cart.customer_id,
                'restaurant_id': cart.restaurant_id,
                'total_value': cart.total_value,
                'items': [
                    {'menu_id': item.menu_id, 'quantity': item.quantity}
                    for item in cart.items
                ]
            }
            return cart_data, 200
        else:
            return {'message': 'Cart not found'}, 404
