from flask import request
from flask_smorest import Blueprint

from models.model import db
from settings.setting import Teacher_info
from utils.cache import cache, redis_cil
from utils.my_route import route_code

teachers_bp = Blueprint("teacher", __name__, url_prefix="/")


@teachers_bp.route("/teachers", methods=["post"])
def get_teachers():
    # teacher_id = int(request.args.get("teacher_id"))
    # teachers: Pagination = db.session.query(Teacher.name, Teacher.photo) \
    #     .filter(Teacher.id > teacher_id) \
    #     .paginate(0, 2, error_out=False)
    #
    # print("-" * 10)
    #
    # return route_code(teachers.items)
    msg = request.json.get("msg")

    # redis 连接
    pub = redis_cil()

    # 发布 消息 msg  给订阅了 teachers 的用户
    pub.publish("teachers", msg)
    return


@teachers_bp.route("/teacher/<int:teacher_id>")
@cache.cached(1500)
def get_teacher_info(teacher_id):
    teacher = db.session.query(*Teacher_info). \
        filter_by(id=teacher_id).one()
    return route_code(teacher)
