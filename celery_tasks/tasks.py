from celery import Celery
from time import sleep

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

app.config_from_object('celeryconfig')
# The first argument to Celery is the name of the current module.
# The second argument is the broker keyword argument, specifying the URL of the message broker you want to use

@app.task
def add(x, y):
    # sleep(5)
    return x + y

