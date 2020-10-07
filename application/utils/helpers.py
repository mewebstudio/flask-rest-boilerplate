import os
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity
from application.models.user import User, UserSchema
from settings import db


def doc(name):
    """
    API Doc YAML loader.
    :param name: string
    :return: string
    """
    return swag_from(os.path.join(os.getcwd(), 'application/doc/{}.yaml'.format(name)))


def current_user():
    """
    JWT authenticated user.
    :return: object
    """
    email = get_jwt_identity()
    user = db.session.query(User).filter(User.email == email).first()
    users_schema = UserSchema()
    return users_schema.dump(user)
