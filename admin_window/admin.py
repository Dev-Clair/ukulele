import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel
from tkcalendar import Calendar
from PIL import ImageTk, Image
# from database.form_database import addrecord  # Import -sqlite3- Database


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
        apply_style.configure('TFrame')
        apply_style.configure('TLabel', foreground="black",
                              font=("Bell MT", 12, "bold"))
        apply_style.configure('TEntry', foreground="blue",
                              background="WhiteSmoke", font=("Helvetica", 12, "normal"))
        apply_style.configure('TButton', foreground="blue",
                              background="MistyRose", font=("Helvetica", 10, "bold"))
        apply_style.configure('TRadiobutton', foreground="blue",
                              font=("times new roman", 10, "bold"))
        apply_style.configure('TMenubutton', foreground="blue",
                              font=("Helvetica", 10, "bold"))
        # apply_style.configure('TLabelframe', foreground="violet red",
        #                       font=("Helvetica", 10, "bold"))
        apply_style.configure(
            'TSeparator', foreground="blue", background="blue")

      # Create Title Label
        slidertext = 'UKULELE - \"The Singing Sculpture\"'  # Slider Text
        self.topLabel = ttk.Label(
            master, text=slidertext, style='TLabel')
        self.topLabel.config(font=("Bell MT", 30, "bold"))
        self.topLabel.place(x=10, y=0)
        # Database Button
        self.databaseButton = ttk.Menubutton(
            master, text='Database', cursor='hand2', direction="left", style='TMenubutton')
        self.databaseButton.place(x=1165, y=0)
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
            master, text='export', cursor='hand2', direction="left", style='TMenubutton')
        self.exportButton.place(x=1265, y=0)
        # Configure Export Menubutton
        self.exportButton.menu = tk.Menu(
            self.exportButton, tearoff=False)
        self.exportButton["menu"] = self.exportButton.menu
        self.exportButton.menu.add_command(
            label="Export to Excel", command=self.exportexcel)
        self.exportButton.menu.add_command(
            label="Export to CSV", command=self.exportcsv)
        self.exportButton.menu.add_command(
            label="Export as XML", command=self.exportxml)

      # Create TOP LEFT Frame
        topleftframe = ttk.Frame(
            master, width=450, height=220)
        topleftframe.place(x=10, y=60)

        # Create Child Widgets
        # Title Label
        self.titlelabel = ttk.Label(
            topleftframe, text="Kindly select the options you'll like to see results for:", style='TLabel', width=60, justify=CENTER)
        self.titlelabel.config(font=("times new roman", 10, "bold"))
        self.titlelabel.config(foreground="black")
        self.titlelabel.pack(side=TOP, expand=1, padx=2, pady=2)
        # Age
        ageframe = ttk.Labelframe(
            topleftframe, text="Age:", labelanchor=NW)
        ageframe.pack(side=TOP, expand=0, fill=X, padx=2, pady=2)
        self.agevar = tk.StringVar()
        self.age_firstradio = ttk.Radiobutton(
            ageframe, text='less than 25', value="1", variable=self.agevar, style='TRadiobutton')
        self.age_firstradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        self.age_secondradio = ttk.Radiobutton(
            ageframe, text='above 25\nbelow 40', value="2", variable=self.agevar, style='TRadiobutton')
        self.age_secondradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        self.age_thirdradio = ttk.Radiobutton(
            ageframe, text='above 40', value="3", variable=self.agevar, style='TRadiobutton')
        self.age_thirdradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        # Gender
        genderframe = ttk.Labelframe(
            topleftframe, text="Gender:", labelanchor=NW)
        genderframe.pack(side=TOP, expand=0, fill=X, padx=2, pady=2)
        gender = ["--Click to Select Gender--", "Male", "Female", "Transgender", "Gender-neutral", "Non-binary",
                  "Agender", "Pangender", "Genderqueer", "Two-spirit", "Third-gender"]
        self.gendervar = tk.StringVar(value=gender[0])
        self.genderdrop = ttk.OptionMenu(
            genderframe, self.gendervar, *gender, direction="right", style='TMenubutton')
        self.genderdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Ethnicity/Race
        ethnicframe = ttk.Labelframe(
            topleftframe, text="Ethnicity:", labelanchor=NW)
        ethnicframe.pack(side=TOP, expand=0, fill=X, padx=2, pady=2)
        ethnic = ["--Click to Select Race--", "Arab", "Black",
                  "Chinese", "Indo-Asian", "Latin", "White"]
        self.ethnicvar = tk.StringVar(value=ethnic[0])
        self.ethnicdrop = ttk.OptionMenu(
            ethnicframe, self.ethnicvar, *ethnic, direction="right", style='TMenubutton')
        self.ethnicdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Disability
        disabilityframe = ttk.Labelframe(
            topleftframe, text="Disability:", labelanchor=NW)
        disabilityframe.pack(side=TOP, expand=0, fill=X, padx=2, pady=2)
        self.disabilityvar = tk.StringVar()
        self.disability_firstradio = ttk.Radiobutton(
            disabilityframe, text='Yes', value="Yes", variable=self.disabilityvar, style='TRadiobutton')
        self.disability_firstradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        self.disability_secondradio = ttk.Radiobutton(
            disabilityframe, text='No', value="No", variable=self.disabilityvar, style='TRadiobutton')
        self.disability_secondradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        # Create Submit Button
        self.submitbutton = ttk.Button(
            topleftframe, text="Submit", command=self.submitentry, style='TButton')
        self.submitbutton.pack(
            side=TOP, expand=1, padx=5, pady=2, anchor=CENTER)

        # Create Separator
        displayseparator = ttk.Separator(master, style='TSeparator')
        displayseparator.place(x=10, y=330, width=420)

        # Create BOTTOM LEFT Frame
        bottomleftframe = ttk.Frame(
            master, width=450, height=370)
        bottomleftframe.place(x=10, y=340)

        # Create Child Widgets
        # Title Label
        self.titlelabel = ttk.Label(
            bottomleftframe, text="Showing results for selected options:", style='TLabel', width=60, justify=CENTER)
        self.titlelabel.config(font=("times new roman", 10, "bold"))
        self.titlelabel.config(foreground="black")
        self.titlelabel.pack(side=TOP, expand=0, padx=2, pady=2)
        # Total Number based on selection
        totalframe = ttk.Labelframe(
            bottomleftframe, text="Total No.:", labelanchor=NW)
        totalframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=2, pady=2)
        self.totalvar = tk.IntVar()
        self.totallabel = ttk.Label(
            totalframe, textvariable=self.totalvar, justify=CENTER)
        self.totallabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # Percentage of Women
        womenframe = ttk.Labelframe(
            bottomleftframe, text="Percentage (%) of Women:", labelanchor=NW)
        womenframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=2, pady=2)
        self.womenvar = tk.IntVar()
        self.womenlabel = ttk.Label(
            womenframe, textvariable=self.womenvar, justify=CENTER)
        self.womenlabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # Average No. Who Enjoyed the Tour
        enjoyframe = ttk.Labelframe(
            bottomleftframe, text="Average No. of People Who Enjoyed the Tour:", labelanchor=NW)
        enjoyframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=2, pady=2)
        self.enjoyvar = tk.DoubleVar()
        self.enjoylabel = ttk.Label(
            enjoyframe, textvariable=self.enjoyvar, justify=CENTER)
        self.enjoylabel.pack(side=TOP, expand=0, padx=5, pady=3)
        # Average No. Curious about the Sculpture
        curiousframe = ttk.Labelframe(
            bottomleftframe, text="Average No. of People Curious about the Singing Sculpture:", labelanchor=NW)
        curiousframe.pack(side=TOP, expand=0, fill=X,
                          anchor=CENTER, padx=2, pady=2)
        self.curiousvar = tk.DoubleVar()
        self.curiouslabel = ttk.Label(
            curiousframe, textvariable=self.curiousvar, justify=CENTER)
        self.curiouslabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # Average No. Who will like to learn more about the Science of Acoustics
        scienceframe = ttk.Labelframe(
            bottomleftframe, text="Average No. Who will like to Learn more about the Science of Acoustics:", labelanchor=NW)
        scienceframe.pack(side=TOP, expand=0, fill=X,
                          anchor=CENTER, padx=2, pady=2)
        self.sciencevar = tk.DoubleVar()
        self.sciencelabel = ttk.Label(
            scienceframe, textvariable=self.sciencevar, justify=CENTER)
        self.sciencelabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # No. Who will like to attend future events
        futureframe = ttk.Labelframe(
            bottomleftframe, text="No. of People Who will like to Attend Future Events:", labelanchor=NW)
        futureframe.pack(side=TOP, expand=0, fill=X,
                         anchor=CENTER, padx=2, pady=2)
        self.futurevar = tk.IntVar()
        self.futurelabel = ttk.Label(
            futureframe, textvariable=self.futurevar, justify=CENTER)
        self.futurelabel.pack(side=TOP, expand=0, padx=2, pady=3)

        # Create RIGHT Frame
        rightframe = ttk.Frame(master, width=870, height=600)
        rightframe.place(x=470, y=60)

        # Create Treeview Widget
        self.treecolumn = ["Id", "Name", "Age", "Email", "Gender",
                           "Ethnicity", "Disability", "Enjoyed", "Curious", "Science," "Future"]
        self.table = ttk.Treeview(
            rightframe, columns=self.treecolumn, cursor='hand2')
        # Configure Table to Scrolls
        # self.table.config(yscrollcommand=self.vsbar.set)
        # self.table.config(xscrollcommand=self.hsbar.set)
        self.table.pack(side=TOP, expand=1, fill=BOTH)
        # Create Vertical and Horizontal Scrollbars
        # self.vsbar = ttk.Scrollbar(
        #     rightframe, orient="vertical")

        # self.vsbar.config(command=self.table.yview)
        # self.vsbar.pack(side=RIGHT, expand=1, fill=Y)
        # self.hsbar = ttk.Scrollbar(
        #     rightframe, orient="horizontal")
        # self.hsbar.config(command=self.table.xview)
        # self.hsbar.pack(side=BOTTOM, expand=1, fill=X)
        # Copyright Label
        self.cpyrightLabel = ttk.Label(
            master, text="© Copyright 2023 | Lexi-Clair Designs", style='TLabel', width=1350)
        self.cpyrightLabel.config(font=("times new roman", 8, "bold"))
        self.cpyrightLabel.config(foreground="blue")
        self.cpyrightLabel.config(background="light grey")
        self.cpyrightLabel.place(x=0, y=665)

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

    def submitentry(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    window = Mainframe(root)
    root.mainloop()
