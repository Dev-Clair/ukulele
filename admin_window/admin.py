import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel
from tkcalendar import Calendar
from PIL import ImageTk, Image
# from database.form_database import submitform  # Import -sqlite3- Database


class Mainframe:
    def __init__(self, master):
        self.master = master
        self.master.title("UKULELE - Admin Window")
        self.master.geometry('1350x680+5+5')
        self.master.iconimage = PhotoImage(file='images/icon_img.ico')
        self.master.iconphoto(True, self.master.iconimage)
        self.master.minsize(100, 100)
        self.master.resizable(0, 0)

        # Widget Styling
        apply_style = ttk.Style(master)
        apply_style.configure('TFrame', background="light grey")
        apply_style.configure('TLabel', foreground="black", background="light grey",
                              font=("Bell MT", 12, "bold"))
        apply_style.configure('TEntry', foreground="blue",
                              background="WhiteSmoke", font=("Helvetica", 12, "normal"))
        apply_style.configure('TButton', foreground="blue",
                              background="MistyRose", font=("Helvetica", 10, "bold"))
        apply_style.configure('TRadiobutton', foreground="blue",
                              font=("times new roman", 10, "bold"))
        apply_style.configure('TMenubutton', foreground="blue", background="light grey",
                              font=("Helvetica", 10, "bold"))
        # apply_style.configure('TLabelFrame', foreground="violet red",
        #                       font=("Helvetica", 10, "bold"))
        apply_style.configure('TSeparator', background="light grey")

      # Create Page Top Frame
        topframe = ttk.Frame(master)
        topframe.pack(side=TOP, fill=X, anchor=NW, padx=1, pady=1)
        # Top Label
        slidertext = 'UKULELE - \"The Singing Sculpture\"'  # Slider Text
        self.topLabel = ttk.Label(
            topframe, text=slidertext, style='TLabel')
        self.topLabel.config(font=("Bell MT", 30, "bold"))
        self.topLabel.pack(side=LEFT, anchor=W, padx=5)
        # Database Button
        self.databaseButton = ttk.Menubutton(
            topframe, text='Database', cursor='hand2', direction="flush", style='TMenubutton')
        self.databaseButton.pack(side=RIGHT, anchor=E, padx=(20, 50))
        # Configure Database Menubutton
        self.databaseButton.menu = tk.Menu(
            self.databaseButton, tearoff=False, cursor='hand2')
        self.databaseButton["menu"] = self.databaseButton.menu
        self.databaseButton.menu.add_command(
            label="Connect Database", command=self.connectdb)
        self.databaseButton.menu.add_command(
            label="Upload Database", command=self.uploaddb)
        # Export Button
        self.exportButton = ttk.Menubutton(
            topframe, text='export', cursor='hand2', direction="flush", style='TMenubutton')
        self.exportButton.pack(side=RIGHT, anchor=E, padx=(20, 50))
        # Configure Export Menubutton
        # self.exportButton.menu = tk.Menu(
        #     self.exportButton, tearoff=False, cursor='hand2')
        # self.exportButton["menu"] = self.exportButton.menu
        # self.exportButton.menu.add_command(label="Current Selection")
        # self.exportButton.menu.add_command(label="All")

        # self.exportButton.submenu = tk.Menu(
        #     self.exportButton)
        # # self.exportButton["submenu"] = self.exportButton.submenu
        # self.exportButton.submenu.add_command(
        #     label="Export as excel", command=self.exportexcel)
        # self.exportButton.submenu.add_command(
        #     label="Export as csv", command=self.exportcsv)
        # self.exportButton.submenu.add_command(
        #     label="Export as XML", command=self.exportxml)
        # self.exportButton.add_cascade(
        #     label="Current Selection", menu=self.exportButton.submenu)

        # self.exportButton.submenu = tk.Menu(self.exportButton)
        # self.exportButton["submenu"] = self.exportButton.submenu
        # self.exportButton.submenu.add_command(label="Export as excel", command=self.exportexcel)
        # self.exportButton.submenu.add_command(label="Export as csv", command=self.exportcsv)
        # self.exportButton.submenu.add_command(label="Export as XML", command=self.exportxml)
        # self.exportButton.add_cascade(label = "All", menu = self.exportButton.submenu)

      # Create LEFT Frame
        leftframe = ttk.Frame(master, width=450)
        leftframe.pack(side=LEFT, expand=1, fill=BOTH,
                       anchor=NW, padx=1, pady=1)

      # Create Page Top Frame
        rightframe = ttk.Frame(master, width=900)
        rightframe.pack(side=RIGHT, expand=1, fill=BOTH,
                        anchor=NE, padx=1, pady=1)

    def connectdb(self):
        pass

    def uploaddb(self):
        pass

    def exportexcel(self):
        pass

    def exportcsv(self):
        pass

    def exportxml(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    window = Mainframe(root)
    root.mainloop()
