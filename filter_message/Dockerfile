# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

# Install OpenJDK-8
RUN apt-get update
RUN apt-get install -qq -y default-jre


RUN pip install -r requirements.txt
RUN pip install kafka-python



COPY . /code/
COPY start.sh ./
RUN pip install kafka-python
RUN chmod +x ./start.sh