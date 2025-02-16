import logging
import os
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import SimpleLogRecordProcessor
from opentelemetry.sdk.resources import Resource


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

    # formatter = JsonFormatter()

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )

    handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
    handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
    )
