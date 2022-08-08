from flask import request
from flask_smorest import Blueprint

from models.model import db, Exercise
from utils.my_route import route_code
from settings.setting import Exercise_info

exercise_bp = Blueprint("exercise", __name__, url_prefix="/")


@exercise_bp.route("/exercise")
def get_exercises():
    args = request.args
    pagintion = db.session.query(*Exercise_info).all()

    return route_code(pagintion)

