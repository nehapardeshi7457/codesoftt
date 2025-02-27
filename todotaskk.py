import tkinter as tk
from tkinter import messagebox
import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task."""
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    """Delete the selected task."""
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        del tasks[selected_index]
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_completed():
    """Mark the selected task as completed."""
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        save_tasks(tasks)
        update_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed.")

def update_list():
    """Update the task list display."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["completed"] else "✖"
        task_listbox.insert(tk.END, f"{task['task']} [{status}]")

# Load tasks from file
tasks = load_tasks()

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

complete_button = tk.Button(btn_frame, text="Mark Completed", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(btn_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

update_list()  # Load existing tasks into the list

root.mainloop()