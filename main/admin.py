import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel
from form_database import selectrecord  # Import -sqlite3- Database


class Mainframe:
    def __init__(self, master):
        self.master = master
        self.master.title("UKULELE - Admin")
        self.master.geometry('1350x680+5+5')
        self.master.iconimage = PhotoImage(file='pic/icon_img.ico')
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
        apply_style.configure(
            'Treeview.Heading', foreground="lightgreen", background="lightblue")

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
            label="Connect to Database", command=self.connectdb)
        self.databaseButton.menu.add_command(
            label="Upload Database to Server", command=self.uploaddb)
        # Export Button
        self.exportButton = ttk.Menubutton(
            master, text='Export', cursor='hand2', direction="left", style='TMenubutton')
        self.exportButton.place(x=1265, y=0)
        # Configure Export Menubutton
        self.exportButton.menu = tk.Menu(
            self.exportButton, tearoff=False)
        self.exportButton["menu"] = self.exportButton.menu
        self.exportButton.menu.add_command(
            label="...export to Excel", command=self.exportexcel)
        self.exportButton.menu.add_command(
            label="...export to CSV", command=self.exportcsv)
        self.exportButton.menu.add_command(
            label="...export as XML", command=self.exportxml)

        # Create TOP LEFT Frame
        topleftframe = ttk.Frame(
            master)
        topleftframe.place(x=10, y=60, width=450, height=250)

        # Create Child Widgets
        # Title Label
        self.titlelabel = ttk.Label(
            topleftframe, text="Kindly select the options you'll like to see results for:", style='TLabel', justify=LEFT)
        self.titlelabel.config(font=("times new roman", 10, "bold"))
        self.titlelabel.config(foreground="black")
        self.titlelabel.pack(side=TOP, expand=1)
        # Age     ##################### Values of RadioButton Needs to Be Adjusted to work with Database Data Types
        ageframe = ttk.Labelframe(
            topleftframe, text="Age:", labelanchor=NW)
        ageframe.pack(side=TOP, expand=0, fill=X, padx=2)
        self.agevar = tk.StringVar()
        self.age_firstradio = ttk.Radiobutton(
            ageframe, text='less than 25', value="< 25", variable=self.agevar, style='TRadiobutton')
        self.age_firstradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        self.age_secondradio = ttk.Radiobutton(
            ageframe, text='above 25\nbelow 40', value="25><40", variable=self.agevar, style='TRadiobutton')
        self.age_secondradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        self.age_thirdradio = ttk.Radiobutton(
            ageframe, text='above 40', value=">40", variable=self.agevar, style='TRadiobutton')
        self.age_thirdradio.pack(
            side=LEFT, expand=1, padx=2, pady=3, anchor=W)
        # Gender
        genderframe = ttk.Labelframe(
            topleftframe, text="Gender:", labelanchor=NW)
        genderframe.pack(side=TOP, expand=0, fill=X, padx=2)
        gender = ["--Click to Select Gender--", "Male", "Female", "Transgender", "Gender-neutral", "Non-binary",
                  "Agender", "Pangender", "Genderqueer", "Two-spirit", "Third-gender"]
        self.gendervar = tk.StringVar(value=gender[0])
        self.genderdrop = ttk.OptionMenu(
            genderframe, self.gendervar, *gender, direction="right", style='TMenubutton')
        self.genderdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Ethnicity/Race
        ethnicframe = ttk.Labelframe(
            topleftframe, text="Ethnicity:", labelanchor=NW)
        ethnicframe.pack(side=TOP, expand=0, fill=X, padx=2)
        ethnic = ["--Click to Select Race--", "Arab", "Black",
                  "Chinese", "Indo-Asian", "Latin", "White"]
        self.ethnicvar = tk.StringVar(value=ethnic[0])
        self.ethnicdrop = ttk.OptionMenu(
            ethnicframe, self.ethnicvar, *ethnic, direction="right", style='TMenubutton')
        self.ethnicdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Disability
        disabilityframe = ttk.Labelframe(
            topleftframe, text="Disability:", labelanchor=NW)
        disabilityframe.pack(side=TOP, expand=0, fill=X, padx=2)
        self.disabilityvar = tk.StringVar()
        self.disability_firstradio = ttk.Radiobutton(
            disabilityframe, text='Yes', value="Yes", variable=self.disabilityvar, style='TRadiobutton')
        self.disability_firstradio.pack(
            side=LEFT, expand=1, padx=2, pady=2, anchor=W)
        self.disability_secondradio = ttk.Radiobutton(
            disabilityframe, text='No', value="No", variable=self.disabilityvar, style='TRadiobutton')
        self.disability_secondradio.pack(
            side=LEFT, expand=1, padx=2, anchor=W)
        # Create Submit Button
        self.submitbutton = ttk.Button(
            topleftframe, text="Submit", command=self.submitentry, style='TButton')
        self.submitbutton.pack(
            side=TOP, expand=1, padx=5, pady=5, anchor=CENTER)

        # Create Separator
        displayseparator = ttk.Separator(master, style='TSeparator')
        displayseparator.place(x=10, y=330, width=450)

        # Create BOTTOM LEFT Frame
        bottomleftframe = ttk.Frame(
            master)
        bottomleftframe.place(x=10, y=340, width=450, height=350)

        # Create Child Widgets
        # Title Label
        self.titlelabel = ttk.Label(
            bottomleftframe, text="Showing results for selected options:", style='TLabel', justify=LEFT)
        self.titlelabel.config(font=("times new roman", 10, "bold"))
        self.titlelabel.config(foreground="black")
        self.titlelabel.pack(side=TOP, expand=0)
        # Total Number based on selection
        totalframe = ttk.Labelframe(
            bottomleftframe, text="Total No.:", labelanchor=NW)
        totalframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=2)
        self.totalvar = tk.IntVar()
        self.totallabel = ttk.Label(
            totalframe, textvariable=self.totalvar, justify=CENTER)
        self.totallabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # Percentage of Women
        womenframe = ttk.Labelframe(
            bottomleftframe, text="Percentage (%) of Women:", labelanchor=NW)
        womenframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=2)
        self.womenvar = tk.IntVar()
        self.womenlabel = ttk.Label(
            womenframe, textvariable=self.womenvar, justify=CENTER)
        self.womenlabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # Average No. Who Enjoyed the Tour
        enjoyframe = ttk.Labelframe(
            bottomleftframe, text="Average No. of People Who Enjoyed the Tour:", labelanchor=NW)
        enjoyframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=2)
        self.enjoyvar = tk.DoubleVar()
        self.enjoylabel = ttk.Label(
            enjoyframe, textvariable=self.enjoyvar, justify=CENTER)
        self.enjoylabel.pack(side=TOP, expand=0, padx=5, pady=3)
        # Average No. Curious about the Sculpture
        curiousframe = ttk.Labelframe(
            bottomleftframe, text="Average No. of people curious about the Ukulele:", labelanchor=NW)
        curiousframe.pack(side=TOP, expand=0, fill=X,
                          anchor=CENTER, padx=2)
        self.curiousvar = tk.DoubleVar()
        self.curiouslabel = ttk.Label(
            curiousframe, textvariable=self.curiousvar, justify=CENTER)
        self.curiouslabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # Average No. Who will like to learn more about the Science of Acoustics
        scienceframe = ttk.Labelframe(
            bottomleftframe, text="Average No. Who will like to learn more about the science of acoustics:", labelanchor=NW)
        scienceframe.pack(side=TOP, expand=0, fill=X,
                          anchor=CENTER, padx=2)
        self.sciencevar = tk.DoubleVar()
        self.sciencelabel = ttk.Label(
            scienceframe, textvariable=self.sciencevar, justify=CENTER)
        self.sciencelabel.pack(side=TOP, expand=0, padx=2, pady=3)
        # No. Who will like to attend future events
        futureframe = ttk.Labelframe(
            bottomleftframe, text="No. of people who will like to attend future events:", labelanchor=NW)
        futureframe.pack(side=TOP, expand=0, fill=X,
                         anchor=CENTER, padx=2)
        self.futurevar = tk.IntVar()
        self.futurelabel = ttk.Label(
            futureframe, textvariable=self.futurevar, justify=CENTER)
        self.futurelabel.pack(side=TOP, expand=0, padx=2, pady=3)

        # Create RIGHT Frame
        rightframe = ttk.Frame(master)
        # Create Vertical and Horizontal Scrollbars
        self.hsbar = ttk.Scrollbar(
            rightframe, orient="horizontal")
        self.vsbar = ttk.Scrollbar(
            rightframe)
        # Create Treeview Widget
        self.treecolumn = ("Id", "Tag", "Name", "Age", "Email", "Gender",
                           "Ethnicity", "Disability", "Enjoyed", "Curious", "Science", "Future")
        self.table = ttk.Treeview(
            rightframe, columns=self.treecolumn, show="headings", style="Treewview.Heading", xscrollcommand=self.hsbar.set, yscrollcommand=self.vsbar.set, cursor='hand2')
        # Configure Scrollbars to -treeview- Table
        self.hsbar.config(command=self.table.xview)
        self.vsbar.config(command=self.table.yview)
        # Define Table -Treeview- Headings
        self.table.heading("Id", text="Id", anchor=CENTER)  # Add Callback
        self.table.heading("Tag", text="Tag No.",
                           anchor=CENTER)  # Add Callback
        self.table.heading("Name", text="Name", anchor=CENTER)  # Add Callback
        self.table.heading("Age", text="Age", anchor=CENTER)  # Add Callback
        self.table.heading("Email", text="Email",
                           anchor=CENTER)  # Add Callback
        self.table.heading("Gender", text="Gender",
                           anchor=CENTER)  # Add Callback
        self.table.heading("Ethnicity", text="Ethnicity",
                           anchor=CENTER)  # Add Callback
        self.table.heading("Disability", text="Disability",
                           anchor=CENTER)  # Add Callback
        self.table.heading("Enjoyed", text="Enjoyed",
                           anchor=CENTER)  # Add Callback
        self.table.heading(
            "Curious", text="Curious", anchor=CENTER)  # Add Callback
        self.table.heading(
            "Science", text="Science", anchor=CENTER)  # Add Callback
        self.table.heading("Future", text="Future",
                           anchor=CENTER)  # Add Callback
        # Configure Table -Treeview- Columns
        self.table.column("Id", width=50, stretch=1, anchor=CENTER)
        self.table.column("Tag", width=50, stretch=1, anchor=CENTER)
        self.table.column("Name", width=200, stretch=1, anchor=CENTER)
        self.table.column("Age", width=100, stretch=1, anchor=CENTER)
        self.table.column("Email", width=200, stretch=1, anchor=CENTER)
        self.table.column("Gender", width=100, stretch=1, anchor=CENTER)
        self.table.column("Ethnicity", width=100, stretch=1, anchor=CENTER)
        self.table.column("Disability", width=100, stretch=1, anchor=CENTER)
        self.table.column("Enjoyed", width=100, stretch=1, anchor=CENTER)
        self.table.column("Curious", width=100, stretch=1, anchor=CENTER)
        self.table.column("Science", width=150, stretch=1, anchor=CENTER)
        self.table.column("Future", width=100, stretch=1, anchor=CENTER)
        # Display -Pack- RIGHT Frame Widgets
        self.hsbar.pack(side=BOTTOM, fill=X)
        self.vsbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH, expand=1)
        rightframe.place(x=470, y=60, width=880, height=600)

        # Generate Sample Data
        contacts = []
        for i in range(1, 80):
            contacts.append((f'id{i}', f'tag{i}', f'first last{i}', f'age{i}', f'first.last{i}@yahoo.com', f'gender{i}', f'ethnicity{i}',
                             f'disability{i}', f'enjoyed{i}', f'curious{i}', f'science{i}', f'future{i}'))
        # Insert Sample Data into Treeview Table
        for contact in contacts:
            self.table.insert("", END, values=contact)

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
        print(
            f"\n{self.agevar.get()}\n{self.gendervar.get()}\n{self.ethnicvar.get()}\n{self.disabilityvar.get()}")
        selectrecord(self.agevar.get(), self.gendervar.get(),
                     self.ethnicvar.get(), self.disabilityvar.get())


if __name__ == "__main__":
    root = tk.Tk()
    window = Mainframe(root)
    root.mainloop()
