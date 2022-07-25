from models.model import db, Course, Student


def check_student_money(course_id: int, student_id: int):
    # todo 优惠卷表映射、查询语句
    coupon_money = 0
    course = db.session.query(Course).filter_by(id=course_id).one()
    student = db.session.query(Student).filter_by(id=student_id).one()
    # student = db.session.query(Student.money, Student.course_num, Student.solo_num).filter_by(id=student_id).one()
    if student.money >= (course.money - coupon_money):
        return student, course, coupon_money
    return None, None, None
