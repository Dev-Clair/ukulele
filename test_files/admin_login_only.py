"""
    The code contained in this file is to be imported as a top level window into Main.
    The program is basically an authentication window which,
     1. receives userinput - username and password
     2. grants access to the server side of the application - Backend GUI
"""


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel


class _window():
    def __init__(self, master):
        """
            contains username and password label and entry widgets
            The submit button is will not submit any information unless correct information has been provided into the fileds
        """
        self.master = master
        self.master.title('Admin Log-in')
        self.master.geometry("350x350+325+100")
        self.master.resizable(0, 0)
        self.master.iconimage = PhotoImage(file='pic/icon_img.ico')
        self.master.iconphoto(True, self.master.iconimage)
        self.master.minsize(100, 100)
        self.master.resizable(0, 0)

        # Widget Styling
        apply_style = ttk.Style(master)
        apply_style.configure('TLabel', foreground="black",
                              font=("Helvetica", 10, "bold"))
        apply_style.configure('TEntry', foreground="blue",
                              background="WhiteSmoke", font=("Helvetica", 12, "normal"))
        apply_style.configure('TButton', foreground="blue",
                              background="MistyRose", font=("Helvetica", 10, "bold"))
        apply_style.configure('TRadiobutton', foreground="blue",
                              font=("times new roman", 10, "bold"))
        apply_style.configure('TMenubutton', foreground="blue",
                              font=("Helvetica", 10, "bold"))
        # apply_style.configure('TLabelFrame', foreground="violet red",
        #                       font=("Helvetica", 10, "bold"))
        apply_style.configure('TSeparator', foreground="black")

        self.admin_img = PhotoImage(
            file='pic/person_imgL.png')
        self.login_img = ttk.Label(
            master, image=self.admin_img, justify=CENTER)
        self.login_img.grid(row=0, columnspan=2, padx=2, pady=10)
        # create Label Widgets
        self.usernamelabel = ttk.Label(
            master, text="Username:", style='TLabel')
        self.usernamelabel.grid(row=1, column=0, padx=2, pady=10)
        self.passwordlabel = ttk.Label(
            master, text="Password:", style='TLabel')
        self.passwordlabel.grid(row=2, column=0, padx=2, pady=10)
        # Create Entry Widgets
        self.uservar = tk.StringVar()
        self.usernameentry = ttk.Entry(
            master, textvariable=self.uservar, width=40, justify=CENTER)
        self.usernameentry.grid(row=1, column=1, padx=2, pady=10)
        self.passvar = tk.StringVar()
        self.passwordentry = ttk.Entry(
            master, textvariable=self.passvar, width=40, justify=CENTER, show="*")
        self.passwordentry.grid(row=2, column=1, padx=2, pady=10)
        # Create log-in Button
        self.logbutton = ttk.Button(
            master, text="Log-in", command=self.adlog, style='TButton')
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


if __name__ == "__main__":
    root = tk.Toplevel()
    window = _window(root)
    root.mainloop()
