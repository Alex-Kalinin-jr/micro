FROM python:3.11-slim

COPY requirements.txt /app/
EXPOSE 8000

RUN apt update && apt upgrade -y
RUN apt install make -y
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r /app/requirements.txt
