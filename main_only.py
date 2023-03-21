import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel, askyesno, askyesnocancel
from PIL import ImageTk, Image


class Mainframe:
    def __init__(self, master):

        self.master = master
        self.master.title("UKULELE")
        self.master.geometry('1300x700+0+0')
        self.master.iconimage = PhotoImage(file='images/icon_img.ico')
        self.master.iconphoto(True, root.iconimage)
        self.master.minsize(100, 100)
        self.master.resizable(0, 0)

        # Widget Styling
        apply_style = ttk.Style(master)
        apply_style.configure('TLabel', foreground="black",
                              font=("Bell MT", 12, "bold"))
        apply_style.configure('TEntry', foreground="blue",
                              background="WhiteSmoke", font=("Bell MT", 12, "bold"), bd=2)
        apply_style.configure('TButton', foreground="blue",
                              background="MistyRose", font=("Helvetica", 12, "bold"))

        # Create Page Top Frame
        topframe = ttk.Frame(master)
        topframe.pack(side=TOP, fill=X, anchor=NW)
        # Top Label
        slidertext = 'UKULELE - \"The Singing Sculpture\"'  # Slider Text
        self.topLabel = ttk.Label(
            topframe, text=slidertext, style='TLabel')
        self.topLabel.config(font=("Bell MT", 30, "bold"))
        self.topLabel.pack(side=LEFT, anchor=NW, padx=5)
        # Admin Log-in Button
        self.topButton = ttk.Button(
            topframe, text='Admin Log-in', cursor='hand2', style='TButton', command=self.adminlogin)
        self.topButton.pack(side=RIGHT, anchor=NE, padx=5)

        # Create Welcome Message Frame
        midframe = ttk.Frame(master)
        midframe.pack(side=TOP, expand=1, fill=X, anchor=CENTER, pady=20)
        # First Child Label
        self.firstLabel = ttk.Label(
            midframe, text="WELCOME TO UKULELE!!!", style='TLabel')
        self.firstLabel.config(font=("Bell MT", 40, "bold"))
        self.firstLabel.pack(side=TOP, anchor=CENTER, pady=20)
        # Second Child Label
        self.secondLabel = ttk.Label(
            midframe, text="We Are Glad You Are Here", style='TLabel')
        self.secondLabel.config(font=("Bell MT", 25, "bold"))
        self.secondLabel.pack(side=TOP, anchor=CENTER, pady=20)

        # Create Label and Survey Button Frame
        bottomframe = ttk.Frame(master, width=950, height=250)
        bottomframe.pack(side=BOTTOM, fill=X,
                         anchor=CENTER, pady=20)
        # Create Bottom Label
        self.bottomLabel = ttk.Label(
            bottomframe, text="Kindly Click on the Button Below to Take a Quick 60 Secs Survey", style='TLabel')
        self.bottomLabel.config(font=("Bell MT", 20, "bold"))
        self.bottomLabel.pack(side=TOP, anchor=CENTER, pady=10)
        self.surveyButton = ttk.Button(
            bottomframe, text="Take Survey", width=20, style='TButton', command=self.takesurvey)
        self.surveyButton.pack(side=TOP, anchor=CENTER, pady=10)

    # Class Functions
    def adminlogin(self):
        """
            Launches a toplevel window for administrative authentication details
        """
        self.admin_win = tk.Toplevel()
        self.admin_win.title('Admin Login')
        self.admin_win.geometry("350x350+325+100")
        self.admin_win.resizable(0, 0)

        self.admin_img = PhotoImage(
            file='images/person_imgL.png')
        self.login_img = ttk.Label(
            self.admin_win, image=self.admin_img, justify=CENTER)
        self.login_img.grid(row=0, columnspan=2, padx=2, pady=10)
        # create Label Widgets
        self.usernamelabel = ttk.Label(
            self.admin_win, text="Username:", style='TLabel')
        self.usernamelabel.grid(row=1, column=0, padx=2, pady=10)
        self.passwordlabel = ttk.Label(
            self.admin_win, text="Password:", style='TLabel')
        self.passwordlabel.grid(row=2, column=0, padx=2, pady=10)
        # Create Entry Widgets
        self.uservar = tk.StringVar()
        self.usernameentry = ttk.Entry(
            self.admin_win, textvariable=self.uservar, width=40, justify=CENTER)
        self.usernameentry.grid(row=1, column=1, padx=2, pady=10)
        self.passvar = tk.StringVar()
        self.passwordentry = ttk.Entry(
            self.admin_win, textvariable=self.passvar, width=40, justify=CENTER, show="*")
        self.passwordentry.grid(row=2, column=1, padx=2, pady=10)
        # Create log-in Button
        self.logbutton = ttk.Button(
            self.admin_win, text="Log-in", command=self.adlog, style='TButton')
        self.logbutton.grid(row=3, columnspan=2, padx=2, pady=10)

        # Direct input focus to the first entry widget of the log-in window
        self.usernameentry.focus_set()

    def adlog(self):
        """
            Allows access to serverside / admin window
        """
        if self.uservar.get() == "sponsor" and self.passvar.get() == "ukulele":
            showinfo('Welcome', 'Log-in Successful', parent=self.admin_win)
            self.admin_win.quit()
            # import adminwindow

        if self.uservar.get() != "sponsor" and self.passvar.get() != "ukulele":
            showerror("Error", "Please enter the correct log-in details",
                      parent=self.admin_win)
            self.usernameentry.delete(0, END)
            self.passwordentry.delete(0, END)
            self.usernameentry.focus_set()

        if self.uservar.get() == "" and self.passvar.get() == "":
            showerror(
                "Error", "Username or Password fields cannot be empty", parent=self.admin_win)
            self.usernameentry.focus_set()

    def takesurvey(self):
        """
            Launches a top level window of the surveyform to read input from user/respondent at runtime
        """
        pass

    # Sliding Text Function
    # def slider(self):
    #     self.count = 0
    #     self.text = ''
    #     if self.count == len(self.slidertext):
    #         self.count == 0
    #         self.text = ''
    #     self.text = self.text+self.slidertext[self.count]
    #     self.topLabel.config(text=self.text)
    #     self.count += 1
    #     self.topLabel.after(300, self.slider)


if __name__ == "__main__":
    root = tk.Tk()
    window = Mainframe(root)
    root.mainloop()
