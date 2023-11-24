from celery import Celery
from time import sleep

celery_app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

celery_app.config_from_object('celery_tasks.celeryconfig')
# The first argument to Celery is the name of the current module.
# The second argument is the broker keyword argument, specifying the URL of the message broker you want to use

@celery_app.task
def add(x, y):
    # sleep(20)
    return int(x) + int(y)

