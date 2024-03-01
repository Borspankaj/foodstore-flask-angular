from flask import Flask
from flask_cors import CORS
from extensions import db
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.user_resource import UserResource
from resources.login_resource import LoginResource , LogoutResource
from resources.menu_resource import MenuResource , RestrauntMenuResource
from resources.restaurant_resource import RestaurantResource , SearchResource , OwnerResource
from resources.cart_resource import CartResource , CartItemResource
from resources.order_resource import OrderResource , OrderItemResource
def create_app() :
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodstore.db'
    app.config['JWT_SECRET_KEY'] = 'my-key-qwer4321'
    register_extensions(app)
    return app

def register_extensions(app) :
    db.init_app(app)
    CORS(app)
    jwt = JWTManager(app)
    api = Api(app)
    register_api(api)
    with app.app_context():
        db.create_all()
        
def register_api(api) :
    api.add_resource(UserResource, '/api/user' , '/api/user/<string:user_email>')
    api.add_resource(LoginResource ,'/api/login' )
    api.add_resource(LogoutResource ,  '/api/logout/<string:user_email>')
    api.add_resource(MenuResource ,'/api/menu' , '/api/menu/<int:menu_id>')
    api.add_resource(RestrauntMenuResource , '/api/get-restaurant-menu/<int:restaurant_id>')
    api.add_resource(RestaurantResource ,'/api/restaurant' ,'/api/restaurant/<int:restaurant_id>')
    api.add_resource(SearchResource , '/api/restaurants')
    api.add_resource(OwnerResource , '/api/owner-restaurants/<string:user_email>' , )
    api.add_resource(CartResource  , '/api/cart' , '/api/cart/<string:user_email>') 
    api.add_resource(CartItemResource , '/api/cart-item/<string:user_email>' , '/api/cart-item/<string:user_email>/<int:menu_id>')
    api.add_resource(OrderResource , '/api/order' , '/api/order/<string:user_email>')
    api.add_resource(OrderItemResource , '/api/manage-orders/<int:restaurant_id>')
if __name__ == "__main__" :

    app = create_app()
    app.run(debug=True , port = 4000)