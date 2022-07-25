from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

student2teacher = db.Table(
    "student2teacher",
    db.Column("id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("student_id", db.Integer, db.ForeignKey("students.id")),
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.id")),
    db.UniqueConstraint("student_id", "teacher_id", name="student2teacher_ids")
)


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, default="名称", comment="用户名")
    attention_num = db.Column(db.Integer, default=0, comment="关注数量")
    phone = db.Column(db.String(11), unique=True, nullable=False, comment="手机号")
    password = db.Column(db.String(16), nullable=False, comment="密码")
    info = db.Column(db.String(256), default="。。。", comment="简介")
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    status = db.Column(db.BOOLEAN, default=True, comment="上线状态")
    photo = db.Column(db.String(256), default="http://xxxxxx/default_photo", comment="头像")
    students = db.relationship("Student", secondary=student2teacher, backref="teachers")

    def __repr__(self):
        return f"老师： {self.name}"


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, default="名称", comment="用户名")
    phone = db.Column(db.String(11), unique=True, nullable=False, comment="手机号")
    password = db.Column(db.String(16), nullable=False, comment="密码")
    info = db.Column(db.String(256), default="。。。", comment="简介")
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    status = db.Column(db.BOOLEAN, default=True, comment="上线状态")
    photo = db.Column(db.String(256), default="http://xxxxxx/default_photo", comment="头像")
    money = db.Column(db.Float(5, 2), default=0.00, comment="学习币")
    course_num = db.Column(db.Integer, default=0, comment="特色课数量")
    solo_num = db.Column(db.Integer, default=0, comment="一对一课数量")
    vip = db.Column(db.DateTime, default=0, comment="会员")


class Course(db.Model):
    __tablename__ = "courses"

    # 基本属性
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, default="名称", comment="课程名字")
    info = db.Column(db.String(256), default="。。。", comment="简介")
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")

    # 表特色属性
    start_time = db.Column(db.DateTime, nullable=True, comment="开课时间")
    end_time = db.Column(db.DateTime, nullable=True, comment="结束时间")
    total = db.Column(db.Integer, comment="本课程包含几节课")
    total_time = db.Column(db.Integer, comment="总时长（秒数）")
    photo = db.Column(db.String(256), default="http://xxxxxx/default_photo", comment="书皮")
    money = db.Column(db.Float(5, 2), default=0.00, comment="价格")

    # 业务属性
    type = db.Column(db.Integer, default=1, comment="{1:特色课，2:一对一}")
    teacher_num = db.Column(db.Integer, default=0, comment="讲师人数")
    collect_num = db.Column(db.Integer, default=0, comment="收藏量")
    course_num = db.Column(db.Integer, default=0, comment="预约量")
    buy_num = db.Column(db.Integer, default=0, comment="购买量")

    # 与其他表关系属性
    solo_num = db.Column(db.Integer, default=0, comment="一对一课数量")
    vip_free = db.Column(db.DateTime, default=0, comment="会员")


class Excerpt(db.Model):
    __tablename__ = "excerpts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courses_id = db.Column(db.Integer, index=True, comment="关联课程id")
    name = db.Column(db.String(16), nullable=False, default="名称", comment="课节名字")


class CourseTeacher(db.Model):
    __tablename__ = "courseteachers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courses_id = db.Column(db.Integer, comment="关联课程id")
    teacher_id = db.Column(db.Integer, comment="关联老师id")

    def __repr__(self):
        return f"老师： {self.name}"

    __table_args__ = (
        db.UniqueConstraint("courses_id", "teacher_id", name="courseteacher_ids"),
    )


class CourseOrder(db.Model):
    __tablename__ = "courseorders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courses_id = db.Column(db.Integer, comment="关联课程id")
    courses_name = db.Column(db.String(16), nullable=False, default="名称", comment="课程名字")
    student_id = db.Column(db.Integer, comment="关联老师id")
    real_price = db.Column(db.Integer, comment="实付价格")
    price = db.Column(db.Integer, comment="标价")
    create_time = db.Column(db.DateTime, default=datetime.now,comment="下订单时间")
    fail = db.Column(db.BOOLEAN, comment="退款")
    coupon_id = db.Column(db.Integer, comment="优惠券id")

    def __repr__(self):
        return f"课程订单： {self.name}"

    # __table_args__ = (
    #     db.UniqueConstraint("courses_id", "teacher_id", name="courseteacher_ids"),
    # )
