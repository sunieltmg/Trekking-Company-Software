from tkinter import *
from tkinter import ttk, messagebox
from classes.login_register_classes import *


def check_username_binary_search(username_list, key):
    lower = 0
    upper = len(username_list) - 1
    while lower <= upper:
        mid_value = (lower + upper) // 2
        if username_list[mid_value][0] == key:
            return True

        elif key > username_list[mid_value][0]:
            lower = mid_value + 1
        else:
            upper = mid_value - 1

    return False


class Register:
    """ Performs tasks like admin/employee registration"""
    def __init__(self):
        self.window = Tk()
        self.window.title('Register Window')
        self.window.geometry('900x560+300+30')
        self.window.resizable(False, False)

        self.login_register_classes=LoginRegisterClasses()

        title = Label(self.window, text="Welcome to Adventure Everest Team Treks\n&\nExpedition",
                      font=('helvetica', 20, 'bold'))
        title.place(x=170, y=30)

        self.first_name = Label(self.window, text='First Name', font=('helvetica', 10))
        self.first_name.place(x=100, y=180)
        self.first_name_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.first_name_entry.place(x=200, y=180)

        self.last_name = Label(self.window, text='Last Name', font=('helvetica', 10))
        self.last_name.place(x=100, y=230)
        self.last_name_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.last_name_entry.place(x=200, y=230)

        self.mobile_no = Label(self.window, text='Mobile No', font=('helvetica', 10))
        self.mobile_no.place(x=100, y=280)
        self.mobile_no_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.mobile_no_entry.place(x=200, y=280)

        self.gender = Label(self.window, text='Gender', font=('helvetica', 10))
        self.gender.place(x=100, y=330)
        self.gender_combo = ttk.Combobox(self.window, font=('helvetica', 10), width=23)
        self.gender_combo.place(x=200, y=330)
        self.gender_combo['values'] = ['Male', 'Female', 'Other']

        self.date_of_birth = Label(self.window, text='Date Of Birth', font=('helvetica', 10))
        self.date_of_birth.place(x=100, y=380)
        self.date_of_birth_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.date_of_birth_entry.place(x=200, y=380)

        self.address = Label(self.window, text='Address', font=('helvetica', 10))
        self.address.place(x=100, y=430)
        self.address_text = Text(self.window, font=('helvetica', 10), width=25, height=4)
        self.address_text.place(x=200, y=430)

        self.username = Label(self.window, text='Username', font=('helvetica', 10))
        self.username.place(x=450, y=180)
        self.username_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.username_entry.place(x=600, y=180)

        self.email = Label(self.window, text='Email', font=('helvetica', 10))
        self.email.place(x=450, y=230)
        self.email_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.email_entry.place(x=600, y=230)

        self.password = Label(self.window, text='Password', font=('helvetica', 10))
        self.password.place(x=450, y=280)
        self.password_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.password_entry.place(x=600, y=280)

        self.confirm_password = Label(self.window, text='Confirm Password', font=('helvetica', 10))
        self.confirm_password.place(x=450, y=330)
        self.confirm_password_entry = Entry(self.window, font=('helvetica', 10), width=25)
        self.confirm_password_entry.place(x=600, y=330)
        # self.chk = IntVar()
        # self.check = Checkbutton(self.window,
        #                          text='I Agree The Terms & Condition', variable=self.chk, onvalue=1, offvalue=0,
        #                          bg="#2f3838", fg='gray')
        # self.check.place(x=450, y=390)

        register_button = Button(self.window, text='Register', font=('helvetica'), bg='black', fg='white',
                                 activebackground='white', activeforeground='black',
                                 width=20, pady=5, bd=1, relief='groove',command=self.registration)
        register_button.place(x=450, y=450)

        back_button = Button(self.window, text='Back', font=('helvetica'), bg='black', fg='white',
                                 activebackground='white', activeforeground='black',
                                 width=20, pady=5, bd=1, relief='groove', command=self.back)
        back_button.place(x=450, y=510)

        self.window.mainloop()

    def registration(self):
        first_name=self.first_name_entry.get()
        last_name=self.last_name_entry.get()
        mobile_no=self.mobile_no_entry.get()
        gender=self.gender_combo.get()
        date_of_birth=self.date_of_birth_entry.get()
        address=self.address_text.get("1.0",END)
        username=self.username_entry.get()
        email=self.email_entry.get()
        password=self.password_entry.get()
        confirm_password=self.confirm_password_entry.get()

        username_list = self.login_register_classes.check_username()
        if first_name=="" or last_name=="" or mobile_no=="" or gender==""\
                or date_of_birth=="" or address=="" or username == "" or\
                email=="" or password == "" or confirm_password=="":
            messagebox.showerror('ERROR', 'All fields are required',parent=self.window)

        # elif self.chk.get() == 0:
        #     messagebox.showerror('ERROR', 'Agree All Terms & Condition',parent=self.window)

        elif check_username_binary_search(username_list, username):
            messagebox.showerror('ERROR', 'User already exists,'
                                          'try another username')

        else:
            self.login_register_classes.registration(first_name, last_name, mobile_no,
                                                     gender, date_of_birth, address, username,
                                                     email, password,confirm_password)
            messagebox.showinfo('REGISTER', 'Registration Success',parent=self.window)
            self.clear()

    def back(self):
        self.window.destroy()

    def clear(self):
        self.first_name_entry.delete(0,END)
        self.last_name_entry.delete(0,END)
        self.mobile_no_entry.delete(0,END)
        self.date_of_birth_entry.delete(0,END)
        self.address_text.delete("1.0", END)
        self.username_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)
        self.confirm_password_entry.delete(0,END)


if __name__=="__main__":
    Register()