from flask_restful import Resource


class Home(Resource):
    @staticmethod
    def get():
        return {'success': True}
