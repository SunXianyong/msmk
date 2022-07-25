import time

from flask import render_template,request
from flask_socketio import SocketIO, emit

from create_app import create_app
from instance.config import DefaultConfig

app = create_app(DefaultConfig)
socketio = SocketIO(app)


@app.route('/')
def test_sconnect():
    return render_template("index.html")

@app.route('/xiaoming')
def connect():
    msg = request.args.get("msg")
    socketio.emit('connect_daming', {'data': msg}, namespace="/dcenter")
    return "ok"


@socketio.on('connect', namespace="/dcenter")
def test_connect():
    print("创建连接")
    emit('connect_daming', {'data': f'你好'}, namespace="/dcenter")


@socketio.on('disconnect', namespace="/dcenter")
def test_disconnect():
    print('Client disconnected')


@socketio.on('message', namespace="/dcenter")
def handle_message(data):
    print('received message: ' + data)


if __name__ == '__main__':
    socketio.run(app, debug=True)
    # app.run(debug=True)
