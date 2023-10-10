import tkinter as tk
from tkinter import Tk, ttk, messagebox
from ttkbootstrap import Style
import json 

class todolistapp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("To-do List App")
        self.geometry("500x500")
        style = Style(theme="flatly")
        style.configure("Custon.TEntry", foreground="gray")

        #create input field for adding tasks
        self.task_inp = ttk.Entry(self, font=("TkDefaultFont", 16),width = 30, style = "Custon.TEntry")
        self.task_inp.pack(pady=10)

        #set placeholder for input field 
        self.task_inp.insert(0,"Enter your todo here...")

        #bind event to clear placeholder when input field is clicked
        self.task_inp.bind("<FocusIn>", self.clear_placeholder)

        #bind event to restore placeholder when input field loses focus
        self.task_inp.bind("<FocusOut>", self.restore_placeholder)

        #create button for adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        #create listbox to display added tasks
        self.list = tk.Listbox(self, font=("TkDefaultFont", 16),height=10, selectmode=tk.NONE)
        self.list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        #create buttons for marking tasks as done or deleting them 
        ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)

        #create button fro displaying task statistics
        ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_stats).pack(side=tk.BOTTOM, pady=10)
        self.load_tasks()
    
    def view_stats(self):
        done_count=0
        tot_count=self.list.size()
        for i in range(tot_count):
            if self.list.itemget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics","Total tasks: {tot_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task=self.task_inp.get()
        if task!="Enter your todo here...":
            self.list.insert(tk.END,task)
            self.list.itemconfig(tk.END, fg="orange")
            self.task_inp.delete(0, tk.END)
            self.save_tasks()

    def mark_done(self):
        task_index = self.list.curselection()
        if task_index:
            self.list.itemconfig(task_index, fg= "green")
            self.save_tasks()

    def delete_task(self):
        task_index = self.list.curselection()
        if task_index:
            self.list.delete(task_index)
            self.save_tasks()

    def clear_placeholder(self, event):
        if self.task_inp.get() == "Enter your todo here...":
            self.task_inp.delete(0, tk.END)
            self.task_inp.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_inp.insert(0, "Enter your todo here...")
            self.task_inp.configure(style="Custon.TEntry")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.list.insert(tk.END, task["text"])
                    self.list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass
    def save_tasks(self):
        data = []
        for i in range(self.list.size()):
            text = self.list.get(i)
            color = self.list.itemget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f: 
            json.dump(data, f)

if __name__ == '__main__':
    app = todolistapp()
    app.mainloop()
