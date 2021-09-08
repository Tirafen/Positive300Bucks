FROM python:3.9-slim-buster
RUN pip install pipenv

ENV PYTHONUNBUFFERED 1
RUN mkdir ./celery_app
COPY ./celery_app /celery_app
WORKDIR ./
COPY requirements.txt ./
EXPOSE 8000
RUN pip install --no-cache-dir -U pip
RUN pip install -v --no-cache-dir -U  -r requirements.txt --src ./

