from tkinter import *
from tkinter import ttk,messagebox

class Employee:
    def __init__(self):
        self.window = Tk()
        self.window.title('Employee Window')
        self.window.geometry('1350x700+0+0')
        self.window.resizable(False, False)

        title = Label(self.window,
                      text="Welcome to Adventure Everest Team Treks & Expedition \t\t|Employee Panel",
                      font=('helvetica', 15, 'bold'),
                      bg="green", fg="white")
        title.pack(fill=BOTH)

        self.window.mainloop()