import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo


class Mainframe:
    def __init__(self, master):
        self.master = master
        self.master.title("UKULELE")
        self.master.geometry('1350x680+5+5')
        # self.master.iconimage = PhotoImage(file='pic\icon_img.png')
        # self.master.iconphoto(True, self.master.iconimage)
        self.master.minsize(100, 100)
        self.master.resizable(0, 0)

        # Widget Styling
        apply_style = ttk.Style(master)
        apply_style.configure('TFrame', backround="blue")
        apply_style.configure('TLabel', foreground="black",
                              font=("Bell MT", 12, "bold"))
        apply_style.configure('TEntry', foreground="blue",
                              background="WhiteSmoke", font=("Helvetica", 12, "normal"))
        apply_style.configure('TButton', foreground="blue",
                              background="MistyRose", font=("Helvetica", 10, "bold"))

        # Create Top Label
        self.slidertext = 'UKULELE - \"The Singing Sculpture\"'  # Slider Text
        self.topLabel = ttk.Label(
            master, text=self.slidertext, style='TLabel')
        self.topLabel.config(font=("Bell MT", 30, "bold"))
        self.topLabel.pack(side=TOP, anchor=W, padx=5)
        # self.slider()

        # Create Log-in Frame
        login_win = ttk.Frame(master, relief=FLAT, style='TFrame')
        login_win.place(x=450, y=150, width=350, height=350)
        # Create Image Label
        self.top_img = PhotoImage(file='pic\person_imgL.png')
        self.login_img = ttk.Label(
            login_win, image=self.top_img, justify=CENTER)
        self.login_img.grid(row=0, columnspan=2, padx=2, pady=10)
        # Create Label Widgets
        self.sponsorlabel = ttk.Label(
            login_win, text="Sponsor Id:", style='TLabel', justify=LEFT)
        self.sponsorlabel.grid(row=1, column=0, padx=2, pady=10)
        self.passwordlabel = ttk.Label(
            login_win, text="Password:", style='TLabel', justify=LEFT)
        self.passwordlabel.grid(row=2, column=0, padx=2, pady=10)
        self.forgetlabel = ttk.Label(
            login_win, text="forgot password? default password is \"ukulele\" in lowercase", style='TLabel', justify=LEFT)
        self.forgetlabel.config(font=("times", 8, "normal"))
        self.forgetlabel.grid(row=3, columnspan=2, padx=2, pady=(1, 2))
        # Create Entry Widgets
        self.sponsorvar = tk.StringVar()
        self.sponsorentry = ttk.Entry(
            login_win, textvariable=self.sponsorvar, width=40, justify=CENTER)
        self.sponsorentry.grid(row=1, column=1, padx=2, pady=10)
        self.passvar = tk.StringVar()
        self.passwordentry = ttk.Entry(
            login_win, textvariable=self.passvar, width=40, justify=CENTER, show="*")
        self.passwordentry.grid(row=2, column=1, padx=2, pady=10)
        # Create Log-in Button
        self.logbutton = ttk.Button(
            login_win, text="Log-in", command=self.adlog, style='TButton')
        self.logbutton.grid(row=4, columnspan=2, padx=2, pady=10)

        # Direct input focus to sponsor entryfield
        self.sponsorentry.focus_set()

        # Create Copyright Label
        self.cpyrightLabel = ttk.Label(
            master, text="© Copyright 2023 | Lexi-Clair Designs", style='TLabel')
        self.cpyrightLabel.config(font=("times new roman", 8, "bold"))
        self.cpyrightLabel.config(foreground="blue")
        self.cpyrightLabel.config(background="light grey")
        self.cpyrightLabel.pack(side=BOTTOM, fill=X,
                                anchor=W, pady=(10, 0))

    # Sponsor Login Function
    def adlog(self):
        """
            Allows access to database window
        """
        if self.sponsorvar.get() != "sponsor" and self.passvar.get() != "ukulele":
            showerror("Error", "Please enter the correct log-in details")
            self.sponsorentry.delete(0, END)
            self.passwordentry.delete(0, END)
            # Direct input focus to sponsor entryfield
            self.sponsorentry.focus_set()
        else:
            showinfo('Welcome', 'Log-in Successful')


if __name__ == "__main__":
    root = tk.Tk()
    window = Mainframe(root)
    root.mainloop()
