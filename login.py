import tkinter
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

window = tkinter.Tk()
window.title("18: Nguyen Duc Canh : Login Page")
window.geometry('1920x1280')


menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)

def _msgBox():
    messagebox.showinfo('Message From Owner ','This is made by NgDCanh!!!')



file_menu = tkinter.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
help_menu = tkinter.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)
menu_bar.add_cascade(label='Help', menu=help_menu)

bg_login = ImageTk.PhotoImage(file="login_bg.jpg")
bg_label = tkinter.Label(window, image=bg_login)

# Initialize MySQL connection
mysqlConnection = mysql.connector.connect(
    host="127.0.0.1",
    user="canh177",
    password="canhga177",
    database="world"
)
cursor = mysqlConnection.cursor()

class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        x_left = self.widget.winfo_rootx()
        y_top = self.widget.winfo_rooty() - 18
        self.tip_window = tkinter.Toplevel(self.widget)
        self.tip_window.overrideredirect(True)
        self.tip_window.geometry("+%d+%d" % (x_left, y_top))
        label = tkinter.Label(
            self.tip_window,
            text=self.tip_text,
            justify=tkinter.LEFT,
            background="#ffffe0",
            relief=tkinter.SOLID,
            borderwidth=1,
            font=("tahoma", "8", "normal")
        )
        label.pack(ipadx=1)

    def hide_tooltip(self):
        if hasattr(self, 'tip_window') and self.tip_window:
            self.tip_window.destroy()


def head_to_main_page():
    window.destroy()
    import main


def head_to_register_page():
    window.destroy()
    import signup


def login():
    entered_email = username.get()
    entered_password = password.get()

    # Query the database to check if the entered email and password exist
    cursor.execute("SELECT EMAIL, PASSWORD FROM USER WHERE EMAIL = %s", (entered_email,))
    result = cursor.fetchone()

    if result:
        stored_email, stored_password = result
        if entered_password == stored_password:
            messagebox.showinfo(title="Login Success", message=f"Successfully logged in with email: {entered_email}")
            head_to_note_page()  	
        else:
            messagebox.showerror(title="Error", message="Incorrect password, please try again.")
    else:
        messagebox.showerror(title="Error", message="User not found, please try another email.")

bg_label = tkinter.Label(window, image=bg_login)
bg_label.place(x=0, y=0)

username = tkinter.StringVar()
password = tkinter.StringVar()

login_label = tkinter.Label(window, text="Login", bg="#FFFFFF", fg="#333333", font=("Arial", 30))
username_label = tkinter.Label(window, text="Email", bg="#FFFFFF", fg="#333333", font=("Arial", 16)
)
username_entry = tkinter.Entry(window, font=("Arial", 16), textvariable=username)
ToolTip(username_entry, 'This is where you type your email here to login !!!')

password_label = tkinter.Label(window, text="Password", bg="#FFFFFF", fg="#333333", font=("Arial", 16))
password_entry = tkinter.Entry(window, show="*", font=("Arial", 16), textvariable=password)
ToolTip(password_entry, 'This is where you type your password here to login !!!')

login_button = tkinter.Button(window, font=("Arial", 20), text="Login", bg="#FF3399", fg="#FFFFFF", command=login)
ToolTip(login_button, 'Click here to Login !!!')

already_label = tkinter.Label(window, text="Want to Register ,Click Sign Up!!!", bg="#FFFFFF", fg="#333333", font=("Arial", 16))
signup_button = tkinter.Button(window, font=("Arial", 20), text="Signup", bg="white",border = 4,cursor='hand2',fg='black', command=head_to_register_page)
ToolTip(signup_button, 'Click here to go to the Register Page !!!')

login_label.place(x=1250, y=300)
username_label.place(x=1100, y=450)
username_entry.place(x=1230, y=450)
password_label.place(x=1100, y=550)
password_entry.place(x=1230, y=550)
login_button.place(x=1250, y=700)



already_label.place(x=1100, y= 625)
signup_button.place(x=1425, y=600)

username_label.focus()
window.mainloop()
