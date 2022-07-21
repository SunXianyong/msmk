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

