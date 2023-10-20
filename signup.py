import tkinter
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("18: Nguyen Duc Canh : Registing Page")
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



# Connect to MySQL database
mysqlConnection = mysql.connector.connect(
    host="127.0.0.1",
    user="canh177",
    password="canhga177",
    database="world"
)
cursor = mysqlConnection.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    EMAIL VARCHAR(255),
    USERNAME VARCHAR(255),
    PASSWORD VARCHAR(255)
);''')

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

def head_to_login_page():
    window.destroy()
    import login


def sign_up():
    if email.get() and username.get() and password.get():
        try:
            cursor.execute("INSERT INTO USER (EMAIL, USERNAME, PASSWORD) VALUES (%s, %s, %s)",
                           (email.get(), username.get(), password.get()))
            mysqlConnection.commit()
            messagebox.showinfo(title="Sign Up Success", message=f"Successfully signed up with username: {username.get()}")
        except mysql.connector.Error as e:
            messagebox.showerror(title="Sign Up Error", message=f"Error: {str(e)}")

bg_image = Image.open("login_bg.jpg")
bg_login = ImageTk.PhotoImage(bg_image)

bg_label = tkinter.Label(window, image=bg_login)
bg_label.place(x=0, y=0)

username = tkinter.StringVar()
password = tkinter.StringVar()
email = tkinter.StringVar()

signup_label = tkinter.Label(window, text="Signup", bg="#FFFFFF", fg="#333333", font=("Arial", 30))
email_label = tkinter.Label(window, text="Email", bg="#FFFFFF", fg="#333333", font=("Arial", 16))
email_entry = tkinter.Entry(window, font=("Arial", 16), textvariable=email)
ToolTip(email_entry, 'This is where you type your email here to sign up !!!')

username_label = tkinter.Label(window, text="Username", bg="#FFFFFF", fg="#333333", font=("Arial", 16))
username_entry = tkinter.Entry(window, font=("Arial", 16), textvariable=username)
ToolTip(username_entry, 'This is where you type your username here to sign up !!!')

password_label = tkinter.Label(window, text="Password", bg="#FFFFFF", fg="#333333", font=("Arial", 16))
password_entry = tkinter.Entry(window, show="*", font=("Arial", 16), textvariable=password)
ToolTip(password_entry, 'This is where you type your password here to login !!!')

signup_button = tkinter.Button(window, font=("Arial", 20), text="Sign Up", bg="#FF3399", fg="#FFFFFF", command=sign_up)
ToolTip(signup_button, 'Click to Sign up !!!')

already_label = tkinter.Label(window, text="Already have an account , Sign In !!!", bg="#FFFFFF", fg="#333333", font=("Arial", 16))
login_button = tkinter.Button(window, font=("Arial", 20), text="Login", bg="white",border = 4,cursor='hand2',fg='black', command=head_to_login_page)
ToolTip(login_button, 'Click to head to the login page !!!')


signup_label.place(x=1215, y=257)
email_label.place(x=1100, y=350)
email_entry.place(x=1230, y=350)
username_label.place(x=1100, y=450)
username_entry.place(x=1230, y=450)
password_label.place(x=1100, y=550)
password_entry.place(x=1230, y=550)
already_label.place(x=1100, y= 625)
login_button.place(x=1500, y=600)
signup_button.place(x=1230, y=700)

window.mainloop()

