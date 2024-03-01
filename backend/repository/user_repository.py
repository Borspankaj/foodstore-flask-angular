from extensions import db
from models.user import User

class UserRepository :
    def get_user(user_email) :
        return User.query.filter_by(email = user_email).first()
        
    def add_user(name, email, phone_number, password, role="Customer"):
        user = User(name=name, email=email, phone_number=phone_number, password=password, role=role)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(user_email, **kwargs):
        user = User.query.filter_by(email = user_email).first()
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            db.session.commit()
            return user
        return None

    def delete_user(user_email):
        user = User.query.filter_by(email = user_email).first()

        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
