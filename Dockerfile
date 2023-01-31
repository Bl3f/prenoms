FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY main.py main.py
COPY prenoms.v1.joblib prenoms.v1.joblib

ENTRYPOINT ["/usr/local/bin/flask", "--app", "main", "run"]