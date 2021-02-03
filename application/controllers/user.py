from flask_jwt_extended import jwt_required
from flask_restful import Resource
from application.utils.helpers import doc, current_user


class Me(Resource):
    @doc('user/me')
    @jwt_required
    def get(self):
        return current_user()


class Profile(Resource):
    @doc('user/profile')
    @jwt_required
    def patch(self):
        return {
            'success': True,
        }
