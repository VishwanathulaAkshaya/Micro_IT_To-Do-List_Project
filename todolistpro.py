import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        for task in tasks:
            listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="#f6f5f3")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=20)

listbox_tasks = tk.Listbox(frame_tasks, width=30, height=10, font=("Arial", 14), selectbackground="#a3c9a8")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=24, font=("Arial", 14))
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", width=10, font=("Arial", 12, "bold"), bg="#4a7c59", fg="white", command=add_task)
button_add_task.pack(pady=2)

button_delete_task = tk.Button(root, text="Delete Task", width=10, font=("Arial", 12, "bold"), bg="#bc4b51", fg="white", command=delete_task)
button_delete_task.pack(pady=2)

button_save_tasks = tk.Button(root, text="Save Tasks", width=10, font=("Arial", 12, "bold"), bg="#425c77", fg="white", command=save_tasks)
button_save_tasks.pack(pady=2)

load_tasks()

root.mainloop()
