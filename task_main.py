import sys
import json
import os
from datetime import datetime

# File name where tasks will be stored
TASKS_FILE = "tasks.json"


# ---------------- Helper Functions ---------------- #


def load_tasks():
    """Load tasks from the JSON file, or return empty list if file doesn't exist"""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save the tasks list into the JSON file"""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def get_new_id(tasks):
    """Generate a unique task ID"""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def get_current_time():
    """Return current timestamp as string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------- Task Operations ---------------- #


def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": get_new_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": get_current_time(),
        "updatedAt": get_current_time()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f" Task added successfully (ID: {new_task['id']})")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = get_current_time()
            save_tasks(tasks)
            print(f" Task {task_id} updated successfully")
            return
    print(f" Task with ID {task_id} not found")


def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f" Task with ID {task_id} not found")
    else:
        save_tasks(updated_tasks)
        print(f" Task {task_id} deleted successfully")


def change_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = get_current_time()
            save_tasks(tasks)
            print(f" Task {task_id} marked as {new_status}")
            return
    print(f" Task with ID {task_id} not found")


def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print(" No tasks found")
        return

    for task in tasks:
        if filter_status is None or task["status"] == filter_status:
            print(f"[{task['id']}] {task['description']} "
                  f"(Status: {task['status']}, Created: {task['createdAt']}, Updated: {task['updatedAt']})")



# ---------------- Main CLI Handler ---------------- #


def main():
    if len(sys.argv) < 2:
        print(" No command provided. Try: add, update, delete, mark-done, mark-in-progress, list")
        return


    command = sys.argv[1]


    if command == "add":
        if len(sys.argv) < 3:
            print(" Please provide a task description")
        else:
            description = " ".join(sys.argv[2:])
            add_task(description)


    elif command == "update":
        if len(sys.argv) < 4:
            print(" Usage: python task_cli.py update <id> <new description>")
        else:
            try:
                task_id = int(sys.argv[2])
                new_description = " ".join(sys.argv[3:])
                update_task(task_id, new_description)
            except ValueError:
                print(" Task ID must be a number")


    elif command == "delete":
        if len(sys.argv) < 3:
            print(" Usage: python task_cli.py delete <id>")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                print(" Task ID must be a number")


    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print(" Usage: python task_cli.py mark-in-progress <id>")
        else:
            try:
                task_id = int(sys.argv[2])
                change_status(task_id, "in-progress")
            except ValueError:
                print(" Task ID must be a number")


    elif command == "mark-done":
        if len(sys.argv) < 3:
            print(" Usage: python task_cli.py mark-done <id>")
        else:
            try:
                task_id = int(sys.argv[2])
                change_status(task_id, "done")
            except ValueError:
                print("❌ Task ID must be a number")


    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        else:
            status = sys.argv[2]
            if status in ["todo", "in-progress", "done"]:
                list_tasks(status)
            else:
                print(" Invalid status. Use: to do, in-progress, done")

    else:
        print(f" Unknown command: {command}")


if __name__ == "__main__":
    main()
