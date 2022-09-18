FROM python:3.9-alpine

EXPOSE 8000


WORKDIR /app


COPY . .
RUN apk add build-base
RUN pip install -r requirements.txt

CMD celery -A core worker --loglevel=info --detach; python manage.py runserver 0.0.0.0:8000