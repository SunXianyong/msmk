from flask import request, make_response
from flask_smorest import Blueprint

from models.model import db, Student, Teacher

students_bp = Blueprint("student", __name__, url_prefix="/")


# @students_bp.before_request
# def login_status():
#     if request.cookies.get("student_id"):
#         ...
#     else:
#         ...


@students_bp.route("student", methods=["post"])
def login_stu():
    info = request.json
    student = db.session.query(Student.id).filter_by(**info).one()
    if student:
        resp = make_response("shi")
        resp.set_cookie("student_id", str(student.id), max_age=36000)
        return resp
    return {"code": 2000}


@students_bp.route("attention", methods=["put"])
def attention2teacher():
    teacher_id = request.json.get("teacher_id")
    student_id = request.cookies.get("student_id")
    teacher = db.session.query(Teacher).filter_by(id=teacher_id).one()
    student = db.session.query(Student).filter_by(id=student_id).one()
    if teacher.students:
        return "已经关注过"
    teacher.students.append(student)
    teacher.attention_num += 1
    return {"code": 200}
