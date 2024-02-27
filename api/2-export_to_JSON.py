""" Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json """

import json
import requests
import sys


def get_user_data(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(url, user_id)
    response = requests.get(user_url)
    return response.json()


def get_user_tasks(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    todos_url = "{}todos?userId={}".format(url, user_id)
    response = requests.get(todos_url)
    return response.json()


def export_to_json(user_id, user_data, tasks):
    l_task = []
    for task in tasks:
        dict_task = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_data.get("username"),
        }
        l_task.append(dict_task)

    d_task = {str(user_id): l_task}
    filename = "{}.json".format(user_id)

    with open(filename, "w") as json_file:
        json.dump(d_task, json_file, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    user_data = get_user_data(user_id)
    user_tasks = get_user_tasks(user_id)

    export_to_json(user_id, user_data, user_tasks)