FROM ubuntu:latest
RUN apt-get update
RUN apt install -y python3-pip
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt