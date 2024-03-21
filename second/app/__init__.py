from flask import Flask
from second.blueprint import api


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api)
    return app
