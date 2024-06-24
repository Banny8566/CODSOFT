import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced To-Do List")
        self.root.geometry("500x500")

        # Frame for the task entry and buttons
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.top_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_button = tk.Button(self.top_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        self.load_tasks_button = tk.Button(self.top_frame, text="Load Tasks", command=self.load_tasks)
        self.load_tasks_button.pack(side=tk.LEFT)

        self.save_tasks_button = tk.Button(self.top_frame, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_button.pack(side=tk.LEFT)

        # Frame for the task list and scroll bar
        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.middle_frame, orient=tk.VERTICAL)
        self.task_listbox = tk.Listbox(self.middle_frame, width=60, height=20, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.pack(side=tk.LEFT)

        # Frame for the action buttons
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(pady=10)

        self.mark_complete_button = tk.Button(self.bottom_frame, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.pack(side=tk.LEFT, padx=5)

        self.mark_incomplete_button = tk.Button(self.bottom_frame, text="Mark Incomplete", command=self.mark_incomplete)
        self.mark_incomplete_button.pack(side=tk.LEFT, padx=5)

        self.delete_task_button = tk.Button(self.bottom_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_complete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"[Completed] {task}")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def mark_incomplete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            if task.startswith("[Completed]"):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(tk.END, task.replace("[Completed] ", ""))
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as incomplete.")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                tasks = self.task_listbox.get(0, tk.END)
                for task in tasks:
                    file.write(f"{task}\n")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path and os.path.exists(file_path):
            self.task_listbox.delete(0, tk.END)
            with open(file_path, 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.task_listbox.insert(tk.END, task.strip())

# Create the main application window
root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
