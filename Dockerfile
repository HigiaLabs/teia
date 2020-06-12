FROM python:3.7-slim

COPY . .

RUN apt-get update && apt-get install -y gcc g++ libgtk2.0-dev && \
    pip install -r requirements.txt

USER root

CMD exec gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker --workers 3 --bind 0.0.0.0:8000