FROM python:3.10

WORKDIR /app
COPY api/ /app/

RUN pip install flask flask-cors requests redis

CMD ["python", "app.py"]
