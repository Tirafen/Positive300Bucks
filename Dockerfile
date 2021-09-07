FROM python:3.9-slim-buster
EXPOSE ${BACKEND_PORT}

ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/app

WORKDIR ${APP_HOME}

COPY app app
COPY requirements.txt ./

RUN pip install --no-cache-dir -U pip
RUN pip install -v --no-cache-dir -U  -r requirements.txt --src /app

