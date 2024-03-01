from flask_restful import Resource, reqparse
from services.user_service import UserService
class UserResource(Resource) :
    
    def get(self ,user_email) :
        response_data = UserService.get_user(user_email)
        if response_data : return response_data
        else: return {'message': 'User not found'}, 404
        
    def post(self ) :
        request_data = reqparse.request.get_json()
        print(request_data)
        try :
            response_data = UserService.create_user(request_data)
        
            return {'message': 'User created successfully' ,
                    'data' : response_data}, 200
        except Exception as e:
            return {'message' : 'internal error' , 
                    'error' : e}
            
    def put(self , user_email) :
        request_data = reqparse.request.get_json()
        response_data = UserService.update_user(request_data , user_email)
        if response_data != None:
            return {'message': 'User updated successfully' ,
                'data' : response_data } , 200
        else :
            return {'message': 'User not found'}, 404
        
    def delete(self , user_email) :
        if UserService.delete_user(user_email):
            return {'message': 'Employee deleted successfully'}
        else:
            return {'message': 'Employee not found'}, 404
    