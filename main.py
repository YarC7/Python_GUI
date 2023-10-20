import tkinter
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
import tkinter as tk
class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("18: Nguyen Duc Canh : Home Page")
        self.geometry("400x850+400+100")

        self.bg_login = ImageTk.PhotoImage(file="bg.jpg")
        self.bg_label = tk.Label(self, image=self.bg_login)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1) 



        self.heading = tk.Label(self, text="Hello, Have a nice day !!!", font="arial 20 bold", fg="black")
        self.heading.pack(pady=(20,0))

        self.heading = tk.Label(self, text="This is Home Page.\nBelow is some Widgets.\nTry Some!", font="arial 20 bold", fg="black")
        self.heading.pack(pady=(20,0))

        


        self.calculator = tk.Label(self, text="Calculator", font="arial 20 bold", fg="black")
        self.calculator.pack(pady=(100,0))
        self.cal_button = tk.Button(self, text="Calculator", font="arial 20 bold", width=10, bg="#5a95ff", fg="#fff", bd=0, command=self.head_to_cal)
        self.cal_button.pack(pady=(10,0))


        self.note = tk.Label(self, text="Note: To-Do-App ", font="arial 20 bold", fg="black")
        self.note.pack(pady=(150,0))
        self.note_button = tk.Button(self, text="Note", font="arial 20 bold", width=10, bg="#5a95ff", fg="#fff", bd=0, command=self.head_to_note)
        self.note_button.pack(pady=(10,0))

        self.footer = tk.Label(self, text="From NgDCanh", font="arial 20 bold", fg="black")

        self.footer.pack(side=tk.BOTTOM, pady=13)





        # Initialize MySQL connection
        self.mysqlConnection = mysql.connector.connect(
            host="127.0.0.1",
            user="canh177",
            password="canhga177",
            database="world"
        )
        self.cursor = self.mysqlConnection.cursor()
    def head_to_cal(self):
    	self.destroy()
    	import calculate



    def head_to_note(self):
    	self.destroy()
    	import note

        

main_page = MainPage()
main_page.mainloop()