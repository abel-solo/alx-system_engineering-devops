#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about TODO list progress"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_id = requests.get(url + '/users/' + argv[1]).json()
    to_do = requests.get(url + '/todos?userId=' + argv[1]).json()
    completed = [todo['title'] for todo in to_do if todo['completed']]

    print('Employee {} is done with tasks({}/{}):'
          .format(user_id['name'], len(completed), len(to_do)))

    [print('\t {}'.format(title)) for title in completed]
