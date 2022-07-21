import os

from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api

from models.model import db
from view import *


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    db.init_app(app)
    Migrate(app, db)

    api = Api(app)
    api.register_blueprint(teachers_bp)
    api.register_blueprint(students_bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
