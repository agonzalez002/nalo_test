FROM python:3.8-slim-buster

COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY ./apt_requirements.txt /tmp
RUN apt-get update -y \
 && apt-get upgrade -y \
 && cat /tmp/apt_requirements.txt | xargs apt-get install -y

COPY ./app /app
WORKDIR /app
