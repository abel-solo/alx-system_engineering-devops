#!/usr/bin/python3
'''script to export data in the JSON format'''
import json
import requests
import sys

if __name__ == '__main__':
    user_sys = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    usr = requests.get(url + "users/{}".format(user_sys)).json()
    username = usr.get("username")
    to_do = requests.get(url+'todos',params={'user_id':user_sys}).json()

    with open("{}.json".format(user_sys), "w") as jsonfile:
        json.dump({user_sys: [{"task": e.get("title"),
                              "completed": e.get("completed"),
                              "username": username} for e in to_do]},
                  jsonfile)
