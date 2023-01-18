#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about TODO list progress"""
import requests as req
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usr_id = req.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = req.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    completed = [title.get("title") for title in todos if
                 title.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'
           .format(usr_id.get('name'),len(completed),len(todos)))

    [print("\t {}".format(title)) for title in completed]
