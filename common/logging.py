import os
import logging

from pythonjsonlogger.json import JsonFormatter
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs.export import ConsoleLogExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor, SimpleLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from pythonjsonlogger.json import JsonFormatter
from flask import Flask



def init_logger():
    endpoint = "localhost:4317"
    
    logger_provider = LoggerProvider(
        resource=Resource.create(
            {
                "service.name": "train-the-telemetry",
                "service.instance.id": os.uname().nodename,
            }
        ),
    )

    set_logger_provider(logger_provider)

    otlp_exporter = OTLPLogExporter(endpoint=endpoint, insecure=True)
    # logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_exporter))
    logger_provider.add_log_record_processor(SimpleLogRecordProcessor(otlp_exporter))
    
    # console_exporter = ConsoleLogExporter()
    # logger_provider.add_log_record_processor(BatchLogRecordProcessor(console_exporter))

    formatter = JsonFormatter()
    handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
    handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
    )
