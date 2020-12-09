from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import webbrowser


class DeveloperProfile:
    """Shows developer related information"""

    def __init__(self):
        self.window = Tk()
        self.window.title('Developer Profile')
        self.window.geometry('1350x700+0+0')
        self.window.configure(bg='white')
        self.window.resizable(False, False)

        profile_img = ImageTk.PhotoImage(Image.open("sanjiv_profile.jpg"))
        profile_label = Label(self.window, image=profile_img)
        profile_label.place(x=550, y=100)

        profile_text_1 = Label(self.window, text="Hello Guys, I'm Sanjiv Limbu", bg='white',
                               font=('helvetica', 20, 'bold'))
        profile_text_1.place(x=450, y=320)

        profile_text_2 = Label(self.window, text="I am a Python Developer", bg='white',
                               font=('helvetica', 15, 'bold'))
        profile_text_2.place(x=450, y=360)

        facebook_img = ImageTk.PhotoImage(Image.open("facebook.png"))
        facebook_button = Button(self.window, image=facebook_img, bd=0,
                                 command=self.open_facebook)
        facebook_button.place(x=450, y=440)

        instagram_img = ImageTk.PhotoImage(Image.open("instagram.png"))
        instagram_button = Button(self.window, image=instagram_img, bd=0,
                                  command=self.open_instagram)
        instagram_button.place(x=550, y=440)

        twitter_img = ImageTk.PhotoImage(Image.open("twitter.png"))
        twitter_button = Button(self.window, image=twitter_img, bd=0,
                                command=self.open_twitter)
        twitter_button.place(x=650, y=440)

        gmail_img = ImageTk.PhotoImage(Image.open("gmail.png"))
        gmail_button = Button(self.window, image=gmail_img, bd=0,
                              command=self.open_gmail)
        gmail_button.place(x=750, y=440)

        youtube_img = ImageTk.PhotoImage(Image.open("youtube.png"))
        youtube_button = Button(self.window, image=youtube_img, bd=0,
                                command=self.open_youtube)
        youtube_button.place(x=850, y=440)

        github_img = ImageTk.PhotoImage(Image.open("github.png"))
        github_button = Button(self.window, image=github_img, bd=0,
                               command=self.open_github)
        github_button.place(x=950, y=440)

        self.window.mainloop()

    def open_facebook(self):
        new = 1
        url = "https://www.facebook.com/sanjiv.limbu.92/"
        webbrowser.open(url, new=new)

    def open_instagram(self):
        new = 1
        url = "https://www.instagram.com/"
        webbrowser.open(url, new=new)

    def open_twitter(self):
        new = 1
        url = "https://twitter.com/"
        webbrowser.open(url, new=new)

    def open_gmail(self):
        new = 1
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.open(url, new=new)

    def open_github(self):
        new = 1
        url = "https://github.com/"
        webbrowser.open(url, new=new)

    def open_youtube(self):
        new = 1
        url = "https://www.youtube.com/"
        webbrowser.open(url, new=new)


if __name__ == "__main__":
    DeveloperProfile()
