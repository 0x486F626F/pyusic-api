FROM ubuntu:latest

ENV LANG C.UTF-8

RUN apt update
RUN apt install -y python3 python3-pip git

ADD . pyusic-api
RUN pip3 install --upgrade pip
RUN pip3 install -r pyusic-api/requirements.txt

EXPOSE 5000
WORKDIR /pyusic-api
CMD python3 run_server.py
