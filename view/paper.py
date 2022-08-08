from random import randint

from flask import request
from flask_smorest import Blueprint

from models.model import db, Exercise4Course, Exercise
from settings.setting import Exercise_info, EXERCISE_TIANKONG, Exercise_xuanze
from utils.my_route import route_code

paper_bp = Blueprint("paper", __name__, url_prefix="/")


@paper_bp.route("/paper")
def get_exercises():
    # json = request.json
    json = request.args
    course_id = json.get("course_id")

    # 获取课程相关题目id
    exercises_ids = db.session.query(Exercise4Course.exercise_id).filter_by(course_id=course_id).all()
    exercises_ids = [i.exercise_id for i in exercises_ids]

    # 根据题类型获取题目
    exercise_x = db.session.query(*Exercise_info).filter(Exercise.id.in_(exercises_ids),
                                                         Exercise.title_type == Exercise_xuanze).all()
    exercise_t = db.session.query(*Exercise_info).filter(Exercise.id.in_(exercises_ids),
                                                         Exercise.title_type == EXERCISE_TIANKONG).all()

    # 随机组合20到
    ret_exercise = [exercise_x[randint(0, len(exercise_x))] for _ in range(10)] + \
                   [exercise_t[randint(0, len(exercise_t))] for _ in range(10)]

    # 创建一张模拟考试的卷子
    # 用户与卷子关系

    return route_code(ret_exercise)
