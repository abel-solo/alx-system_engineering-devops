#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests
import sys


if __name__ == '__main__':
    usr_sys = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    usr = requests.get(url + '/users/' + usr_sys).json()['username']
    todos = requests.get(url + '/todos?userId=' + usr_sys).json()
    with open('{}.csv'.format(usr_sys), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([usr_sys, usr, todo['completed'], todo['title']])
