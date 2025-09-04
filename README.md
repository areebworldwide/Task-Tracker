📌 README.md
# 📝 Task Tracker CLI

A simple **Command Line Interface (CLI)** application built in Python to manage daily tasks (To-Do List).  
This project is part of the **MSK Institute** hands-on learning approach and helps practice Python programming with real-world use cases.  

---

## 🚀 Features
- Add new tasks  
- Update or delete existing tasks  
- Mark tasks as **todo**, **in-progress**, or **done**  
- List all tasks or filter by status  
- Stores all tasks in a local JSON file automatically  
- Lightweight & beginner-friendly (no external libraries needed)  

---

## 📂 Task Properties
Each task includes:
- **id**: Unique identifier  
- **description**: Short task description  
- **status**: `todo`, `in-progress`, or `done`  
- **createdAt**: Date and time task was created  
- **updatedAt**: Date and time task was last updated  

Example JSON file (`tasks.json`):
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2025-09-04 12:30:00",
    "updatedAt": "2025-09-04 12:30:00"
  }
]

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli

2. Run with Python
python task_main.py add "Buy groceries"

💡 Shortcut Setup (Windows)

To avoid typing python task_main.py every time, create a task.bat file:

@echo off
python "D:\Task Tracker\task_main.py" %*


Copy task.bat to C:\Windows\System32 for global access.
Now you can run:

task add "Buy groceries"
task list
task mark-done 1

🔑 Commands
Add Task
task add "Buy groceries"

Update Task
task update 1 "Buy groceries and cook dinner"

Delete Task
task delete 1

Mark Task Status
task mark-in-progress 1
task mark-done 1

List Tasks
task list          # All tasks
task list todo     # Only pending tasks
task list done     # Only completed tasks
task list in-progress

🧑‍💻 Tech Stack

Language: Python 3

Modules Used: sys, os, json, datetime

📜 License

This project is open-source and free to use under the MIT License.

👨‍🏫 Author

Developed as part of MSK Institute practical learning.
Created by Areeb Akhtar
