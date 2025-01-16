from flask import Flask
import logging
from common.zookeeper import init_zookeeper_and_register
from first.blueprint import api
from common import init_logger
from pythonjsonlogger.json import JsonFormatter
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs.export import ConsoleLogExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from pythonjsonlogger.json import JsonFormatter
import os

def create_app() -> Flask:
    init_logger()
    
    app = Flask(__name__)
    app.register_blueprint(api)

    # -- Initialize Zookeeper and register the service.
    init_zookeeper_and_register()
    
    return app
