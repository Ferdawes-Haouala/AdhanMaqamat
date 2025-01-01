from flask.views import MethodView
from flask_smorest import Blueprint
from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token
from models.user import User
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from schemas import UserSchema

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, description="User registered successfully.")
    def post(self, user_data):
        if User.query.filter_by(email=user_data["email"]).first():
            return {"message": "A user with that email already exists."}, 400

        user_data["password"] = generate_password_hash(user_data["password"])
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully."}

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema, as_kwargs=True)
    @blp.response(200, description="Access token generated.")
    def post(self, email, password):
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return {"message": "Invalid email or password."}, 401
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}