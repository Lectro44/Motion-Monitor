FROM python:3.12.2-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /deploy
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000