from .course import courses_bp
# from .robot_day2 import robot_bp, socketio
from .robot_room import robot_bp, socketio
from .student import students_bp
from .teachers import teachers_bp
from .exercise import exercise_bp
from .paper import paper_bp

__all__ = ["teachers_bp", "students_bp", "courses_bp", "robot_bp", "socketio", "exercise_bp","paper_bp"]
