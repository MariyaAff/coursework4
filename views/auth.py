from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service, user_service

auth_ns = Namespace("auth")

@auth_ns.route("/register")
class RegisterView(Resource):
    def post(self):
        req_json = request.json
        email = req.json.get("email"
        password = req.json.get("password")

        if None in [email, password]:
            return "", 400

        req_json["favorite_genre"] = 1
        user_service.create(req_json)

        return "User created", 201

@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req.json.get("email"
        password = req.json.get("password")

        if None in [email, password]:
            return "", 400

        tokens = auth_service.generate_token(email, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        access_token = req_json.get("access_token")
        refresh_token = req_json.get("refresh_token")
        valid = auth_service.valid_token(access_token, refresh_token)
        if not valid:
            return "Invalid tiken", 400
        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201

