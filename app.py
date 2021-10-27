from flask import Flask
from service.init_service import init_db

application = Flask(__name__)


@application.cli.command('init')
def initdb_command():
    init_db()


if __name__ == '__main__':
    application.run()

# circular imports for using flask application in multiple modules
# must be imported in bottom of the file
import controller.controller
