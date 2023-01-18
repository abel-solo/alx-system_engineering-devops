#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usr = requests.get(url + '/users/' + sys.argv[1]).json()['username']
    todos = requests.get(url + '/todos?userId=' + sys.argv[1]).json()
    with open('{}.csv'.format(sys.argv[1]), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([sys.argv[1], usr, todo['completed'], todo['title']])
