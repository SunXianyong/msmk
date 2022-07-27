from flask_login import LoginManager

from models.model import db, Student

login = LoginManager()
login.login_view = "login_stu"


# @login.request_loader
# def check_login(req):
#     return db.session.query(Student).get(req.args.get("id"))


@login.user_loader
def check_login(id):
    return db.session.query(Student).get(id)
