from flask import Flask
from first.blueprint import api


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api)
    return app
