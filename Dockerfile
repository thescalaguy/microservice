FROM python:3.12-alpine
WORKDIR /opt/microservice

# -- Copy microservice
COPY . .

# -- Install packages
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
RUN opentelemetry-bootstrap -a install
