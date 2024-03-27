#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the JSON format.

Requirements:

    Records all tasks from all employees
    Format must be:
    {
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            {"username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
            },
            ...
        ],
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            {"username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
            },
            ...
        ]
    }
        File name must be: todo_all_employees.json
"""
from json import loads, dump
import sys
import urllib.request


URL = "https://jsonplaceholder.typicode.com/"


if __name__ == "__main__":

    def get_request(ressource, param=None):
        """
        Make request
        Attrs:
            ressource (str): a ressource
            param (tuple): matching param
        Return:
            response: dict
        """
        _route = URL + ressource
        if param:
            _route += "/?" + f"{param[0]}={param[1]}"
        request = urllib.request.Request(_route, method="GET")
        response = urllib.request.urlopen(request)

        return loads(response.read())

    args = sys.argv
    all_data = {}
    try:
        users = get_request("users")
        for user in users:
            todos = get_request("todos", ("userId", user.get("id")))
            data = []
            USER_ID = user.get("id")
            USERNAME = user.get("username")
            for task in todos:
                TASK_COMPLETED_STATUS = task.get("completed")
                TASK_TITLE = task.get("title")
                row = {
                    "username": f"{USERNAME}",
                    "task": f"{TASK_TITLE}",
                    "completed": TASK_COMPLETED_STATUS,
                }
                data.append(row)

            all_data[f"{USER_ID}"] = data

        with open(
            "todo_all_employees.json",
            mode="w",
            newline="",
            encoding="utf-8"
        ) as jsonfile:
            dump(all_data, jsonfile)
        jsonfile.close()

    except ValueError:
        print("KO")
