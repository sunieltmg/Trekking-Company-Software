from tkinter import *
from tkinter import ttk, messagebox
from views.permit import *
from views.manage_peak import *
from views.developer_profile import *
from views.bill import *
from PIL import ImageTk, Image
import time
import webbrowser


def bill_history():
    Bill()


class System:
    def __init__(self):
        """ Performs tasks like managing peak, bill history, developer informtaion"""
        self.window = Tk()
        self.window.title('System Window')
        self.window.geometry('1350x700+0+0')
        self.window.resizable(False, False)

        title = Label(self.window,
                      text="Welcome to Adventure Everest Team Treks & Expedition Admin Panel",
                      font=('helvetica', 15, 'bold'),
                      bg="green", fg="white")
        title.place(x=300, y=10)

        self.top_frame = Frame(self.window, height=80, width=1330, bg='lightgreen')
        self.top_frame.place(x=10, y=50)

        manage_peak_button = Button(self.top_frame, text='Manage Peak', font='helvetica', bg='green', fg='white',
                                    activebackground='white', activeforeground='green',
                                    width=15, pady=5, bd=1, relief='groove', command=self.manage_peak)
        manage_peak_button.place(x=270, y=15)

        bill_history_button = Button(self.top_frame, text='Bill History', font='helvetica', bg='green', fg='white',
                                     activebackground='white', activeforeground='green',
                                     width=15, pady=5, bd=1, relief='groove', command=bill_history)
        bill_history_button.place(x=480, y=15)

        developer_information_button = Button(self.top_frame, text='Developer Information', font='helvetica',
                                              bg='green', fg='white',
                                              activebackground='white', activeforeground='green',
                                              width=18, pady=5, bd=1, relief='groove',
                                              command=self.developer_information)
        developer_information_button.place(x=690, y=15)

        exit_button = Button(self.top_frame, text='Exit', font='helvetica', bg='green', fg='white',
                             activebackground='white', activeforeground='green',
                             width=15, pady=5, bd=1, relief='groove', command=exit)
        exit_button.place(x=900, y=15)

        self.nma_peak_frame = Frame(self.window, width=410, height=400, bg='lightgreen')
        self.nma_peak_frame.place(x=10, y=200)

        title = Label(self.nma_peak_frame, text='NMA Peak', font=('helvetica', 15, 'bold'), bg='lightgreen')
        title.place(x=130, y=0)

        info_text = """            1)  Mt.Cholaste(6423m) Solukhumbhu \n
              2)  Mt.Kyazo Ri(6151m) Solukhumbhu   \n
             3)  Mt.Nirekha(6159m) Solukhmubhu    \n
            4)  Mt.Langsisa Ri(6412m) Rasuwa     \n
                  5)  Mt.Ombigaichen(6340m) Solukhumbhu\n
      6)  Mt.Bokta(6114m) Dolakha          \n
7)  Mt.Chekigo(6121m) Dolakha\n
                8)  Mt.Phari Lapcha(6017m) Solukhumbhu\n
               9)  Mt.Lobuje West(6416m) Solukhumbhu\n
10) Mt. Larkya Peak(6416) Gorkha\n
11) Mt. ABI(6043m) Solukhumbhu\n
12) Mt.Yubra Himal(6048m) Rasuwa\n
                    """
        info = Label(self.nma_peak_frame, text=info_text,
                     font=('helvetica', 9), bg='lightgreen')
        info.place(x=10, y=30)

        nma_peak_button = Button(self.nma_peak_frame, text='For Peak detail Info', command=self.open_nma_peak)
        nma_peak_button.place(x=280, y=370)

        self.nma_training_frame = Frame(self.window, width=460, height=400, bg='lightgreen')
        self.nma_training_frame.place(x=430, y=200)

        title = Label(self.nma_training_frame, text='NMA Training', font=('helvetica', 15, 'bold'), bg='lightgreen')
        title.place(x=130, y=10)

        nma_training_button = Button(self.nma_training_frame, text='For NMA training detail Info',
                                     command=self.open_nma_training, width=30)
        nma_training_button.place(x=200, y=370)

        info1_text = """                    1) Basic Mountaineering Training\n\n
                        2) Advance Mountaineering Training\n\n
           3) Mountain Leader Training\n\n
                 4) High Mountain Resue Training\n\n
        5) Mountain Guide Training"""

        info1 = Label(self.nma_training_frame, text=info1_text,
                      font=('helvetica', 11), bg='lightgreen')
        info1.place(x=10, y=60)

        self.trekking_guidance_frame = Frame(self.window, width=438, height=400, bg='lightgreen')
        self.trekking_guidance_frame.place(x=900, y=200)

        nma_trekking_guidance = Button(self.trekking_guidance_frame, text='For trekkig guidance detail Info',
                                       command=self.open_nma_trekking_guidance, width=30)
        nma_trekking_guidance.place(x=200, y=370)

        title = Label(self.trekking_guidance_frame, text='Trekking Guidance', font=('helvetica', 15, 'bold'),
                      bg='lightgreen')
        title.place(x=130, y=10)

        trekking_guidance_1 = Label(self.trekking_guidance_frame,
                                    text="Because there is no immediate and direct threat of life, it is difficult ",
                                    font=('helvetica', 11), bg='lightgreen')
        trekking_guidance_1.place(x=0, y=60)

        trekking_guidance_2 = Label(self.trekking_guidance_frame,
                                    text="to appreciate or to see the gradual diminution in the quality of life ",
                                    font=('helvetica', 11), bg='lightgreen')
        trekking_guidance_2.place(x=0, y=85)

        trekking_guidance_3 = Label(self.trekking_guidance_frame,
                                    text="caused by the innumerable acts of environmental degradation. ",
                                    font=('helvetica', 11), bg='lightgreen')
        trekking_guidance_3.place(x=0, y=110)

        self.window.mainloop()

    def open_nma_peak(self):
        new = 1
        url = "https://www.nepalmountaineering.org/article-nma_peaks"
        webbrowser.open(url, new=new)

    def open_nma_training(self):
        new = 1
        url = "https://www.nepalmountaineering.org/article-training"
        webbrowser.open(url, new=new)

    def open_nma_trekking_guidance(self):
        new = 1
        url = "https://www.nepalmountaineering.org/article-trekking_guidance"
        webbrowser.open(url, new=new)

    def manage_peak(self):
        ManagePeak()

    def exit(self):
        self.window.destroy()

    def developer_information(self):
        self.window.destroy()
        DeveloperProfile()


if __name__ == "__main__":
    System()
