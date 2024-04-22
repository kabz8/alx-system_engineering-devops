#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    users = response_users.json()
    todos = response_todos.json()

    todo_dict = {}

    for user in users:
        tasks = [{"username": user['username'],
                  "task": task['title'],
                  "completed": task['completed']}
                 for task in todos if task['userId'] == user['id']]
        todo_dict[user['id']] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_dict, json_file)
