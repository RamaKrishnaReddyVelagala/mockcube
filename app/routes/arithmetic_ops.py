from flask import request, jsonify
from celery_tasks.tasks import add  # Import the Celery task
from app import app as flask_app
from celery_tasks.tasks import celery_app
from celery.result import AsyncResult


@flask_app.route('/add', methods=['GET'])
def add_numbers():
    # Extract x and y from the POST request
    args = request.args
    x = args.get('x')  # Extracts the value of 'x' from the JSON
    y = args.get('y')  # Extracts the value of 'y' from the JSON
    print(f"x_value:{x}, y_value:{y}")
    result = add.delay(x,y)
    # print(f"result_id: {result.id}")
    # print(f"type: {type(result.id)}")
    return f"result_id: {result.id}"

@flask_app.route('/add_result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = AsyncResult(task_id, app=celery_app)
    if result.state == 'PENDING':
        return jsonify({'state': result.state, 'status': 'Task is still processing'})
    elif result.state != 'FAILURE':
        return jsonify({'state': result.state, 'result': result.result})
    else:
        return jsonify({'state': result.state, 'status': 'Task failed', 'error': str(result.info)})