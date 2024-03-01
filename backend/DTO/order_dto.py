from utils.utils import get_menu_price
from DTO.menu_dto import MenuDto
class OrderDto :
    def get_order_data(orders) :
        order_data = { "data" : [
            {
                "order_id" : order.id ,
                "customer_id" : order.customer_id ,
                "restaurant_id" : order.restaurant_id ,
                "status" : order.status ,
                "items" : [
                    {
                        "menu_id" : item.menu_id ,
                        "dish_name" : MenuDto.get_dish_name(item.menu_id) ,
                        "order_item_id" : item.id ,
                        "quantity" : item.quantity ,
                        
                    }
                    for item in order.items
                ]
            }
            for order in orders
            ] 
        }
        return order_data
    
    def get_orders_for_owner(orders) :
        data = {
            "orders" : [
                {
                    "order_item_id" : item.id ,
                    "book_id" : item.book_id ,
                    # "book_title" : get_book_title(item.book_id) ,
                    "status" : item.status
                }
                for item in orders
            ]
        }
        
        return data