import os
import logging

from common import create_counter, increment_counter, fibo
from first.blueprint import api
from first.service.second import make_request
import time
import random

from pythonjsonlogger.json import JsonFormatter
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs.export import ConsoleLogExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from pythonjsonlogger.json import JsonFormatter


_counter = create_counter(
    name="first.request.count",
    unit="1",
    description="Counts the number of requests received by the service"
)


@api.post("/")
def post() -> dict:
    logging.getLogger().info("Received a request")
    time.sleep(random.random())
    # increment_counter(counter=_counter)
    return make_request()  # Makes a call to second


@api.get("/<int:n>")
def get(n: int) -> dict:

    def _one(n: int):
        return _two(n=n)

    def _two(n: int):
        return _fibo(n=n)

    def _fibo(n: int):
        for i in range(1, n - 1):
            fibo(i)
        return fibo(n=n)

    return {"fibonacci": _one(n=n)}
