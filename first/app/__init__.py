from flask import Flask

from common.zookeeper import init_zookeeper_and_register
from first.blueprint import api


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api)

    # -- Initialize Zookeeper and register the service.
    init_zookeeper_and_register()

    return app
