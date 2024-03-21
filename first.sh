#!/bin/sh

export PYTHONPATH=.
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name first \
    --exporter_otlp_traces_endpoint 0.0.0.0:4317 \
    --exporter_otlp_logs_endpoint 0.0.0.0:4317 \
    --exporter_otlp_metrics_endpoint 0.0.0.0:4317 \
    python first/service.py