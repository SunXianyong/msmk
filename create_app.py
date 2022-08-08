import os

from flask import Flask,current_app
from flask_migrate import Migrate
from flask_smorest import Api

from models.model import db
from utils.cache import cache
from view import *


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)
    db.init_app(app)
    Migrate(app, db)
    cache.init_app(app)

    api = Api(app)
    api.register_blueprint(teachers_bp)
    api.register_blueprint(students_bp)
    api.register_blueprint(courses_bp)
    api.register_blueprint(robot_bp)
    api.register_blueprint(exercise_bp)
    api.register_blueprint(paper_bp)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    socketio.init_app(app, cors_allowed_origins='*', logger=True, engineio_logger=True)

    return socketio, app
