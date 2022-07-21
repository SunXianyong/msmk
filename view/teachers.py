from flask_smorest import Blueprint

from models.model import db, Teacher
from utils.my_route import ret_route
from settings.config import Teacher_info

teachers_bp = Blueprint("teacher", __name__, url_prefix="/")


@teachers_bp.route("teachers")
def get_teachers():
    teachers = db.session.query(Teacher.name, Teacher.photo).limit(10).all()
    return ret_route(teachers)


@teachers_bp.route("teacher/<int:teacher_id>")
def get_teacher_info(teacher_id):
    teacher = db.session.query(*Teacher_info). \
        filter_by(id=teacher_id).one()
    return ret_route(teacher)


