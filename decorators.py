#import jwt
from flask import request
from flask_restx import abort
from constants import JWT_SECRET

def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in requesr.headers:
            abort(401)

            data = request.headers["Authorization"]
            token = data.split("Bearer ")[-1]
            try:
                jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            except Exception as e:
                print("JWT decode error", e)
                abort(401)
            return func(*args, **kwargs)
        return wrapper

    def admin_required(func):
        def wrapper(*args, **kwargs):
            if "Authorization" not in requesr.headers:
                abort(401)

                data = request.headers["Authorization"]
                token = data.split("Bearer ")[-1]
                try:
                    user = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
                    role = user.get("role")
                    if role != "admin":
                        abort(403)

                except Exception as e:
                    print("JWT decode error", e)
                    abort(401)
                return func(*args, **kwargs)
            return wrapper
