FROM python:3.7
WORKDIR /server

COPY . /server/
RUN ls -la /server/*

COPY requirements.txt /server/
RUN pip install -r requirements.txt


CMD gunicorn -b localhost:8000 -w 4 main:app
