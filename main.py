import argparse
import json

def add_task(args):
 tasks_path = '/Users/iexists/task tracker cli/tasks.json'

 with open(tasks_path,"r") as f:
    tasks = json.load(f)


    new_task = {
        "id": max(task["id"] for task in tasks) + 1 if tasks else 1,
        "description": args.description,
        "status": 1,
        "createdat": "",
        "updatedat": ""
    }
    tasks.append(new_task)
    with open('/Users/iexists/task tracker cli/tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)
    print(f"Task added: {new_task}")


def main():
    parser = argparse.ArgumentParser(prog="task-cli")   
    sub = parser.add_subparsers(dest="command", required=True)
    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("description")
    p_add.set_defaults(func=add_task)
    args = parser.parse_args()
    args.func(args)



