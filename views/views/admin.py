from tkinter import *
from tkinter import ttk, messagebox
from views.system import *
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


class Admin:
    """ Performs admin level tasks like assigning role, changing password, deleting user, managing peak, bill"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Admin Window')
        self.window.geometry('1350x700+0+0')
        self.window.resizable(False, False)
        self.update_index = ""

        self.login_register_classes = LoginRegisterClasses()
        self.admin_classes = AdminClasses()

        title = Label(self.window,
                      text="Welcome to Adventure Everest Team Treks & Expedition \t\t|Admin Panel",
                      font=('helvetica', 15, 'bold'),
                      bg="green", fg="white")
        title.pack(fill=BOTH)

        delete_text = Label(self.window, text='Double click to delete employee information by selecting that row',
                            font=('times new roman', 10))
        delete_text.place(x=400, y=30)

        self.search_frame = Frame(self.window, width=920, height=50, bg='lightgray')
        self.search_frame.place(x=200, y=70)

        search_title = Label(self.search_frame, text='Sarch By:', font=('helvetica', 15, 'bold'),
                             fg='black',
                             bg='lightgray')
        search_title.place(x=10, y=5)

        self.search_option_combo = ttk.Combobox(self.search_frame, font=('helvetica', 10, 'bold'), width=23)
        self.search_option_combo.place(x=130, y=5)
        self.search_option_combo['values'] = ['emp_id', 'mobile_no', 'email']
        self.search_option_combo.set('Select Option')

        self.search_value_entry = Entry(self.search_frame, font=('helvetica', 10, 'bold'), width=25)
        self.search_value_entry.place(x=350, y=5)

        search_button = Button(self.search_frame, text='Search', font='helvetica', bg='green', fg='white',
                               activebackground='white', activeforeground='green',
                               width=10, pady=5, bd=1, relief='groove', command=self.search_employee)
        search_button.place(x=550, y=5)

        clear_button = Button(self.search_frame, text='Clear', font='helvetica', bg='green', fg='white',
                              activebackground='white', activeforeground='green',
                              width=10, pady=5, bd=1, relief='groove', command=self.search_clear)
        clear_button.place(x=680, y=5)

        show_all_button = Button(self.search_frame, text='Show all', font='helvetica', bg='green', fg='white',
                                 activebackground='white', activeforeground='green',
                                 width=10, pady=5, bd=1, relief='groove', command=self.show_all)
        show_all_button.place(x=810, y=5)

        self.assign_role_frame = Frame(self.window, width=300, height=400, bg='lightgreen')
        self.assign_role_frame.place(x=10, y=150)

        assign_role_title = Label(self.assign_role_frame, text='Assign Role', font=('helvetica', 15, 'bold'),
                                  fg='black',
                                  bg='lightgreen')
        assign_role_title.place(x=70, y=5)

        self.select_employee_combo = ttk.Combobox(self.assign_role_frame, font=('helvetica', 10, 'bold'), width=23)
        self.select_employee_combo.place(x=50, y=55)
        self.select_employee_combo.set('Select Employee')

        self.select_role_combo = ttk.Combobox(self.assign_role_frame, font=('helvetica', 10, 'bold'), width=23)
        self.select_role_combo.place(x=50, y=105)
        self.select_role_combo['values'] = ['Admin', 'Employee']
        self.select_role_combo.set('Select Role')

        clear_button = Button(self.assign_role_frame, text='Clear', font='helvetica', bg='green', fg='white',
                              activebackground='white', activeforeground='green',
                              width=20, pady=5, bd=1, relief='groove', command=self.clear_assign)
        clear_button.place(x=49, y=200)

        assign_button = Button(self.assign_role_frame, text='Assign', font='helvetica', bg='green', fg='white',
                               activebackground='white', activeforeground='green',
                               width=20, pady=5, bd=1, relief='groove', command=self.assign_role)
        assign_button.place(x=49, y=280)

        self.admin_detail_frame = LabelFrame(self.window, text='Employee Detail')
        self.admin_detail_frame.place(x=320, y=150, width=700, height=400)

        self.scroll_x = ttk.Scrollbar(self.admin_detail_frame, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(self.admin_detail_frame, orient=VERTICAL)
        self.employee_detail_tree = ttk.Treeview(self.admin_detail_frame, column=('employee_id',
                                                                                  'first_name', 'last_name',
                                                                                  'mobile_no', 'gender',
                                                                                  'date_of_birth', 'address',
                                                                                  'username', 'email', 'type',
                                                                                  'password'))

        self.scroll_x.config(command=self.employee_detail_tree.xview)
        self.scroll_y.config(command=self.employee_detail_tree.yview)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.employee_detail_tree.config(xscrollcommand=self.scroll_x.set,
                                         yscrollcommand=self.scroll_y.set)

        self.employee_detail_tree['show'] = 'headings'
        self.employee_detail_tree.heading('employee_id', text='Employee Id')
        self.employee_detail_tree.heading('first_name', text='First_Name')
        self.employee_detail_tree.heading('last_name', text='Last_Name')
        self.employee_detail_tree.heading('mobile_no', text='Mobile_No')
        self.employee_detail_tree.heading('gender', text='Gender')
        self.employee_detail_tree.heading('date_of_birth', text='Date_Of_Birth')
        self.employee_detail_tree.heading('address', text='Address')
        self.employee_detail_tree.heading('username', text='Username')
        self.employee_detail_tree.heading('email', text='Email')
        self.employee_detail_tree.heading('type', text='Type')
        self.employee_detail_tree.heading('password', text='Password')
        self.employee_detail_tree.pack(fill=BOTH, expand=1)

        self.change_password_frame = Frame(self.window, height=400, width=310, bg='lightgreen')
        self.change_password_frame.place(x=1025, y=150)

        change_password_title = Label(self.change_password_frame, text='Change Password',
                                      font=('helvetica', 15, 'bold'),
                                      fg='black',
                                      bg='lightgreen')
        change_password_title.place(x=70, y=5)

        username = Label(self.change_password_frame, text='Username', font=('helvetica', 10), bg='lightgreen')
        username.place(x=120, y=50)
        self.username_entry = Entry(self.change_password_frame, width=30)
        self.username_entry.place(x=70, y=80)

        old_password = Label(self.change_password_frame, text='Old Password', font=('helvetica', 10), bg='lightgreen')
        old_password.place(x=120, y=130)
        self.old_password_entry = Entry(self.change_password_frame, width=30)
        self.old_password_entry.place(x=70, y=160)

        new_password = Label(self.change_password_frame, text='New Password', font=('helvetica', 10), bg='lightgreen')
        new_password.place(x=120, y=210)
        self.new_password_entry = Entry(self.change_password_frame, width=30)
        self.new_password_entry.place(x=70, y=240)

        clear_button = Button(self.change_password_frame, text='Clear', font='helvetica', bg='green', fg='white',
                              activebackground='white', activeforeground='green',
                              width=20, pady=5, bd=1, relief='groove', command=self.clear_password)
        clear_button.place(x=69, y=280)

        change_password_button = Button(self.change_password_frame, text='Change Password', font='helvetica',
                                        bg='green',
                                        fg='white',
                                        activebackground='white', activeforeground='green',
                                        width=20, pady=5, bd=1, relief='groove', command=self.change_password)
        change_password_button.place(x=69, y=340)

        self.delete_employee_frame = LabelFrame(self.window, width=930, height=80, bg='lightgray',
                                                text='Delete Employee')
        self.delete_employee_frame.place(x=200, y=590)

        employee_id_title = Label(self.delete_employee_frame, text='Employee Id:', font=('helvetica', 15, 'bold'),
                                  fg='black',
                                  bg='lightgray')
        employee_id_title.place(x=10, y=5)

        self.employee_id_entry = Entry(self.delete_employee_frame, font=('helvetica', 15), width=20)
        self.employee_id_entry.place(x=180, y=5)

        delete_button = Button(self.delete_employee_frame, text='Delete', font='helvetica', bg='green', fg='white',
                               activebackground='white', activeforeground='green',
                               width=15, pady=5, bd=1, relief='groove', command=self.delete_employee)
        delete_button.place(x=450, y=5)

        go_to_system_button = Button(self.delete_employee_frame, text='Go To System', font='helvetica', bg='green',
                                     fg='white',
                                     activebackground='white', activeforeground='green',
                                     width=15, pady=5, bd=1, relief='groove', command=self.system)
        go_to_system_button.place(x=610, y=5)

        exit_button = Button(self.delete_employee_frame, text='Exit', font='helvetica', bg='green', fg='white',
                             activebackground='white', activeforeground='green',
                             width=15, pady=5, bd=1, relief='groove', command=self.exit)
        exit_button.place(x=770, y=5)
        self.combo_assign_user_value()
        self.show_items_in_tree()

        self.window.mainloop()

    def system(self):
        self.window.destroy()
        System()

    def combo_assign_user_value(self):
        user = []
        data = self.login_register_classes.check_username()
        for detail in data:
            user.append(detail[0])

        self.select_employee_combo['values'] = user

    def clear_assign(self):
        self.select_employee_combo.set("")
        self.select_role_combo.set("")

    def assign_role(self):
        employee = self.select_employee_combo.get()
        role = self.select_role_combo.get()
        if employee == "" or role == "":
            messagebox.showerror('ERROR', 'All fields are required',
                                 parent=self.window)
            return False

        if self.admin_classes.assign_role(role, employee):
            messagebox.showinfo('CHANGED', 'User status is changed sucessfully'
                                , parent=self.window)
            self.show_items_in_tree()

        else:
            messagebox.showerror('ERROR', 'User is not changed',
                                 parent=self.window)

    def change_password(self):
        username_list = self.login_register_classes.check_username()
        username = self.username_entry.get()
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()

        if username == "" or old_password == "" or new_password == "":
            messagebox.showerror('ERROR', 'All Fields are required',
                                 parent=self.window)

        elif check_username_binary_search(username_list, username) is False:
            messagebox.showerror('ERROR', 'User does not exists,'
                                          'Check username and try again', parent=self.window)

        elif self.admin_classes.change_password(new_password, username,
                                                old_password):
            messagebox.showinfo('SUCESS', 'Password udapted successfully',
                                parent=self.window)
            self.show_items_in_tree()

    def clear_password(self):
        self.username_entry.delete(0, END)
        self.old_password_entry.delete(0, END)
        self.new_password_entry.delete(0, END)

    def show_items_in_tree(self):
        data = self.admin_classes.employee_detail()
        self.employee_detail_tree.delete(*self.employee_detail_tree.get_children())

        for detail in data:
            self.employee_detail_tree.insert("", 'end', text=detail[0],
                                             values=(detail[0], detail[1], detail[2], detail[3],
                                                     detail[4], detail[5], detail[6],
                                                     detail[7], detail[8], detail[9],
                                                     detail[10], detail[11]))
        self.employee_detail_tree.bind("<Double-1>", self.select_data)

    def select_data(self, event):
        self.selected_row = self.employee_detail_tree.selection()[0]
        self.update_index = self.employee_detail_tree.item(self.selected_row, 'text')
        self.selected_value = self.employee_detail_tree.item(self.selected_row,
                                                             'values')
        self.employee_id_entry.delete(0, END)
        self.employee_id_entry.insert(0, self.selected_value[0])

    def delete_employee(self):
        employee_id = self.employee_id_entry.get()
        if employee_id == "":
            messagebox.showerror('ERROR', 'Select employee first to delete', parent=self.window)
            return False

        elif self.admin_classes.delete_employee(employee_id):
            messagebox.showinfo('DELETE', 'Employee details deleted successfully', parent=self.window)
            self.show_items_in_tree()

    def exit(self):
        self.window.destroy()

    def search_employee(self):
        option = self.search_option_combo.get()
        value = self.search_value_entry.get()
        if option == "" or value == "":
            messagebox.showerror('ERROR', 'ALL Fields ARE REQUIRED', parent=self.window)
            return False

        else:
            data = self.admin_classes.search_employee(option,
                                                      value)
            self.employee_detail_tree.delete(*self.employee_detail_tree.get_children())
            if len(data) >= 1:
                for detail in data:
                    self.employee_detail_tree.insert("", 'end', text=detail[0],
                                                     values=(detail[0], detail[1], detail[2],
                                                             detail[3], detail[4],
                                                             detail[5], detail[6],
                                                             detail[7], detail[8],
                                                             detail[9], detail[10],
                                                             detail[11]))

                    self.employee_detail_tree.bind("<Double-1>", self.select_data)
            else:
                messagebox.showerror('ERROR', 'FIELD NOT FOUND')

    def search_clear(self):
        self.search_option_combo.set("")
        self.search_value_entry.delete(0, END)

    def show_all(self):
        self.show_items_in_tree()


if __name__ == "__main__":
    Admin()
