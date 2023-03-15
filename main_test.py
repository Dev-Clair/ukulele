import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel, askyesno, askyesnocancel
from PIL import ImageTk, Image


class Mainframe():
    def __init__(self, master):

        main_win = ttk.Frame(master, cursor='hand2')
        main_win.pack(expand=1, fill=BOTH)

        # Widget Styling
        apply_style = ttk.Style(master=main_win)
        apply_style.configure('TLabel', foreground="black",
                              font=("Bell MT", 12, "bold"))
        apply_style.configure('TEntry', foreground="black",
                              background="WhiteSmoke", font=("Bell MT", 12, "bold"), bd=2)
        apply_style.configure('TButton', foreground="violet red",
                              background="MistyRose", font=("Helvetica", 12, "bold"))

        # Create Page Title Frame
        topframe = ttk.Frame(main_win, width=950, height=250)
        topframe.pack(side=TOP, expand=0, fill=BOTH,
                      anchor=N, padx=10, pady=(5, 20))
        # Create Slider Label
        labelFrame = ttk.Frame(topframe)
        labelFrame.pack(side=LEFT, expand=1, anchor=W)
        # slider text
        self.slidertext = "UKULELE - \"The Singing Sculpture\""
        topLabel = ttk.Label(
            labelFrame, text=self.slidertext, style='TLabel')
        topLabel.config(font=("Bell MT", 30, "bold"))
        topLabel.pack(expand=1, fill=BOTH)
        # Create Admin Log-in Button
        buttonFrame = ttk.Frame(topframe)
        buttonFrame.pack(side=RIGHT, expand=1, anchor=E)
        topButton = ttk.Button(
            buttonFrame, text='Admin Log-in', cursor='hand2', style='TButton', command=self.adminlogin, state='disabled')
        topButton.pack(expand=1, fill=BOTH)

        # Create Welcome Message Frame
        midframe = ttk.Frame(main_win, width=950, height=250)
        midframe.pack(side=TOP, expand=1, fill=BOTH,
                      anchor=CENTER, padx=10)
        # First Child Frame
        firsttextFrame = ttk.Frame(midframe)
        firsttextFrame.pack(side=TOP, expand=1, anchor=CENTER)
        firstLabel = ttk.Label(
            firsttextFrame, text="WELCOME TO UKULELE!!!", style='TLabel')
        firstLabel.config(font=("Bell MT", 40, "bold"))
        firstLabel.pack(expand=1, fill=BOTH)
        # Second Child Frame
        secondtextFrame = ttk.Frame(midframe)
        secondtextFrame.pack(side=TOP, expand=1)
        secondLabel = ttk.Label(
            secondtextFrame, text="We Are Glad You Are Here", style='TLabel')
        secondLabel.config(font=("Bell MT", 25, "bold"))
        secondLabel.pack(expand=1, fill=BOTH)

        # Create Label and Survey Button Frame
        bottomframe = ttk.Frame(main_win, width=950, height=250)
        bottomframe.pack(side=BOTTOM, expand=1, fill=BOTH,
                         anchor=S, padx=10, pady=(5, 20))
        # Create Bottom Label
        bottomLabel = ttk.Label(
            bottomframe, text="Kindly Click on the Button Below to Take a Quick 60 Secs Survey", style='TLabel')
        bottomLabel.config(font=("Bell MT", 20, "bold"))
        bottomLabel.pack(side=TOP, expand=1, anchor=CENTER)
        surveyButton = ttk.Button(
            bottomframe, text="Take Survey", width=20, style='TButton', command=self.takesurvey)
        surveyButton.pack(side=TOP, expand=1, anchor=CENTER)

    def adminlogin(self):
        """
            Launches a toplevel window to take in administrative authentication details
        """
        pass

    def takesurvey(self):
        """
            Launches a top level window of the surveyform to read input from user/respondent at runtime
        """
        import surveyform
        # pass


if __name__ == "__main__":
    root = tk.Tk()
    window = Mainframe(root)
    root.title("UKULELE")
    root.geometry('1200x700+0+0')
    # root.iconimage = PhotoImage(file='images/icon_img.ico')
    # root.iconphoto(False, root.iconimage)
    root.minsize(100, 100)
    root.resizable(1, 1)
    root.mainloop()
