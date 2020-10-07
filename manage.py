import os
from settings import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db, directory=os.path.join('application', 'migrations'))
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from application.models.user import User

if __name__ == '__main__':
    manager.run()
