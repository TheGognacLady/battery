FROM python:3.7
WORKDIR /server

COPY . /server/
RUN ls -la /server/*

COPY requirements.txt /server/
RUN pip install -r requirements.txt


CMD gunicorn --bind 0.0.0.0:5000 main:app
