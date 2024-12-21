import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Listbox to display tasks
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=20)

        # Entry field to add tasks
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Buttons for adding and removing tasks
        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", width=20, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.mark_button = tk.Button(root, text="Mark as Done", width=20, command=self.mark_done)
        self.mark_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove!")

    def mark_done(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            task = f"{task} (Done)"
            self.tasks[selected_task_index] = task
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done!")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
