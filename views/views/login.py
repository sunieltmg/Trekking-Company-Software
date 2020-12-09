from tkinter import *
from classes.login_register_classes import *
from views.permit import *
from views.admin import *
from views.employee import *
from tkinter import ttk, messagebox
from views.register import *


def open_register():
    Register()


class Login:
    """ Performs tasks like admin/employee registration"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Login Window')
        self.window.geometry('900x550+300+30')
        self.window.resizable(False, False)

        self.login_register_classes = LoginRegisterClasses()
        title = Label(self.window,
                      text="Welcome to Adventure Everest Team Treks"
                           "\n&\nExpedition\nPlease Register if you"
                           " are new to system",
                      font=('helvetica', 20, 'bold'))
        title.place(x=170, y=30)

        self.user_name = Label(self.window, text='Username', font=('helvetica', 10))
        self.user_name.place(x=100, y=230)
        self.user_name_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.user_name_entry.place(x=200, y=230)

        self.password = Label(self.window, text='Password', font=('helvetica', 10))
        self.password.place(x=450, y=230)
        self.password_entry = Entry(self.window, font=('helvetica', 10), width=25, show="*")
        self.password_entry.place(x=600, y=230)

        login_button = Button(self.window, text='Login', font='helvetica', bg='black', fg='white',
                              activebackground='white', activeforeground='black',
                              width=36, pady=5, bd=1, relief='groove', command=self.click_login)
        login_button.place(x=300, y=330)

        register_button = Button(self.window, text='Register', font='helvetica', bg='green', fg='white',
                                 activebackground='white', activeforeground='green',
                                 width=36, pady=5, bd=1, relief='groove', command=open_register)
        register_button.place(x=300, y=430)

        self.window.mainloop()

    def click_login(self):
        username = self.user_name_entry.get()
        password = self.password_entry.get()
        if username == "" and password == "":
            messagebox.showerror('ERROR', 'All fields are required')

        else:
            login_data = self.login_register_classes.login(username, password)
            self.logged()

    def logged(self):
        username = self.user_name_entry.get()
        password = self.password_entry.get()
        login_data = self.login_register_classes.login(username, password)
        data = self.login_register_classes.admin_or_user(username, password)
        if login_data == 1:
            if data[0][9] == 'Admin':
                self.window.destroy()
                Admin()
            else:
                self.window.destroy()
                Permit()
        else:
            messagebox.showerror('Error', 'Username or password not matched')


if __name__ == "__main__":
    Login()
