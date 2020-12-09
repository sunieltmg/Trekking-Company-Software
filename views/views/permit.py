from tkinter import *
from tkinter import ttk, messagebox
from classes.login_register_classes import *
import time
import random


class Permit:
    """ Performs tasks like add/update/delete/search permit"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Employee Window')
        self.window.geometry('1350x700+0+0')
        self.window.configure(bg='lightgray')
        self.window.resizable(False, False)
        self.permit_classes = PermitClasses()
        self.update_index = ""
        self.date = time.strftime("%d/%m/%Y")

        title = Label(self.window,
                      text="Welcome to Adventure Everest Team Treks & Expedition Admin Panel\t\t|Permit Section",
                      font=('helvetica', 15, 'bold'),
                      bg="green", fg="white")
        title.pack(fill=BOTH)

        permit_detail_title = Label(self.window, text='Permit Detail', font=('helvetica', 15, 'bold'),
                                    bg='lightgray')
        permit_detail_title.place(x=500, y=30)

        name_of_peak = Label(self.window, text="Name of Peak",
                             font=('helvetica', 10), bg='lightgray')
        name_of_peak.place(x=20, y=80)

        self.name_of_peak_entry = Entry(self.window, font=('helvetica', 10),
                                        width=25,
                                        bd=1)
        self.name_of_peak_entry.place(x=130, y=80)

        height = Label(self.window, text="Height", font=('helvetica', 10),
                       bg='lightgray')
        height.place(x=330, y=80)

        self.height_entry = Entry(self.window, font=('helvetica', 10),
                                  width=25, bd=1)
        self.height_entry.place(x=480, y=80)

        climbing_period = Label(self.window, text="Climbing Period",
                                font=('helvetica', 10), bg='light gray')
        climbing_period.place(x=680, y=80)

        self.climbing_period_entry = Entry(self.window, font=('helvetica', 10),
                                           width=25)
        self.climbing_period_entry.place(x=800, y=80)

        trekking_route = Label(self.window, text="Trekking Route",
                               font=('helvetica', 10), bg='light gray')
        trekking_route.place(x=1030, y=80)

        self.trekking_route_entry = Entry(self.window, font=('helvetica', 10),
                                          width=25)
        self.trekking_route_entry.place(x=1150, y=80)

        leader_name = Label(self.window, text="Leader(L) Name",
                            font=('helvetica', 10), bg='light gray')
        leader_name.place(x=20, y=110)

        self.leader_name_entry = Entry(self.window, font=('helvetica', 10),
                                       width=25)
        self.leader_name_entry.place(x=130, y=110)

        leader_country = Label(self.window, text="L(Country)",
                               font=('helvetica', 10), bg='light gray')
        leader_country.place(x=330, y=110)

        self.leader_country_entry = Entry(self.window, font=('helvetica', 10),
                                          width=25)
        self.leader_country_entry.place(x=480, y=110)

        leader_passport_no = Label(self.window, text="L(Passport No)",
                                   font=('helvetica', 10), bg='light gray')
        leader_passport_no.place(x=680, y=110)

        self.leader_passport_no_entry = Entry(self.window, font=('helvetica', 10),
                                              width=25)
        self.leader_passport_no_entry.place(x=800, y=110)

        leader_age = Label(self.window, text="L(Age)",
                           font=('helvetica', 10), bg='light gray')
        leader_age.place(x=1030, y=110)

        self.leader_age_entry = Entry(self.window, font=('helvetica', 10),
                                      width=25)
        self.leader_age_entry.place(x=1150, y=110)

        leader_sex = Label(self.window, text="L(Sex)",
                           font=('helvetica', 10), bg='light gray')
        leader_sex.place(x=20, y=140)

        self.leader_sex_combo = ttk.Combobox(self.window, font=('helvetica', 10),
                                             width=22)
        self.leader_sex_combo.place(x=130, y=140)
        self.leader_sex_combo['values'] = ['Male', 'Female', 'Other']
        self.leader_sex_combo.current(0)

        member_name = Label(self.window, text="Member(M) Name",
                            font=('helvetica', 10), bg='light gray')
        member_name.place(x=330, y=140)

        self.member_name_entry = Entry(self.window, font=('helvetica', 10),
                                       width=25)
        self.member_name_entry.place(x=480, y=140)

        member_country = Label(self.window, text="M(Country)", font=('helvetica', 10),
                               bg='light gray')
        member_country.place(x=680, y=140)

        self.member_country_entry = Entry(self.window, font=('helvetica', 10),
                                          width=25)
        self.member_country_entry.place(x=800, y=140)

        member_passport_no = Label(self.window, text="M(Passport No)",
                                   font=('helvetica', 10), bg='light gray')
        member_passport_no.place(x=1030, y=140)

        self.member_passport_no_entry = Entry(self.window, font=('helvetica', 10),
                                              width=25)
        self.member_passport_no_entry.place(x=1150, y=140)

        member_age = Label(self.window, text="M(Age)",
                           font=('helvetica', 10), bg='light gray')
        member_age.place(x=20, y=170)

        self.member_age_entry = Entry(self.window, font=('helvetica', 10),
                                      width=25)
        self.member_age_entry.place(x=130, y=170)

        member_sex = Label(self.window, text="M(Sex)",
                           font=('helvetica', 10), bg='light gray')
        member_sex.place(x=330, y=170)

        self.member_sex_combo = ttk.Combobox(self.window, font=('helvetica', 10),
                                             width=23)
        self.member_sex_combo.place(x=480, y=170)
        self.member_sex_combo['values'] = ['Male', 'Female', 'Other']
        self.member_sex_combo.current(0)

        member_total = Label(self.window, text="M(Total climbers)",
                             font=('helvetica', 10), bg='light gray')
        member_total.place(x=680, y=170)

        self.member_total_entry = Entry(self.window, font=('helvetica', 10),
                                        width=25)
        self.member_total_entry.place(x=800, y=170)

        member_trekking_agency = Label(self.window, text="M(Trekking Agency)",
                                       font=('helvetica', 10), bg='light gray')
        member_trekking_agency.place(x=1030, y=170)

        self.member_trekking_agency_entry = Entry(self.window, font=('helvetica', 10),
                                                  width=25)
        self.member_trekking_agency_entry.place(x=1150, y=170)

        member_guide = Label(self.window, text="M(Guide Name)",
                             font=('helvetica', 10), bg='light gray')
        member_guide.place(x=20, y=200)

        self.member_guide_entry = Entry(self.window, font=('helvetica', 10),
                                        width=25)
        self.member_guide_entry.place(x=130, y=200)

        member_guide_reg = Label(self.window, text="M(Guide NMA  Reg No)",
                                 font=('helvetica', 10), bg='light gray')
        member_guide_reg.place(x=330, y=200)

        self.member_guide_reg_entry = Entry(self.window, font=('helvetica', 10),
                                            width=25)
        self.member_guide_reg_entry.place(x=480, y=200)

        permit_date = Label(self.window, text="M(Permit Date)",
                            font=('helvetica', 10), bg='light gray')
        permit_date.place(x=680, y=200)

        self.permit_date_entry = Entry(self.window, font=('helvetica', 10),
                                       width=25)
        self.permit_date_entry.place(x=800, y=200)

        permit_cost = Label(self.window, text="M(Permit Cost)",
                            font=('helvetica', 10), bg='light gray')
        permit_cost.place(x=1030, y=200)

        self.permit_cost_entry = Entry(self.window, font=('helvetica', 10),
                                       width=25)
        self.permit_cost_entry.place(x=1150, y=200)

        self.employee_detail_frame = Frame(self.window, height=455, width=900, bg='lightgreen')
        self.employee_detail_frame.place(x=10, y=230)

        self.employee_detail_label = Label(self.employee_detail_frame, text='Permit Information',
                                           font=('helvetica', 15, 'bold'), bg='lightgreen')
        self.employee_detail_label.place(x=350, y=10)

        self.search_frame = Frame(self.employee_detail_frame, width=920, height=40, bg='lightgreen')
        self.search_frame.place(x=20, y=50)

        search_title = Label(self.search_frame, text='Sarch By:', font=('helvetica', 10, 'bold'),
                             fg='black',
                             bg='lightgreen')
        search_title.place(x=5, y=5)

        self.search_option_combo = ttk.Combobox(self.search_frame, font=('helvetica', 10, 'bold'), width=20)
        self.search_option_combo.place(x=90, y=5)
        self.search_option_combo['values'] = ['name_of_peak', 'leader_name', 'member_name']

        self.search_value_entry = Entry(self.search_frame, font=('helvetica', 10, 'bold'), width=25)
        self.search_value_entry.place(x=280, y=5)

        search_button = Button(self.search_frame, text='Search', font='helvetica', bg='green', fg='white',
                               activebackground='white', activeforeground='green',
                               width=8, pady=3, bd=1, relief='groove', command=self.search_permit)
        search_button.place(x=500, y=0)

        clear_button = Button(self.search_frame, text='Clear', font='helvetica', bg='green', fg='white',
                              activebackground='white', activeforeground='green',
                              width=8, pady=3, bd=1, relief='groove', command=self.search_clear)
        clear_button.place(x=630, y=0)

        show_all_button = Button(self.search_frame, text='Show all', font='helvetica', bg='green', fg='white',
                                 activebackground='white', activeforeground='green',
                                 width=8, pady=3, bd=1, relief='groove', command=self.show_all)
        show_all_button.place(x=760, y=0)

        self.permit_info_frame = LabelFrame(self.employee_detail_frame, text='Permit Info', bg='lightgreen')
        self.permit_info_frame.place(x=5, y=100, width=890, height=350)

        self.scroll_x = ttk.Scrollbar(self.permit_info_frame, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(self.permit_info_frame, orient=VERTICAL)
        self.permit_info_tree = ttk.Treeview(self.permit_info_frame, column=('name_of_peak',
                                                                             'height', 'climbing_period',
                                                                             'trekking_route',
                                                                             'leader(l)_name', 'l(country)',
                                                                             'l(passport_no)',
                                                                             'l(age)', 'l(sex)', 'member(m)_name',
                                                                             'm(country)', 'm(passport_no)',
                                                                             'm(age)', 'm(sex)', 'm(total_climbers)',
                                                                             'm(trekking_agency)', 'm(guide_name)',
                                                                             'm(guide_nma_reg_no', 'm(permit_date)',
                                                                             'm(permit_cost)'))

        self.scroll_x.config(command=self.permit_info_tree.xview)
        self.scroll_y.config(command=self.permit_info_tree.yview)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.permit_info_tree.config(xscrollcommand=self.scroll_x.set,
                                     yscrollcommand=self.scroll_y.set)

        self.permit_info_tree['show'] = 'headings'
        self.permit_info_tree.heading('name_of_peak', text='Name of Peak')
        self.permit_info_tree.heading('height', text='Height')
        self.permit_info_tree.heading('climbing_period', text='Climbing Period')
        self.permit_info_tree.heading('trekking_route', text='Trekking Route')
        self.permit_info_tree.heading('leader(l)_name', text='Leader(L) Name')
        self.permit_info_tree.heading('l(country)', text='L(Country)')
        self.permit_info_tree.heading('l(passport_no)', text='L(Passport No)')
        self.permit_info_tree.heading('l(age)', text='L(Age)')
        self.permit_info_tree.heading('l(sex)', text='L(Sex)')
        self.permit_info_tree.heading('member(m)_name', text='Member(M) Name')
        self.permit_info_tree.heading('m(country)', text='M(country)')
        self.permit_info_tree.heading('m(passport_no)', text='M(Passport No)')
        self.permit_info_tree.heading('m(age)', text='M(Age)')
        self.permit_info_tree.heading('m(sex)', text='M(Sex)')
        self.permit_info_tree.heading('m(total_climbers)', text='M(Total climbers)')
        self.permit_info_tree.heading('m(trekking_agency)', text='M(Trekking Agency)')
        self.permit_info_tree.heading('m(guide_name)', text='M(Guide Name)')
        self.permit_info_tree.heading('m(guide_nma_reg_no', text='M(Guide NMA Reg No')
        self.permit_info_tree.heading('m(permit_date)', text='M(Permit Date)')
        self.permit_info_tree.heading('m(permit_cost)', text='M(Permit Cost')
        self.permit_info_tree.pack(fill=BOTH, expand=1)

        self.permit_function_frame = Frame(self.window, width=450, height=100, bg='#164d1c')
        self.permit_function_frame.place(x=910, y=230)

        add_button = Button(self.permit_function_frame, text='Add', font='helvetica', bg='lightgreen', fg='black',
                            activebackground='white', activeforeground='green',
                            width=7, pady=5, bd=1, relief='groove', command=self.add_permit)
        add_button.place(x=5, y=30)

        update_button = Button(self.permit_function_frame, text='Update', font='helvetica', bg='lightgreen', fg='black',
                               activebackground='white', activeforeground='green',
                               width=7, pady=5, bd=1, relief='groove', command=self.update_permit)
        update_button.place(x=90, y=30)

        delete_button = Button(self.permit_function_frame, text='Delete', font='helvetica', bg='lightgreen', fg='black',
                               activebackground='white', activeforeground='green',
                               width=7, pady=5, bd=1, relief='groove', command=self.delete_permit)
        delete_button.place(x=175, y=30)

        clear_button = Button(self.permit_function_frame, text='Clear', font='helvetica', bg='lightgreen', fg='black',
                              activebackground='white', activeforeground='green',
                              width=7, pady=5, bd=1, relief='groove', command=self.clear_permit)
        clear_button.place(x=260, y=30)

        generate_bill_button = Button(self.permit_function_frame, text='Generate Bill', font='helvetica',
                                      bg='lightgreen', fg='black',
                                      activebackground='white', activeforeground='green',
                                      width=10, pady=5, bd=1, relief='groove', command=self.generate_bill)
        generate_bill_button.place(x=340, y=30)

        self.view_bill_frame = Frame(self.window, bg='white')
        self.view_bill_frame.place(x=910, y=325, width=450, height=360)

        self.bill_area = Label(self.view_bill_frame, text='Billing Area',
                               font=('helvetica', 10, 'bold'),
                               bg='white', fg='black', pady=2)
        self.bill_area.pack(fill=X)

        self.scroll_y = ttk.Scrollbar(self.view_bill_frame, orient=VERTICAL)
        self.bill_text_area = Text(self.view_bill_frame,
                                   yscrollcommand=self.scroll_y.set)
        self.bill_text_area.insert(END, "\tAdventure Everest Team Treks "
                                        "& Expedition")
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.bill_text_area.yview)
        self.bill_text_area.pack(fill=BOTH, expand=1)
        self.show_items_in_tree()

        self.window.mainloop()

    def clear_permit(self):
        self.name_of_peak_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.climbing_period_entry.delete(0, END)
        self.trekking_route_entry.delete(0, END)
        self.leader_name_entry.delete(0, END)
        self.leader_country_entry.delete(0, END)
        self.leader_passport_no_entry.delete(0, END)
        self.leader_age_entry.delete(0, END)
        self.member_name_entry.delete(0, END)
        self.member_country_entry.delete(0, END)
        self.member_passport_no_entry.delete(0, END)
        self.member_age_entry.delete(0, END)
        self.member_total_entry.delete(0, END)
        self.member_trekking_agency_entry.delete(0, END)
        self.member_guide_entry.delete(0, END)
        self.member_guide_reg_entry.delete(0, END)
        self.permit_date_entry.delete(0, END)
        self.permit_cost_entry.delete(0, END)

    def add_permit(self):
        self.get_interface_value()
        if self.name_of_peak == "" or self.height == "" or self.climbing_period == "" \
                or self.trekking_route == "" or self.leader_name == "" or \
                self.leader_country == "" or self.leader_passport_no == "" \
                or self.leader_age == "" or self.leader_sex == "" or self.member_name \
                == "" or self.member_country == "" or self.member_passport_no == "" \
                or self.member_age == "" or self.member_sex == "" or \
                self.total_climber == "" or self.name_of_trekking_company == "" \
                or self.name_of_guide == "" or self.guide_reg == "" or self.permit_date == "" \
                or self.permit_cost == "":
            messagebox.showerror('ERROR', 'All fields are required')
            return False
        else:
            try:
                isinstance(int(self.leader_age), int)
                isinstance(int(self.member_age), int)
            except ValueError:
                messagebox.showerror('ERROR', 'only numbers are allowed')
                return False

        if self.permit_classes.add_permit(self.name_of_peak, self.height, self.climbing_period,
                                          self.trekking_route, self.leader_name, self.leader_country,
                                          self.leader_passport_no, self.leader_age, self.leader_sex,
                                          self.member_name, self.member_country, self.member_passport_no,
                                          self.member_age, self.member_sex, self.total_climber,
                                          self.name_of_trekking_company, self.name_of_guide,
                                          self.guide_reg, self.permit_date, self.permit_cost):
            messagebox.showinfo('Permit', 'Permit added successfully')
            self.clear_permit()
            self.show_items_in_tree()
        else:
            messagebox.showerror('Error', 'Student not added')

    def get_interface_value(self):
        self.name_of_peak = self.name_of_peak_entry.get()
        self.height = self.height_entry.get()
        self.climbing_period = self.climbing_period_entry.get()
        self.trekking_route = self.trekking_route_entry.get()
        self.leader_name = self.leader_name_entry.get()
        self.leader_country = self.leader_country_entry.get()
        self.leader_passport_no = self.leader_passport_no_entry.get()
        self.leader_age = self.leader_age_entry.get()
        self.leader_sex = self.leader_sex_combo.get()
        self.member_name = self.member_name_entry.get()
        self.member_country = self.member_country_entry.get()
        self.member_passport_no = self.member_passport_no_entry.get()
        self.member_age = self.member_age_entry.get()
        self.member_sex = self.member_sex_combo.get()
        self.total_climber = self.member_total_entry.get()
        self.name_of_trekking_company = self.member_trekking_agency_entry.get()
        self.name_of_guide = self.member_guide_entry.get()
        self.guide_reg = self.member_guide_reg_entry.get()
        self.permit_date = self.permit_date_entry.get()
        self.permit_cost = self.permit_cost_entry.get()

    def show_items_in_tree(self):
        data = self.permit_classes.permit_detail()

        self.permit_info_tree.delete(*self.permit_info_tree.get_children())

        for detail in data:
            self.permit_info_tree.insert("", 'end', text=detail[0],
                                         values=(detail[1], detail[2], detail[3],
                                                 detail[4], detail[5], detail[6],
                                                 detail[7], detail[8], detail[9],
                                                 detail[10], detail[11],
                                                 detail[12], detail[13],
                                                 detail[14], detail[15],
                                                 detail[16], detail[17],
                                                 detail[18], detail[19],
                                                 detail[20]))
        self.permit_info_tree.bind("<Double-1>", self.select_data)

    def select_data(self, event):
        self.selected_row = self.permit_info_tree.selection()[0]
        self.update_index = self.permit_info_tree.item(self.selected_row, 'text')
        self.selected_value = self.permit_info_tree.item(self.selected_row,
                                                         'values')

        self.name_of_peak_entry.delete(0, END)
        self.name_of_peak_entry.insert(0, self.selected_value[0])

        self.height_entry.delete(0, END)
        self.height_entry.insert(0, self.selected_value[1])

        self.climbing_period_entry.delete(0, END)
        self.climbing_period_entry.insert(0, self.selected_value[2])

        self.trekking_route_entry.delete(0, END)
        self.trekking_route_entry.insert(0, self.selected_value[3])

        self.leader_name_entry.delete(0, END)
        self.leader_name_entry.insert(0, self.selected_value[4])

        self.leader_country_entry.delete(0, END)
        self.leader_country_entry.insert(0, self.selected_value[5])

        self.leader_passport_no_entry.delete(0, END)
        self.leader_passport_no_entry.insert(0, self.selected_value[6])

        self.leader_age_entry.delete(0, END)
        self.leader_age_entry.insert(0, self.selected_value[7])

        self.leader_sex_combo.set("")
        self.leader_sex_combo.insert(0, self.selected_value[8])

        self.member_name_entry.delete(0, END)
        self.member_name_entry.insert(0, self.selected_value[9])

        self.member_country_entry.delete(0, END)
        self.member_country_entry.insert(0, self.selected_value[10])

        self.member_passport_no_entry.delete(0, END)
        self.member_passport_no_entry.insert(0, self.selected_value[11])

        self.member_age_entry.delete(0, END)
        self.member_age_entry.insert(0, self.selected_value[12])

        self.member_sex_combo.set("")
        self.member_sex_combo.insert(0, self.selected_value[13])

        self.member_total_entry.delete(0, END)
        self.member_total_entry.insert(0, self.selected_value[14])

        self.member_trekking_agency_entry.delete(0, END)
        self.member_trekking_agency_entry.insert(0, self.selected_value[15])

        self.member_guide_entry.delete(0, END)
        self.member_guide_entry.insert(0, self.selected_value[16])

        self.member_guide_reg_entry.delete(0, END)
        self.member_guide_reg_entry.insert(0, self.selected_value[17])

        self.permit_date_entry.delete(0, END)
        self.permit_date_entry.insert(0, self.selected_value[18])

        self.permit_cost_entry.delete(0, END)
        self.permit_cost_entry.insert(0, self.selected_value[19])

    def search_permit(self):
        option = self.search_option_combo.get()
        value = self.search_value_entry.get()
        if option == "" or value == "":
            messagebox.showerror('ERROR', 'ALL Fields ARE REQUIRED', parent=self.window)
            return False

        else:
            data = self.permit_classes.search_permit(option,
                                                     value)
            self.permit_info_tree.delete(*self.permit_info_tree.get_children())
            if len(data) >= 1:
                for detail in data:
                    self.permit_info_tree.insert("", 'end', text=detail[0],
                                                 values=(detail[1], detail[2],
                                                         detail[3], detail[4],
                                                         detail[5], detail[6],
                                                         detail[7], detail[8],
                                                         detail[9], detail[10],
                                                         detail[11], detail[12],
                                                         detail[13], detail[14],
                                                         detail[15], detail[16],
                                                         detail[17], detail[18],
                                                         detail[19], detail[20]))

                    self.permit_info_tree.bind("<Double-1>", self.select_data)
            else:
                messagebox.showerror('ERROR', 'FIELD NOT FOUND')

    def search_clear(self):
        self.search_option_combo.set("")
        self.search_value_entry.delete(0, END)

    def show_all(self):
        self.show_items_in_tree()

    def delete_permit(self):
        if self.update_index == "":
            messagebox.showerror("ERROR", "Select first in order to delete permit detail", parent=self.window)
            return False

        if self.permit_classes.delete_permit(int(self.update_index)):
            messagebox.showinfo('DELETE', 'Data deleted successfully', parent=self.window)
            self.clear_permit()
            self.show_items_in_tree()
            self.update_index = ""
        else:
            messagebox.showerror('ERROR', 'Deletion failed', parent=self.window)
            return False

    def update_permit(self):
        self.get_interface_value()
        if self.update_index == "":
            messagebox.showerror('ERROR', 'Select Item first inorder to'
                                          ' update', parent=self.window)
            return False

        if self.name_of_peak == "" or self.height == "" or self.climbing_period == "" \
                or self.trekking_route == "" or self.leader_name == "" or \
                self.leader_country == "" or self.leader_passport_no == "" \
                or self.leader_age == "" or self.leader_sex == "" or self.member_name \
                == "" or self.member_country == "" or self.member_passport_no == "" \
                or self.member_age == "" or self.member_sex == "" or \
                self.total_climber == "" or self.name_of_trekking_company == "" \
                or self.name_of_guide == "" or self.guide_reg == "" or self.permit_date == "" or self.permit_cost:
            messagebox.showerror('ERROR', 'All fields are required')
            return False

        else:
            try:
                isinstance(int(self.leader_age), int)
                isinstance(int(self.member_age), int)
            except ValueError:
                messagebox.showerror('ERROR', 'only numbers are allowed')
                return

        if self.permit_classes.update_permit(self.name_of_peak, self.height, self.climbing_period,
                                             self.trekking_route, self.leader_name, self.leader_country,
                                             self.leader_passport_no, self.leader_age, self.leader_sex,
                                             self.member_name, self.member_country, self.member_passport_no,
                                             self.member_age, self.member_sex, self.total_climber,
                                             self.name_of_trekking_company, self.name_of_guide,
                                             self.guide_reg, self.permit_date, self.permit_cost, self.update_index):
            messagebox.showinfo('Permit', 'Permit Updated successfully')
            self.clear_permit()
            self.show_items_in_tree()
            self.update_index = ""
        else:
            messagebox.showerror('Error', 'Permit not updated')

    def generate_bill(self):
        random_bill = random.randint(1000, 9000)
        self.bill = StringVar()
        self.bill.set(str(random_bill))
        data = self.permit_classes.permit_detail_for_bill(self.update_index)
        self.bill_text_area.delete('1.0', END)
        if self.update_index == "":
            messagebox.showerror('ERROR', 'Selct permit first in order to generate bill', parent=self.window)
            return False

        self.bill_text_area.insert(END, "\tPersonal Information")
        self.bill_text_area.insert(END, f"\n\nPermit Date              :{self.date}")
        self.bill_text_area.insert(END, f"\nBill no                  :{self.bill.get()}")
        self.bill_text_area.insert(END, f"\nPermit No                :{data[0][0]}")
        self.bill_text_area.insert(END, f"\nMember Name              :{data[0][10]}")
        self.bill_text_area.insert(END, f"\nMember Passport No       :{data[0][12]}")
        self.bill_text_area.insert(END, f"\nLeader Name              :{data[0][5]}")
        self.bill_text_area.insert(END, f"\nPassport Passport No     :{data[0][7]}")
        self.bill_text_area.insert(END, "\n\nCost Information")
        self.bill_text_area.insert(END, f"\n\nS.N\t\tParticulars\t\t\t"
                                        f"Amount")
        self.bill_text_area.insert(END, f"\n\n1\t\tPermit\t\t\t{data[0][20]}")
        self.bill_text_area.insert(END, f"\n2\t\tGarbage Deposit\t\t\t50000")
        self.bill_text_area.insert(END, f"\n3\t\tInsurance\t\t\t12800")
        total = (50, 000 + float(data[0][20]) + 12800)
        self.bill_text_area.insert(END, f"\n\n Total bill:   {total}")

        permit_no = data[0][0]
        permit_date = self.date
        bill_no = self.bill.get()
        member_name = data[0][10]
        member_passport_no = data[0][12]
        leader_name = data[0][5]
        leader_passport_no = data[0][7]
        permit_cost = data[0][20]
        message = messagebox.askyesno('SAVE BILL', 'Do you want to save a bill'
                                      , parent=self.window)
        if message > 0:
            try:
                self.permit_classes.add_bill(permit_no, permit_date, bill_no, member_name, member_passport_no,
                                             leader_name, leader_passport_no, permit_cost)
            except Exception as e:
                messagebox.showerror('ERROR',
                                     'Student has already paid the bill ',
                                     parent=self.window)
            else:
                bill_data = self.bill_text_area.get('1.0', END)
                file = open("Bill/" + str(self.bill.get()) + ".txt", "w")
                file.write(bill_data)
                file.close()
                messagebox.showinfo("SAVED", f"Bill No:{self.bill.get()}"
                                             f" saved successfully", parent=self.window)


if __name__ == "__main__":
    Permit()
