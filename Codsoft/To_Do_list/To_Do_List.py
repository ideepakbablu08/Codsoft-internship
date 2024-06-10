import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")
        
        self.tasks = []
        
        self.create_widgets()
        
    def create_widgets(self):
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 14), bg="#e6f2ff", fg="#333333", selectbackground="#cce6ff")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.entry_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.entry_frame.pack(fill=tk.X, padx=10)
        
        self.task_entry = tk.Entry(self.entry_frame, font=("Arial", 14))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.add_button = tk.Button(self.entry_frame, text="Add Task", font=("Arial", 14), bg="#4CAF50", fg="#ffffff", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        self.update_button = tk.Button(self.root, text="Update Task", font=("Arial", 14), bg="#FFC107", fg="#ffffff", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=(0, 10))
        
        self.delete_button = tk.Button(self.root, text="Delete Task", font=("Arial", 14), bg="#F44336", fg="#ffffff", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=(0, 10))

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            new_task = simpledialog.askstring("Update Task", "Edit the task:", initialvalue=self.tasks[selected_task_index])
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_listbox()
                messagebox.showinfo("Success", "Updated successfully")
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")
        
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            response = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if response:
                selected_task_index = selected_task_index[0]
                del self.tasks[selected_task_index]
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{idx}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
