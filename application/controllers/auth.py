from flask import request
from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required
)
from flask_restful import Resource

from application.models.user import *
from application.utils.helpers import doc


class Login(Resource):
    @doc('auth/login')
    def post(self):
        if not request.is_json:
            return {'msg': 'Missing JSON in request'}, 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)
        remember_me = request.json.get('remember_me', None)

        if not email:
            return {'msg': 'Missing email parameter'}, 400
        if not password:
            return {'msg': 'Missing password parameter'}, 400

        user = db.session.query(User).filter(User.email == email).first()
        if user is None or user.check_password(password) is not True:
            return {'msg': 'Bad credentials!'}, 401

        response = {'access_token': create_access_token(identity=email)}
        if remember_me is True:
            response.update({'refresh_token': create_refresh_token(identity=email)})

        return response, 200


class Refresh(Resource):
    @doc('auth/refresh')
    @jwt_refresh_token_required
    def patch(self):
        email = get_jwt_identity()
        return {'access_token': create_access_token(identity=email)}
