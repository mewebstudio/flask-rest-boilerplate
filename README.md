#BMO API

##Installation
```bash
pip install -r requirements.pip
```

for development
```bash
cp .env.dev .env
```

for production
```bash
cp .env.prod .env
```

##Migrate DB
```bash
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

## Load dummy data
```bash
$ python fixtures.py
```

##Mailing example
```bash
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
