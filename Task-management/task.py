from datetime import datetime

# Import validation functions
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return False

    if not validate_task_description(description):
        return False

    if not validate_due_date(due_date):
        return False

    task = {
        "title": "Groceries",
        "description": "Shop at Market Basket for food",
        "due_date": "2024-06-20",
        "completed": True}
    

    tasks.append(task)
    print("Task added successfully!")
    return True


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        return False

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    return pending_tasks


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = 0

        for task in tasks:
            if task["completed"]:
                completed += 1

        progress = (completed / len(tasks)) * 100

    return progress