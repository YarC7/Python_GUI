import tkinter as tk
import mysql.connector

class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("18: Nguyen Duc Canh : To-Do-List Page")
        self.geometry("400x850+400+100")

        # Initialize MySQL connection
        self.mysqlConnection = mysql.connector.connect(
            host="127.0.0.1",
            user="canh177",
            password="canhga177",
            database="world"
        )
        self.cursor = self.mysqlConnection.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS NOTE (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            TITLE VARCHAR(255),
    		TASK VARCHAR(255)
        );''')

        self.task_list = []

        self.Image_icon = tk.PhotoImage(file="note.png")
        self.iconphoto(False, self.Image_icon)

        self.TopImage = tk.PhotoImage(file="topbar.png")
        tk.Label(self, image=self.TopImage).pack()

        self.dockImage = tk.PhotoImage(file="dock.png")
        tk.Label(self, image=self.dockImage, bg="#32405b").place(x=30, y=25)

        self.noteImage = tk.PhotoImage(file="task.png")
        tk.Label(self, image=self.noteImage, bg="#32405b").place(x=340, y=25)

        self.heading = tk.Label(self, text="All Task", font="arial 20 bold", fg="white", bg="#32405b")
        self.heading.place(x=150, y=20)

        self.frame = tk.Frame(self, width=400, height=50, bg="white")
        self.frame.place(x=0, y=230)

        self.frame2 = tk.Frame(self, width=400, height=50, bg="white")
        self.frame2.place(x=0, y=130)

        #title
        self.title = tk.StringVar()
        

        self.placeholder_title = "Input Title ..."
        self.title_entry = tk.Entry(self.frame2, width=18, font="arial 20", bd=0, fg="gray", textvariable=self.title)
        self.title_entry.bind("<FocusIn>", self.on_title_entry_focus_in)
        self.title_entry.bind("<FocusOut>", self.on_title_entry_focus_out)
        self.title_entry.insert(0, self.placeholder_title)
        self.title_entry.place(x=10, y=4)

        #task
        self.task = tk.StringVar()
        
        self.placeholder_text = "Input Task ..."
        self.task_entry = tk.Entry(self.frame, width=18, font="arial 20", bd=0, fg="gray", textvariable=self.task)
        self.task_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.task_entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.task_entry.insert(0, self.placeholder_text)
        self.task_entry.place(x=10, y=7)


        self.button = tk.Button(self.frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=self.add_task)
        self.button.place(x=300, y=0)

        self.frame1 = tk.Frame(self, bd=3, width=700, height=280, bg="#32405b")
        self.frame1.pack(pady=(320, 0))

        self.listbox = tk.Listbox(self.frame1, font=('arial', 12), width=40, height=16, bg="#32405b", cursor="hand2", fg="white", selectbackground="#5a95ff")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
        self.scrollbar = tk.Scrollbar(self.frame1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.load_tasks()  # Load tasks from the database

        self.delete_icon = tk.PhotoImage(file="delete.png")
        self.delete_button = tk.Button(self, image=self.delete_icon, bd=0, command=self.delete_task)
        self.delete_button.pack(side=tk.BOTTOM, pady=13)

    def on_entry_focus_in(self, event):
    	placeholder_text = "Input Task ..."
    	if self.task_entry.get() == self.placeholder_text:
            self.task_entry.delete(0, tk.END)
            self.task_entry.configure(fg="black")

    def on_title_entry_focus_in(self, event):
        placeholder_title = "Input Title ..."
        if self.title_entry.get() == self.placeholder_title:
            self.title_entry.delete(0, tk.END)
            self.title_entry.configure(fg="black")        

    def on_entry_focus_out(self, event):
    	placeholder_text = "Input Task ..."
    	if self.task_entry.get() == "":
            self.task_entry.insert(0, self.placeholder_text)
            self.task_entry.configure(fg="gray")

    def on_title_entry_focus_out(self, event):
    	placeholder_title = "Input Title ..."
    	if self.title_entry.get() == "":
            self.title_entry.insert(0, self.placeholder_title)
            self.title_entry.configure(fg="gray")



    def add_task(self):
        title_text = self.title.get()
        task_text = self.task_entry.get()
        
        if title_text and task_text and task_text != self.placeholder_text:
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, self.placeholder_text)
            self.task_entry.configure(fg="gray")
            self.task_entry.configure(show="*")
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, self.placeholder_text)
            self.title_entry.configure(fg="gray")
            
            full_task = f"{title_text}: {task_text}"
            self.task_list.append(full_task)
            self.listbox.insert(tk.END, full_task)
            
            # Add the task to the database
            self.cursor.execute("INSERT INTO NOTE (TITLE, TASK) VALUES (%s, %s)", (title_text, task_text))
            self.mysqlConnection.commit()
            self.on_title_entry_focus_out
            self.on_entry_focus_out

    def delete_task(self):
        selected_task = self.listbox.get(self.listbox.curselection())
        if selected_task:
            self.listbox.delete(self.listbox.curselection())

            # Delete the task from the database
            self.cursor.execute("DELETE FROM NOTE WHERE TASK = %s", (selected_task,))
            self.mysqlConnection.commit()

    def load_tasks(self):
        self.cursor.execute("SELECT TITLE, TASK FROM NOTE")
        tasks = self.cursor.fetchall()
        for task in tasks:
            full_task = f"{task[0]}: {task[1]}"
            self.listbox.insert(tk.END, full_task)

app = ToDoListApp()
app.mainloop()