from models.user import User
from models.token import UserToken
from DTO.user_dto import UserDto
import secrets
from extensions import db
class AuthService :
    
    def authenticate(request_data) :
        try :
            print(request_data)
            user_email = request_data['email']
            print("--")
            user = User.query.filter_by(email = user_email).first()
            print(user)
            if user.password == request_data['password'] :
                return UserDto.get_userdata_from_model(user=user)
            else :
                return None
        except Exception as e :
            print(e)
            return  None
        
    def create_token(user_email) :
        
        existing_token = UserToken.query.filter_by(email = user_email).first()
        if existing_token ==None :   
            new_user_token = UserToken(
                email = user_email
            )
            token = secrets.token_hex(16)
            new_user_token.token = token
        
            try :
                db.session.add(new_user_token)
                db.session.commit()
                return token
            except Exception as e :
                print(e)
                db.session.rollback()
                return None
            
        else :
            new_token = secrets.token_hex(16)
            existing_token.token = new_token
            try :
                db.session.commit()
                return new_token
            except Exception as e :
                print(e)
                db.session.rollback()
                return None
    
    def is_authorized(token) :
        existing_token = UserToken.query.filter_by(token = token).first()
        print(existing_token)
        if existing_token != None :
            print('----')
            return True
        return False

    def is_authorized_admin(token) :
        existing_token = UserToken.query.filter_by(token = token).first()
        print(existing_token)
        if existing_token != None :
            email = existing_token.email
            user = User.query.filter_by(email = email).first()
            if user.role == 'ADMIN' :
                return True
            return False
        return False
    
    def delete_token(user_email) :
        print("11111")
        user_token = UserToken.query.filter_by(email = user_email).first()
        if user_token:
            
            try :
                db.session.delete(user_token)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                db.session.rollback() 
                return False
            
        return False