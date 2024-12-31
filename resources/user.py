from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token
#from marshmallow import Schema, fields, ValidationError
from models.user import User
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from schemas import UserSchema

user_schema = UserSchema()


# User registration resource
class UserRegister(Resource):
    def post(self):
        data = request.get_json()

        # Validate input data
        errors = user_schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        # Check if the user already exists
        if User.query.filter_by(email=data["email"]).first():
            return {"message": "A user with that email already exists."}, 400

        # Hash the password
        hashed_password = generate_password_hash(data["password"])

        # Create a new user
        new_user = User(
            name=data.get("name"),
            email=data["email"],
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully."}, 201


class UserLogin(Resource):
    def post(self):
        data = request.get_json()

        # Validate input data
        errors = user_schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        # Fetch user from the database
        user = User.query.filter_by(email=data["email"]).first()
        if not user or not check_password_hash(user.password, data["password"]):
            return {"message": "Invalid email or password."}, 401

        # Generate JWT token
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200