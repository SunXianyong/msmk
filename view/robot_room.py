from flask import render_template
from flask_smorest import Blueprint
from flask_socketio import SocketIO

name_space = '/dcenter'

robot_bp = Blueprint("robot", __name__, url_prefix="/robot")
socketio = SocketIO()


@robot_bp.route('/')
def test_sconnect():
    return render_template("index_room.html")


@socketio.on('connect', namespace="/dcenter")
def test_connect():
    print("客户端已连接")


@socketio.on('disconnect', namespace="/dcenter")
def test_disconnect():
    print('Client disconnected')


@socketio.on('message', namespace="/dcenter")
def handle_message(data):
    print("dce")
    room_id = data.get("room")
    socketio.emit(room_id, {'data': {"room": None, "msg": data.get("message")}}, namespace="/dcenter")


@socketio.on('message')
def handle_message(data):
    print("robot")
    room_id = data.get("room")
    socketio.emit(room_id, {'data': {"room": None, "msg": data.get("message")}}, namespace="/dcenter")


@socketio.event
def handle_message(data):
    print("robot")
    room_id = data.get("room")
    socketio.emit(room_id, {'data': {"room": None, "msg": data.get("message")}}, namespace="/dcenter")
