import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Initialize tasks list
        self.tasks = []

        # Create GUI elements
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=60, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Populate initial tasks
        self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_index] = updated_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
