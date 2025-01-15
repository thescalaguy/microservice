import os
import logging
from pythonjsonlogger.json import JsonFormatter

from common import create_counter, increment_counter, fibo
from first.blueprint import api
from first.service.second import make_request
import time
import random

from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs.export import ConsoleLogExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from pythonjsonlogger.json import JsonFormatter


logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "train-the-telemetry",
            "service.instance.id": os.uname().nodename,
        }
    ),
)

set_logger_provider(logger_provider)

otlp_exporter = OTLPLogExporter(endpoint="http://localhost:4317", insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_exporter))

# console_exporter = ConsoleLogExporter()
# logger_provider.add_log_record_processor(BatchLogRecordProcessor(console_exporter))

formatter = JsonFormatter()
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

logger = logging.getLogger()

_counter = create_counter(
    name="first.request.count",
    unit="1",
    description="Counts the number of requests received by the service"
)


@api.post("/")
def post() -> dict:
    logger.info("Received a request")
    time.sleep(random.random())
    increment_counter(counter=_counter)
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
