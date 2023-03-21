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
        self.master.iconphoto(True, self.master.iconimage)
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
        pass

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
