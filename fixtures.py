import os
import json
from application.models.user import User

FIXTURES_DIR = os.path.join(os.getcwd(), 'application', 'fixtures')

print('Users loading...')

users = json.load(open(os.path.join(FIXTURES_DIR, 'users.json')))
for item in users:
    user = User(item['email'], item['password'], item['name'], item['last_name'], item['roles'])
    user.save()

print('{} users loaded!'.format(len(users)))
