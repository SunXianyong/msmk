from models.model import Teacher, Course, Exercise

Teacher_info = [Teacher.name, Teacher.photo, Teacher.id, Teacher.info]
Exercise_info = [Exercise.big_title, Exercise.small_title, Exercise.id]
COURSE_INFO = [Course.name, Course.photo, Course.id, Course.info, Course.buy_num,
               Course.money, Course.total, Course.total_time]

RESPONSE_CODE = {
    200: "操作成功",
    405: "登录失败",
    444: "余额不足",
}

Exercise_xuanze = 1
EXERCISE_TIANKONG = 2