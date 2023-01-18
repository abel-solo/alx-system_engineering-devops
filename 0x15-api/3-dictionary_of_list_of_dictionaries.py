#!/usr/bin/python3
'''script to export data in the JSON format'''
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": e.get("title"),
            "completed": e.get("completed")
        } for e in requests.get(url + "todos",
                         params={"userId": usr.get("id")}).json()]
            for user in user}, jsonfile)
