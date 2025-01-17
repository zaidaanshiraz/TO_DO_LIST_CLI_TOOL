import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def mark_task_completed(tasks, task_number):
    """Mark a task as completed."""
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    """Delete a task from the list."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(tasks, task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
