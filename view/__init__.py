from .course import courses_bp
from .robot import robot_bp
from .robot import socketio
from .student import students_bp
from .teachers import teachers_bp

__all__ = ["teachers_bp", "students_bp", "courses_bp", "robot_bp", "socketio"]
