from flask import render_template
from flask_smorest import Blueprint
from flask_socketio import SocketIO

robot_bp = Blueprint("robot", __name__, url_prefix="/")
socketio = SocketIO()


@robot_bp.route('/robot2')
def robot_index():
    return render_template('index.html')


@socketio.on("connect", namespace="/robot_chat")
def connect():
    print("ok")


@socketio.on("disconnect", namespace="/robot_chat")
def disconnect():
    print("断开")


@socketio.on("qwer", namespace="/robot_chat")
def read_message(data):
    print(data)
    socketio.emit("asdf", "from emit", namespace="/robot_chat")
    socketio.send("from send", namespace="/robot_chat")
    print("ok")
