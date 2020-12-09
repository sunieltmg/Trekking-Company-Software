from tkinter import *
from tkinter import ttk, messagebox
from classes.login_register_classes import *


class Bill:
    """ Performs tasks like generating permit bill"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Bill History')
        self.window.geometry('1350x650+0+0')
        self.window.resizable(False, False)
        self.permit_classes = PermitClasses()

        title = Label(self.window,
                      text="Welcome to Adventure Everest Team Treks\n&\nExpedition\nBilling History Section",
                      font=('helvetica', 15, 'bold'))
        title.place(x=400, y=30)

        self.bill_history_frame = LabelFrame(self.window, text='Bill Details')
        self.bill_history_frame.place(x=0, y=150, width=1350, height=495)

        self.scroll_x = ttk.Scrollbar(self.bill_history_frame, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(self.bill_history_frame, orient=VERTICAL)
        self.bill_detail_tree = ttk.Treeview(self.bill_history_frame, column=('permit_no',
                                                                              'permit_date', 'bill_no',
                                                                              'member_name', 'member_passport_no',
                                                                              'leader_name', 'leader_passport_no',
                                                                              'permit_cost', 'garbage_deposit',
                                                                              'insurance'))

        self.scroll_x.config(command=self.bill_detail_tree.xview)
        self.scroll_y.config(command=self.bill_detail_tree.yview)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.bill_detail_tree.config(xscrollcommand=self.scroll_x.set,
                                     yscrollcommand=self.scroll_y.set)

        self.bill_detail_tree['show'] = 'headings'
        self.bill_detail_tree.heading('permit_no', text='Permit No')
        self.bill_detail_tree.heading('permit_date', text='Permit Date')
        self.bill_detail_tree.heading('member_name', text='Member Name')
        self.bill_detail_tree.heading('member_passport_no', text='Member Passport No')
        self.bill_detail_tree.heading('leader_name', text='Leader Name')
        self.bill_detail_tree.heading('leader_passport_no', text='Leader Passport No')
        self.bill_detail_tree.heading('permit_cost', text='Permit Cost')
        self.bill_detail_tree.heading('garbage_deposit', text='Garbage Deposit')
        self.bill_detail_tree.heading('insurance', text='Insurance')
        self.bill_detail_tree.pack(fill=BOTH, expand=1)

        self.show_items_in_tree()
        self.window.mainloop()

    def show_items_in_tree(self):
        data = self.permit_classes.show_bill()
        self.bill_detail_tree.delete(*self.bill_detail_tree.get_children())

        for detail in data:
            self.bill_detail_tree.insert("", 'end', text=detail[0],
                                         values=(detail[0], detail[1], detail[2], detail[3],
                                                 detail[4], detail[5], detail[6],
                                                 detail[7], detail[8], detail[9]))


if __name__ == "__main__":
    Bill()
