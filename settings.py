import os
from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger

load_dotenv(os.path.join(os.getcwd(), '.env'))

app = Flask(__name__)
app.config.update({
    'ENV': os.environ.get('ENV'),
    'DEBUG': os.environ.get('DEBUG') in ['True', 'true'],
    'TESTING': os.environ.get('TESTING') in ['True', 'true'],
    'SECRET_KEY': os.environ.get('SECRET_KEY'),
    'JWT_SECRET_KEY': os.environ.get('JWT_SECRET_KEY'),
    'JWT_ACCESS_TOKEN_EXPIRES': int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES')),
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'JSON_SORT_KEYS': False,
    'MAIL_SERVER': os.environ.get('MAIL_SERVER'),
    'MAIL_PORT': os.environ.get('MAIL_PORT'),
    'MAIL_USE_TLS': os.environ.get('MAIL_USE_TLS') in ['True', 'true'],
    'MAIL_USE_SSL': os.environ.get('MAIL_USE_SSL') in ['True', 'true'],
    'MAIL_DEBUG': os.environ.get('DEBUG') in ['True', 'true'],
    'MAIL_USERNAME': os.environ.get('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.environ.get('MAIL_PASSWORD'),
    'MAIL_SUPPRESS_SEND': False,
    'SWAGGER': {
        'title': os.environ.get('NAME'),
        'info': {
            'title': os.environ.get('NAME'),
            'version': os.environ.get('VERSION'),
        },
        'specs': [
            {
                'endpoint': 'doc',
                'route': '/api/doc.json',
                'rule_filter': lambda rule: True,
                'model_filter': lambda tag: True,
            }
        ],
        'static_url_path': '/static/swagger',
        'swagger_ui': True,
        'specs_route': '/api/doc',
        'consumes': [
            'application/x-www-form-urlencoded',
        ],
        'produces': [
            'application/json',
        ],
        'securityDefinitions': {
            'Bearer': {
                'type': 'apiKey',
                'description': 'Authorization: Bearer {jwt}',
                'name': 'Authorization',
                'in': 'header',
                'scheme': 'Bearer',
                'template': 'Bearer {apiKey}'
            }
        },
        'security': [
            {
                'Bearer': []
            }
        ],
        'uiversion': 3,
        'ui_params': {
            'apisSorter': 'alpha',
            'operationsSorter': 'alpha',
        },
        'hide_top_bar': True,
        'footer_text': '&copy; 2021. All rights reserved.',
    }
})

db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)
jwt = JWTManager(app)
swagger = Swagger(app)
