import os
import json
from application.models.user import User


def load_fixture(name):
    """
    Load json fixture (./application/fixtures/[name].json).
    :param name: string
    :return: object
    """
    return json.load(open(os.path.join(os.getcwd(), 'application', 'fixtures', '{}.json'.format(name))))


print('Users loading...')

users = load_fixture('users')
for item in users:
    user = User(item['email'], item['password'], item['name'], item['last_name'], item['roles'])
    user.save()

print('{} users loaded!'.format(len(users)))
