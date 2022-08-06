from __future__ import absolute_import,unicode_literals
from .email import send_email

from celery import shared_task
# from celery.decorators import task
from celery.utils.log import get_task_logger
from djangoProject.celery import app

@shared_task
def task_one(x,y):
    res = f'Result is {x*y}'
    return res

logger = get_task_logger(__name__)

@app.task(name='send_email_task')
def send_email_task(name,email,content):
    logger.info("sent successfully")
    return send_email(name,email,content)

