FROM python:3.11-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
