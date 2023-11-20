from flask import Flask, jsonify
from celery.result import AsyncResult
from celery_tasks.tasks import some_long_task, celery # Import the Celery task function

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask - Test Ping"

@app.route('/longtask')
def long_task():
    # import time
    # time.sleep(10)
    # return "slept for 10 sec"

    # Trigger the Celery task
    task = some_long_task.delay()  
    return f"Started long task with ID: {task.id}"
    
@app.route('/task_status/<task_id>')
def task_status(task_id):
    # Check the status of the Celery task
    task = AsyncResult(task_id, app=celery)
    
    if task.successful():
        return jsonify({"status": "Task completed", "result": task.result})
    elif task.failed():
        return jsonify({"status": "Task failed", "error": str(task.result)})
    else:
        return jsonify({"status": "Task is still running"})

if __name__ == '__main__':
    app.run(debug=True)
