from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from db import db
from resources.user import  blp as UserBlueprint
from resources.maqamat import blp as MaqamatBlueprint
from resources.maqam_details import blp as MaqamDetailsBlueprint
from resources.book_call import blp as BookCallBlueprint
from flask_cors import CORS
from flasgger import Swagger


def create_app():
    app = Flask(__name__)
    CORS(app)
    # Flask-Smorest Configuration
    app.config["API_TITLE"] = "Adhan Maqamat API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    # Database Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "987456321"  # Setting a  secret key for JWT

    db.init_app(app)

    jwt = JWTManager(app)  # Initialize JWTManager

    # Initialize Flask-Smorest API
    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(MaqamatBlueprint)
    api.register_blueprint(MaqamDetailsBlueprint)
    api.register_blueprint(BookCallBlueprint)
    
    
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
