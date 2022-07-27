from create_app import create_app
from instance.config import DefaultConfig

socketio, app = create_app(DefaultConfig)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    # app.run(debug=True)
