# flask-rest-boilerplate

## Requirements:
flask, python-dotenv, SQLAlchemy, Flask-SQLAlchemy, Flask-Migrate, Flask-Script, Flask-JWT-Extended, Flask-RESTful, Flask-Marshmallow, Flask-Mail, flasgger, marshmallow-sqlalchemy, Werkzeug, psycopg2

## Installation
```bash
pip install -r requirements.txt
```

for development
```bash
cp .env.dev .env
```

for production
```bash
cp .env.prod .env
```

`Edit this .env file as you wish.`

## Migrate DB
```bash
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

## Load dummy data
```bash
$ python fixtures.py
```

## Run app
```bash
$ python app.py
```

## Mailing example
```python
from flask_mail import Message
from settings import mail

def send_email():
    msg = Message(
        subject='Hello',
        sender=('Sender Name', 'sender@example.com'),
        recipients=['recipient@example.com'],
        html='<p><strong>Hello,</strong></p><p>body</p>',
    )
    mail.send(msg)
```
