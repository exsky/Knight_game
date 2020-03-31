FROM python:latest
MAINTAINER exsky alex19911118@gmail.com
RUN mkdir -p /home/knights
WORKDIR /home/knights
CMD python game.py
