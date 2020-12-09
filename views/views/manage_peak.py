from tkinter import *
from tkinter import ttk, messagebox
from classes.login_register_classes import *


class ManagePeak:
    """ Performs tasks like managing peak"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Manage Peak')
        self.window.geometry('1350x700+0+0')
        self.window.resizable(False, False)
        self.peak_classes = PeakClasses()
        self.admin_classes = AdminClasses()
        self.update_index = ""

        title = Label(self.window,
                      text="Welcome to Adventure Everest Team Treks & Expedition \t\t|Manage Peak",
                      font=('helvetica', 15, 'bold'),
                      bg="green", fg="white")
        title.pack(fill=BOTH)

        manage_peak_title = Label(self.window,
                                  text=" Manage Peak",
                                  font=('helvetica', 15, 'bold'))
        manage_peak_title.place(x=600, y=50)

        self.search_frame = Frame(self.window, width=920, height=50, bg='lightgray')
        self.search_frame.place(x=200, y=100)

        search_title = Label(self.search_frame, text='Sarch By:', font=('helvetica', 15, 'bold'),
                             fg='black',
                             bg='lightgray')
        search_title.place(x=10, y=5)

        self.search_option_combo = ttk.Combobox(self.search_frame, font=('helvetica', 10, 'bold'), width=23)
        self.search_option_combo.place(x=130, y=5)
        self.search_option_combo['values'] = ['peak_name', 'district', 'himalayan_range']

        self.search_value_entry = Entry(self.search_frame, font=('helvetica', 10, 'bold'), width=25)
        self.search_value_entry.place(x=350, y=5)

        search_button = Button(self.search_frame, text='Search', font='helvetica', bg='green', fg='white',
                               activebackground='white', activeforeground='green',
                               width=10, pady=5, bd=1, relief='groove', command=self.search_peak)
        search_button.place(x=550, y=5)

        clear_button = Button(self.search_frame, text='Clear', font='helvetica', bg='green', fg='white',
                              activebackground='white', activeforeground='green',
                              width=10, pady=5, bd=1, relief='groove', command=self.search_clear)
        clear_button.place(x=680, y=5)

        show_all_button = Button(self.search_frame, text='Show all', font='helvetica', bg='green', fg='white',
                                 activebackground='white', activeforeground='green',
                                 width=10, pady=5, bd=1, relief='groove', command=self.show_all)
        show_all_button.place(x=810, y=5)

        self.right_frame = Frame(self.window, height=520, width=500, bg='lightgreen')
        self.right_frame.place(x=5, y=170)

        peak_detail_label = Label(self.right_frame, text='Peak Details', font=('helvetica', 15, 'bold'),
                                  bg='lightgreen')
        peak_detail_label.place(x=170, y=10)

        peak_name_label = Label(self.right_frame, text='Peak Name', font=('helvetica', 15), bg='lightgreen')
        peak_name_label.place(x=170, y=80)
        self.peak_name_entry = Entry(self.right_frame, font=('helvetica', 15))
        self.peak_name_entry.place(x=100, y=115)

        height_label = Label(self.right_frame, text='Height', font=('helvetica', 15), bg='lightgreen')
        height_label.place(x=170, y=150)
        self.height_entry = Entry(self.right_frame, font=('helvetica', 15))
        self.height_entry.place(x=100, y=185)

        himalayan_range_label = Label(self.right_frame, text='Himalayan Range', font=('helvetica', 15), bg='lightgreen')
        himalayan_range_label.place(x=130, y=220)
        self.himalayan_range_entry = Entry(self.right_frame, font=('helvetica', 15))
        self.himalayan_range_entry.place(x=100, y=255)

        district_label = Label(self.right_frame, text='District', font=('helvetica', 15), bg='lightgreen')
        district_label.place(x=170, y=290)
        self.district_entry = Entry(self.right_frame, font=('helvetica', 15))
        self.district_entry.place(x=100, y=325)

        caravan_route_label = Label(self.right_frame, text='Caravan Route', font=('helvetica', 15), bg='lightgreen')
        caravan_route_label.place(x=130, y=360)
        self.caravan_route_text = Text(self.right_frame, font=('helvetica', 10), width=30, height=3)
        self.caravan_route_text.place(x=100, y=395)

        add_button = Button(self.right_frame, text='Add', font='helvetica', bg='green', fg='white',
                            activebackground='white', activeforeground='green',
                            width=10, pady=5, bd=1, relief='groove', command=self.add_peak_detail)
        add_button.place(x=20, y=470)

        update_button = Button(self.right_frame, text='Update', font='helvetica', bg='green', fg='white',
                               activebackground='white', activeforeground='green',
                               width=10, pady=5, bd=1, relief='groove', command=self.update_peak_detail)
        update_button.place(x=130, y=470)

        delete_button = Button(self.right_frame, text='Delete', font='helvetica', bg='green', fg='white',
                               activebackground='white', activeforeground='green',
                               width=10, pady=5, bd=1, relief='groove', command=self.delete_peak_detail)
        delete_button.place(x=240, y=470)

        clear_button = Button(self.right_frame, text='Clear', font='helvetica', bg='green', fg='white',
                              activebackground='white', activeforeground='green',
                              width=10, pady=5, bd=1, relief='groove', command=self.clear_peak_detail)
        clear_button.place(x=350, y=470)

        self.peak_detail_tree = LabelFrame(self.window, text='Peak Detail', bg='lightgray')
        self.peak_detail_tree.place(x=510, y=170, width=840, height=520)

        self.scroll_x = ttk.Scrollbar(self.peak_detail_tree, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(self.peak_detail_tree, orient=VERTICAL)
        self.peak_detail_tree = ttk.Treeview(self.peak_detail_tree,
                                             column=('peak_name',
                                                     'height',
                                                     'himalayan_range',
                                                     'district',
                                                     'caravan_route'))

        self.scroll_x.config(command=self.peak_detail_tree.xview)
        self.scroll_y.config(command=self.peak_detail_tree.yview)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.peak_detail_tree.config(xscrollcommand=self.scroll_x.set,
                                     yscrollcommand=self.scroll_y.set)

        self.peak_detail_tree['show'] = 'headings'
        self.peak_detail_tree.heading('peak_name', text='Peak Name')
        self.peak_detail_tree.heading('height', text='Height')
        self.peak_detail_tree.heading('himalayan_range', text='Himalayan Range')
        self.peak_detail_tree.heading('district', text='District')
        self.peak_detail_tree.heading('caravan_route', text='Caravan Route')
        self.peak_detail_tree.pack(fill=BOTH, expand=1)
        self.show_items_in_tree()

        self.window.mainloop()

    def add_peak_detail(self):
        peak_name = self.peak_name_entry.get()
        height = self.height_entry.get()
        himalayan_range = self.himalayan_range_entry.get()
        district = self.district_entry.get()
        caravan_route = self.caravan_route_text.get("1.0", END)

        if peak_name == "" or height == "" or himalayan_range == "" or district == "" or caravan_route == "":
            messagebox.showerror('ERROR', 'All fields are required', parent=self.window)
            return False

        elif self.peak_classes.add_peak_detail(peak_name, height, himalayan_range, district, caravan_route):
            messagebox.showinfo('ADD', 'Peak detail is added successfully', parent=self.window)
            self.show_items_in_tree()

    def clear_peak_detail(self):
        self.peak_name_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.himalayan_range_entry.delete(0, END)
        self.district_entry.delete(0, END)
        self.caravan_route_text.delete("1.0", END)

    def show_items_in_tree(self):
        data = self.peak_classes.peak_detail()

        self.peak_detail_tree.delete(*self.peak_detail_tree.get_children())

        for detail in data:
            self.peak_detail_tree.insert("", 'end', text=detail[0],
                                         values=(detail[1], detail[2], detail[3],
                                                 detail[4], detail[5]))
        self.peak_detail_tree.bind("<Double-1>", self.select_data)

    def select_data(self, event):
        self.selected_row = self.peak_detail_tree.selection()[0]
        self.update_index = self.peak_detail_tree.item(self.selected_row, 'text')
        self.selected_value = self.peak_detail_tree.item(self.selected_row,
                                                         'values')
        self.peak_name_entry.delete(0, END)
        self.peak_name_entry.insert(0, self.selected_value[0])

        self.height_entry.delete(0, END)
        self.height_entry.insert(0, self.selected_value[1])

        self.himalayan_range_entry.delete(0, END)
        self.himalayan_range_entry.insert(0, self.selected_value[2])

        self.district_entry.delete(0, END)
        self.district_entry.insert(0, self.selected_value[3])

        self.caravan_route_text.delete("1.0", END)
        self.caravan_route_text.insert("1.0", self.selected_value[4])

    def update_peak_detail(self):
        peak_name = self.peak_name_entry.get()
        height = self.height_entry.get()
        himalayan_range = self.himalayan_range_entry.get()
        district = self.district_entry.get()
        caravan_route = self.caravan_route_text.get("1.0", END)
        if self.update_index == "":
            messagebox.showerror('ERROR', 'Select Item first inorder to'
                                          ' update', parent=self.window)
            return False

        if peak_name == "" or height == "" or himalayan_range == "" \
                or district == "" or caravan_route == "":
            messagebox.showerror('ERROR', 'All fields are required', parent=self.window)
            return False

        if self.peak_classes.update_peak_detail(peak_name, height, himalayan_range, district, caravan_route,
                                                int(self.update_index)):
            messagebox.showinfo('UPDATE', 'Data updated successfully', parent=self.window)
            self.clear_peak_detail()
            self.show_items_in_tree()
            self.update_index = ""
        else:
            messagebox.showerror('ERROR', 'Updation failed', parent=self.window)
            return False

    def delete_peak_detail(self):
        if self.update_index == "":
            messagebox.showerror('ERROR', 'Select Item first inorder to'
                                          ' update', parent=self.window)
            return False

        if self.peak_classes.delete_peak_detail(int(self.update_index)):
            messagebox.showinfo('DELETE', 'Data deleted successfully', parent=self.window)
            self.clear_peak_detail()
            self.show_items_in_tree()
            self.update_index = ""
        else:
            messagebox.showerror('ERROR', 'Deletion failed', parent=self.window)
            return False

    def search_peak(self):
        option = self.search_option_combo.get()
        value = self.search_value_entry.get()
        if option == "" or value == "":
            messagebox.showerror('ERROR', 'ALL Fields ARE REQUIRED', parent=self.window)
            return False

        else:
            data = self.peak_classes.search_peak(option, value)
            self.peak_detail_tree.delete(*self.peak_detail_tree.get_children())
            if len(data) >= 1:
                for detail in data:
                    self.peak_detail_tree.insert("", 'end', text=detail[0],
                                                 values=(detail[1], detail[2],
                                                         detail[3], detail[4],
                                                         detail[5]))

                    self.peak_detail_tree.bind("<Double-1>", self.select_data)
            else:
                messagebox.showerror('ERROR', 'FIELD NOT FOUND')

    def search_clear(self):
        self.search_option_combo.set("")
        self.search_value_entry.delete(0, END)

    def show_all(self):
        self.show_items_in_tree()


if __name__ == "__main__":
    ManagePeak()
