#!/bin/sh

export PYTHONPATH=.
export SERVICE=second
export PORT=9001
export OTEL_EXPORTER_OTLP_INSECURE=true

opentelemetry-instrument \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --logs_exporter otlp \
    --service_name second \
    --exporter_otlp_traces_endpoint 0.0.0.0:4317 \
    --exporter_otlp_logs_endpoint 0.0.0.0:4317 \
    --exporter_otlp_metrics_endpoint 0.0.0.0:4317 \
    python second/service.py
