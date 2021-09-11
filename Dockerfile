FROM python:3.9-slim-buster
RUN pip install pipenv
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
RUN mkdir /app/celery_app
COPY . /app
COPY . /app/celery_app
WORKDIR /app
COPY requirements.txt ./
EXPOSE 8000
EXPOSE 15672
EXPOSE 5672
EXPOSE 5432
EXPOSE 80
RUN pip install -r requirements.txt
VOLUME /app
