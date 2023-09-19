
from flask import (
    jsonify, 
    request
)
import hashlib

import jwt
from datetime import datetime, timedelta

# Define a secret key for signing the token
SECRET_KEY = 'your_secret_key_here'

from src.infra.db.repositories.useridentity_repository import UserIdentityRepository

class UserIdentityHandler:

    def __init__(self):
        pass

    def handle_post_login():
        body = request.get_json()

        if body is None:
            return jsonify({"error": "Invalid request body by missing any fields `username` or `password`"}), 400

        if "username" not in body or "password" not in body:
            return jsonify({"error": "Invalid request body by missing any fields `username` or `password`"}), 400


        repository = UserIdentityRepository()

        password = hashlib.md5(body["password"].encode()).hexdigest()
        result = repository.authenticate(body["username"], password)

        if result is None:
            return jsonify({"error": "Invalid credentials"}), 401

        # Define payload (claims) for the token
        payload = {
            "sub": result[0],
            "exp": datetime.utcnow() + timedelta(days=30)
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({
            "access_token": access_token,
        })

    def handle_post_validate_token():
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        # Remove the Bearer prefix from the token
        token = str.replace(str(token), 'Bearer ', '')

        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # Perform additional checks if needed, e.g., token expiration, user validation, etc.
            return jsonify({"message": "Token is valid"})
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except jwt.DecodeError:
            return jsonify({"message": "Token is invalid"}), 401

    def handle_post_register_user():
        body = request.get_json()

        if body is None:
            return jsonify({"error": "Invalid request body by missing any fields `username`, `password` or `email`"}), 400

        if "username" not in body or "password" not in body or "email" not in body:
            return jsonify({"error": "Invalid request body by missing any fields `username`, `password` or `email`"}), 400

        repository = UserIdentityRepository()

        user_exists = repository.get_by_username_or_email(body["username"], body["email"])

        if user_exists is not None:
            return jsonify({"error": "User already exists"}), 409

        password = hashlib.md5(body["password"].encode()).hexdigest()
        result = repository.create(body["username"], password, body["email"])

        if result is None:
            return jsonify({"error": "Error while creating the user"}), 500

        return jsonify({"message": "User created successfully"})




