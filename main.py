from flask import Flask, jsonify

from AddTaskInteractor import AddTaskInteractor
from DeleteTaskInteractor import DeleteTaskInteractor
from GetTaskInteractor import GetTaskInteractor
from InMemoryStorage import InMemoryStorage

app = Flask(__name__)

taskGateway = InMemoryStorage()
addTaskInteractor = AddTaskInteractor(taskGateway)
getTaskInteractor = GetTaskInteractor(taskGateway)
deleteTaskInteractor = DeleteTaskInteractor(taskGateway)


@app.route('/tasks/add/<summary>', methods=['GET'])
def task_add(summary):
    task_id = addTaskInteractor.add_task(summary)
    return jsonify({'id': task_id}), 200


@app.route('/tasks/delete/<int:_id>', methods=['DELETE'])
def task_delete(_id):
    deleteTaskInteractor.delete_task(_id)
    return 'ok', 200


@app.route('/tasks', methods=['GET'])
def tasks():
    tasks_list = getTaskInteractor.get_tasks()
    tasks_json = []
    for t in tasks_list:
        tasks_json.append({'id': t.id, 'summary': t.summary})
    return jsonify(tasks_json), 200


app.run(port=5000)
