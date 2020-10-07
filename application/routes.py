from settings import app
from flask_restful import Api
from application.controllers.home import *
from application.controllers.auth import *

api = Api()

api.add_resource(Home, '/')
api.add_resource(Login, '/auth/login')
api.add_resource(Refresh, '/auth/refresh')
api.add_resource(Me, '/auth/me')

api.init_app(app)


@app.errorhandler(404)
def not_found(e):
    return {'msg': str(e)}, 404
