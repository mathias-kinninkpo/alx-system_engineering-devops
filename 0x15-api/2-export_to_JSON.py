#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: {
        "USER_ID": [
            {
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"
            },
            {
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"
            },
            ...
        ]
    }
    File name must be: USER_ID.json
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
        if param:
            _route = URL + ressource + "/?" + f"{param[0]}={param[1]}"
            request = urllib.request.Request(_route, method="GET")
            response = urllib.request.urlopen(request)

            return loads(response.read())
        return {}

    args = sys.argv
    if len(args) > 1:
        try:
            userId = int(args[1])
            user = get_request("users", ("id", userId))
            todos = get_request("todos", ("userId", userId))
            data = []
            USER_ID = userId
            USERNAME = user[0].get("username")
            for task in todos:
                TASK_COMPLETED_STATUS = task.get("completed")
                TASK_TITLE = task.get("title")
                row = {
                    "task": f"{TASK_TITLE}",
                    "completed": TASK_COMPLETED_STATUS,
                    "username": f"{USERNAME}",
                }
                data.append(row)

            with open(
                f"{USER_ID}.json", mode="w", newline="", encoding="utf-8"
            ) as jsonfile:
                dump({f"{USER_ID}": data}, jsonfile)
            jsonfile.close()

        except ValueError:
            pass
