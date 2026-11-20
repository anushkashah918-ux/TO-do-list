import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My To-Do List")
root.geometry("500x550")
root.configure(bg="#f0f4f8")
3
tasks = []

title = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 24, "bold"),
    bg="#f0f4f8",
    fg="#243b53"
)
title.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

task_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=40,
    height=15,
    selectbackground="#627d98"
)
task_list.pack(pady=15)


def add_task():
    task = entry.get().strip()

    if task:
        task_list.insert(tk.END, "☐ " + task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showwarning("Warning", "Select a task first!")


def complete_task():
    selected = task_list.curselection()

    if selected:
        index = selected[0]
        task = task_list.get(index)

        if task.startswith("☐"):
            task_list.delete(index)
            task_list.insert(index, "✓" + task[1:])
        else:
            task_list.delete(index)
            task_list.insert(index, "☐" + task[1:])
    else:
        messagebox.showwarning("Warning", "Select a task first!")


tk.Button(
    root, text="Add Task", command=add_task,
    bg="#2f80ed", fg="white", width=20
).pack(pady=5)

tk.Button(
    root, text="Complete / Undo", command=complete_task,
    bg="#27ae60", fg="white", width=20
).pack(pady=5)

tk.Button(
    root, text="Delete Task", command=delete_task,
    bg="#eb5757", fg="white", width=20
).pack(pady=5)

root.mainloop()