#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

    Requirements:

    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO list
    progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with tasks
        (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
            completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
from json import loads
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
            EMPLOYEE_NAME = user[0].get("name").strip()
            NUMBER_OF_DONE_TASKS = 0
            completed_tasks_title = []
            for task in todos:
                if task.get("completed"):
                    NUMBER_OF_DONE_TASKS += 1
                    completed_tasks_title.append(task.get("title").strip())
            TOTAL_NUMBER_OF_TASKS = len(todos)
            print(f"Employee {EMPLOYEE_NAME} is done with", end=" ")
            print(f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
            for task in completed_tasks_title:
                print("\t " + task)
        except ValueError:
            pass
