

class UserDto :
    
    def get_userdata_from_model(user) :
        if user :
            return {
                'name' : user.name ,
                'email' : user.email ,
                'phone_number' : user.phone_number ,
                'role' :user.role
                
            }
        
        else :
            return {
        
            }
            
    def get_user_data_from_request(request_data) :
        name =  ""
        email = ""
        phone_number = ""
        password = ""
        role = ""
        if request_data["name"] : name = request_data["name"]
        if request_data["email"] : email = request_data["email"]
        if request_data["phone_number"] : phone_number = request_data["phone_number"]
        if request_data["password"] : password = request_data["password"]
        if request_data["role"] : role = request_data["role"]
        return (name , email , phone_number , password , role )
        