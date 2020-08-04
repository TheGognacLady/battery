FROM python:3.7
WORKDIR /server

COPY . /server/
RUN ls -la /server/*

COPY requirements.txt /server/
RUN pip install -r requirements.txt


CMD python main.py --host 0.0.0.0
