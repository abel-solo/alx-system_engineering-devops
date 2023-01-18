#!/usr/bin/python3
"""Script to export data in the CSV format"""
import sys
import requests
import csv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usr = requests.get(url + '/users/' + argv[1]).json()['username']
    todos = requests.get(url + '/todos?userId=' + argv[1]).json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], usr, todo['completed'], todo['title']])
