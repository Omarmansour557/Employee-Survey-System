from time import sleep
from core.celery import celery

@celery.task
def notify_employees(message):
    print('Sending Surveys....')
    print(message)
    sleep(10)
    print('Surveys were successfully launched!')