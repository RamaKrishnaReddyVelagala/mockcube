from celery import Celery, shared_task
import time

# Create a Celery instance
celery = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')

@shared_task(name='celery_tasks.tasks.some_long_task')
def some_long_task():
    print("Started long task")
    time.sleep(10)
    print("Task completed")
    return "Completed"

