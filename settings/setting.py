from models.model import Teacher, Course

Teacher_info = [Teacher.name, Teacher.photo, Teacher.id, Teacher.info]
COURSE_INFO = [Course.name, Course.photo, Course.id, Course.info, Course.buy_num,
               Course.money, Course.total, Course.total_time]





RESPONSE_CODE = {
    200: "操作成功",
    405: "登录失败",
    444: "余额不足",
}
