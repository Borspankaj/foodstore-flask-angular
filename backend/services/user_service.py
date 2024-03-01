from repository.user_repository import UserRepository
from DTO.user_dto import UserDto
class UserService :
    
    def get_user(user_email) :
        user = UserRepository.get_user(user_email)
        user_data = UserDto.get_userdata_from_model(user)
        return user_data
        
    def create_user(request_data) :
        name , email , phone_number , password , role = UserDto.get_user_data_from_request(request_data)
        new_user = UserRepository.add_user(name=name , email=email , phone_number= phone_number , password= password ,role=role)
        user_data = UserDto.get_userdata_from_model(new_user)
        return user_data
        
    def update_user(request_data , user_email):
        name , email , phone_number , password , role = UserDto.get_user_data_from_request(request_data)
        user = UserRepository.update_user(user_email , name = name , email = email , phone_number = phone_number , password = password , role = role)
        user_data = UserDto.get_userdata_from_model(user)
        return user_data
    
    def delete_user(user_email) :
        if UserRepository.delete_user(user_email) :
            return True
        return False