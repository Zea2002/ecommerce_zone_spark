FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y gcc libpq-dev


RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

