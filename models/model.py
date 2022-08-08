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
    create_time = db.Column(db.DateTime, default=datetime.now, comment="下订单时间")
    fail = db.Column(db.BOOLEAN, comment="退款")
    coupon_id = db.Column(db.Integer, comment="优惠券id")

    def __repr__(self):
        return f"课程订单： {self.name}"

    # __table_args__ = (
    #     db.UniqueConstraint("courses_id", "teacher_id", name="courseteacher_ids"),
    # )


# 课程表
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


# 卷子表
class Paper(db.Model):
    __tablename__ = "paper"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(512), comment="卷名")
    paper_total = db.Column(db.Integer, comment="卷子总分")
    choice_total = db.Column(db.Integer, comment="选择题总分")
    write_total = db.Column(db.Integer, comment="填空总分")
    read_total = db.Column(db.Integer, comment="阅读理解总分")
    choice_num = db.Column(db.Integer, comment="选择题数量")
    write_num = db.Column(db.Integer, comment="填空数量")
    read_num = db.Column(db.Integer, comment="阅读理解数量")
    time_out = db.Column(db.Integer, comment="考试时长 (秒)")
    time_end = db.Column(db.DateTime, comment="结束时间")
    status = db.Column(db.Integer, comment="{0:模拟卷，1:正式卷}")
    money = db.Column(db.Integer, comment="价格")
    hot_count = db.Column(db.Integer, comment="热度")
    create_time = db.Column(db.Integer, comment="创建时间")


# 题目表
class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    big_title = db.Column(db.String(1024), comment="大标题题目")
    small_title = db.Column(db.String(512), comment="小标题题目")
    answer = db.Column(db.String(512), comment="答案")
    title_type = db.Column(db.Integer, comment="{1:选择，2：填空，3：阅读理解}")


# 卷子题目关系表
class Exercise4Paper(db.Model):
    __tablename__ = "exercise4paper"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paper_id = db.Column(db.Integer, comment="卷子id")
    exercise_id = db.Column(db.Integer, comment="题目id")


# 课程题目关系表
class Exercise4Course(db.Model):
    __tablename__ = "exercise4course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, comment="课程id")
    exercise_id = db.Column(db.Integer, comment="题目id")


# 卷子课程关系表
class Paper4Course(db.Model):
    __tablename__ = "paper4course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paper_id = db.Column(db.Integer, comment="卷子id")
    course_id = db.Column(db.Integer, comment="课程id")



# 收藏考题

# 考题分类

# 卷子和学生关联
    # 考了多少分
    # 考完状态


#
