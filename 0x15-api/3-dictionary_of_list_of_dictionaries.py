#!/usr/bin/python3
'''script to export data in the JSON format'''
import json
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + '/users/').json()
    to_do = requests.get(url + '/todos/').json()

    i, records = 0, []
    id, user, all = users[i]['id'], users[i]['username'], {}

    for todo in to_do:
        if todo['userId'] != id:
            all[id] = records
            i += 1
            id, user = users[i]['id'], users[i]['username']
            records = []
        records.append({'username': user, 'task': todo['title'],
                        'completed': todo['completed']})

    all[id] = records
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all, file)
