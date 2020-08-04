FROM python:3.7
WORKDIR /selen

COPY . /selen/
RUN ls -la /selen/*

COPY requirements.txt /selen/
RUN pip install -r requirements.txt


CMD python main.py
