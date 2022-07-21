from create_app import create_app
from instance.config import DefaultConfig

app = create_app(DefaultConfig)

if __name__ == '__main__':
    app.run()
