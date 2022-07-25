from flask import request
from flask_smorest import Blueprint

from models.model import db, CourseTeacher, Teacher, CourseOrder
from settings.setting import COURSE_INFO, Teacher_info
from utils.db import check_student_money
from utils.my_route import route_code, query2dict, commit_route

courses_bp = Blueprint("course", __name__, url_prefix="/")


@courses_bp.route("/course/info")
def get_course_info():
    course_id = request.args.get("course_id", None)
    if not course_id:
        return route_code("无课程", 408)
    courseteacher = db.session.query(CourseTeacher.teacher_id).filter_by(courses_id=course_id).all()
    teachers = db.session.query(*Teacher_info).filter(Teacher.id.in_([i.teacher_id for i in courseteacher])).all()
    course = db.session.query(*COURSE_INFO).filter_by(id=course_id).one()
    ret = query2dict(course, teachers=query2dict(teachers))
    return route_code(ret)


@courses_bp.route("/course/order", methods=["put"])
def add_course_order():
    course_id = request.args.get("course_id", None)
    coupon_id = request.args.get("coupon_id", None)
    student_id = request.cookies.get("student_id")

    student, course, coupon_money = check_student_money(course_id=int(course_id), student_id=int(student_id))
    if not student:
        return route_code("操作失败", 444)

    # 学生余额减少，购买课程量增加
    real_price = course.money - coupon_money
    student_buy_num = [None, student.course_num, student.solo_num][course.type]
    student_buy_num += 1
    student.money -= real_price

    # 课程购买数量
    course.buy_num += 1

    # 添加订单
    order = {
        "courses_id": course.id,
        "courses_name": course.name,
        "student_id": student.id,
        "real_price": real_price,
        "price": course.money,
        "fail": 0,
        "coupon_id": coupon_id,
    }

    db.session.add(CourseOrder(**order))
    return commit_route("购买成功")
