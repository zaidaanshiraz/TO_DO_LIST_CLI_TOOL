# TO_DO_LIST_CLI_TOOL

This is a simple command-line To-Do List application written in Python. It allows users to manage their tasks effectively by adding, viewing, completing, and deleting tasks, all while saving the task list to a JSON file for persistence.

## Features

- **Add Tasks**: Add new tasks to your to-do list.
- **View Tasks**: Display all tasks along with their completion status.
- **Mark Tasks as Completed**: Mark specific tasks as completed.
- **Delete Tasks**: Remove tasks from the list.
- **Persistent Storage**: Tasks are saved in a `tasks.json` file to maintain data between sessions.

## How It Works

1. The application stores tasks in a JSON file (`tasks.json`).
2. Tasks are represented as dictionaries with two fields:
   - `task`: The description of the task.
   - `completed`: A boolean indicating whether the task is completed.
3. The program provides a menu-driven interface for user interaction.

## File Structure

- `tasks.json`: A JSON file where tasks are stored persistently.
- The script includes the following functions:
  - **`load_tasks()`**: Loads tasks from the JSON file.
  - **`save_tasks(tasks)`**: Saves the tasks to the JSON file.
  - **`add_task(tasks, task)`**: Adds a new task to the task list.
  - **`view_tasks(tasks)`**: Displays the list of tasks and their statuses.
  - **`mark_task_completed(tasks, task_number)`**: Marks a specific task as completed.
  - **`delete_task(tasks, task_number)`**: Deletes a task from the list.

## Usage

1. Run the script using Python:
   ```bash
   python to_do_list.py
   ```
2. Use the menu to interact with the application:
   - **Option 1**: Add a new task.
   - **Option 2**: View all tasks.
   - **Option 3**: Mark a task as completed.
   - **Option 4**: Delete a task.
   - **Option 5**: Exit the application.

## Example Session

```
To-Do List Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
Choose an option: 1
Enter the task: Buy groceries
Task added: Buy groceries

To-Do List Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
Choose an option: 2
1. Buy groceries [✗]

To-Do List Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
Choose an option: 3
Enter the task number to mark as completed: 1
Task 1 marked as completed.

To-Do List Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
Choose an option: 5
Exiting...
```

## Requirements

- Python 3.x

## Customization

You can modify the `tasks.json` file or enhance the script to include additional features like:
- Setting due dates for tasks.
- Categorizing tasks.
- Filtering tasks based on completion status.

## License

This project is free to use and modify. It serves as a starting point for building more advanced task management systems.
