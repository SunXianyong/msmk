import time
from flask import render_template
from flask_smorest import Blueprint
from flask_socketio import SocketIO, emit

name_space = '/dcenter'

robot_bp = Blueprint("robot", __name__, url_prefix="/robot")
socketio = SocketIO()


@robot_bp.route('/')
def index():
    return render_template('index.html')


@robot_bp.route('/push')
def push_once():
    event_name = 'dcenter'
    broadcasted_data = {'data': "数据传输成功"}
    for i in range(5):
        time.sleep(i)
        socketio.emit(event_name, broadcasted_data, broadcast=False, namespace=name_space)
    return 'done!'


@socketio.on('connect', namespace=name_space)
def connected_msg():
    print('client connected.')


@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')


@socketio.on('my_event', namespace=name_space)
def mtest_message(message):
    emit('my_response',
         {'data': message['data'], 'count': 1})

