FROM python:3.9
RUN apt update && apt install python-dev -y

WORKDIR /app
COPY requirements.txt /app
COPY src/. /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD sfx-py-trace app.py
