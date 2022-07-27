# import random
#
# from flask import render_template, request
# from flask_smorest import Blueprint
# from flask_socketio import SocketIO
#
# name_space = '/dcenter'
#
# robot_bp = Blueprint("robot", __name__, url_prefix="/robot")
# socketio = SocketIO()
#
#
# @robot_bp.route('/')
# def test_sconnect():
#     return render_template("index.html")
#
#
# @socketio.on('connect', namespace="/dcenter")
# def test_connect():
#     student_id = int(request.cookies.get("tes")) + random.randint(0, 10)
#     print(student_id)
#
#     if request.args.get("type", None):
#         socketio.emit(f'dcenter', {'data': {"room": student_id, "msg": student_id}}, namespace="/dcenter")
#         socketio.emit(f'dcenter', {'user': student_id, "room": student_id}, namespace="/dcenter")
#
#     print(f"我在新房间 dcenter{student_id}")
#     socketio.emit(f'dcenter', {'data': {"room": None, "msg": student_id}}, namespace="/dcenter")
#
#
# @socketio.on('disconnect', namespace="/dcenter")
# def test_disconnect():
#     print('Client disconnected')
#
#
# @socketio.on('message', namespace="/dcenter")
# def handle_message(data):
#     room_id = data.get("room")
#     socketio.emit(room_id, {'data': {"room": None, "msg": data.get("message")}}, namespace="/dcenter")
