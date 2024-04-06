FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0