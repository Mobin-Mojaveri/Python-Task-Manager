
from storage import load_tasks, save_tasks
from datetime import datetime


def add_task(title):
    if not title.strip():
        print("Task title cannot be empty.")
        return

    tasks = load_tasks()

    task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": title.strip(),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def show_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(f"""
ID: {task['id']}
Title: {task['title']}
Status: {status}
Created: {task['created_at']}
-----------------------------
""")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task not found.")
        return

    save_tasks(new_tasks)
    print("Task deleted successfully!")


def update_task(task_id, new_title):
    if not new_title.strip():
        print("New title cannot be empty.")
        return

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title.strip()
            save_tasks(tasks)
            print("Task updated successfully!")
            return

    print("Task not found.")


def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task completed successfully!")
            return

    print("Task not found.")


def search_tasks(keyword):
    tasks = load_tasks()

    results = [
        task for task in tasks
        if keyword.lower() in task["title"].lower()
    ]

    if not results:
        print("No matching tasks found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for task in results:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']} | {task['title']} | {status}")
