from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db
from resources.user import UserRegister,UserLogin
from resources.maqamat import MaqamatList, MaqamUpload, MaqamDetail
from resources.book_call import BookCall, BookingDetail
from flask_cors import CORS
from flasgger import Swagger
swagger = Swagger(app)




def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "987456321"  # Setting a  secret key for JWT

    db.init_app(app)

    jwt = JWTManager(app)  # Initialize JWTManager

    api = Api(app)
    
    # User Endpoints
    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    
    # Maqamat Endpoints
    api.add_resource(MaqamatList, "/maqamat")
    api.add_resource(MaqamUpload, "/maqamat/upload")
    api.add_resource(MaqamDetail, "/maqamat/<int:maqam_id>")
    
    # Booking Endpoints
    api.add_resource(BookCall, "/book-call")
    api.add_resource(BookingDetail, "/book-call/<int:booking_id>")
    
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
