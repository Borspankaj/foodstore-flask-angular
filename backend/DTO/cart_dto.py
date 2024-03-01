class CartDto :
    
    def get_cart_data_from_request(request_data) :
        
        menu_id = request_data.get("menu_id", None)
        quantity = request_data.get("quantity", 0)
        restaurant_id = request_data.get("restaurant_id" , None)
        return menu_id , quantity, restaurant_id