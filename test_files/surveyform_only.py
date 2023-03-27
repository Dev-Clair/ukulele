"""
    The code contained in this file is to be imported as a top level frame into Main.
    The program is basically a Main Window which contains,
     1. A mainframe - serves as a container/parent to labelframes
     2. A bottomframe - holds the submit button for transferring enteries from the form to the database
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel
from tkcalendar import Calendar
import time
from datetime import *
# from database.form_database import submitform  # Import -sqlite3- Database


class Mainwindow:
    def __init__(self, master):
        """
            contains top labels:
                Title label - "UKULELE"
                Notice Label - "Kindly enter the required information into the fields below"
            labeframes which hold demographoc and survey questions
            and a bottom frame which holds the submit button
            The submit button is will not submit any information until all mandatory fields "*" have been filled 
        """
        self.master = master
        self.master.title("UKULELE - Survey Form")
        self.master.geometry('550x650+342+20')
        self.master.iconimage = PhotoImage(file='pic/icon_img.ico')
        self.master.iconphoto(True, self.master.iconimage)
        self.master.minsize(100, 100)
        self.master.resizable(0, 0)

        # Widget Styling
        apply_style = ttk.Style(master)
        apply_style.configure('TLabel', foreground="blue",
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

        # Create Main Frame
        mainframe = ttk.Frame(master)
        mainframe.pack(side=TOP, expand=1, fill=BOTH)
        # Title Label
        titlelabel = ttk.Label(
            mainframe, text='UKULELE!!!', foreground='black', font=('times', 20, 'bold'))
        titlelabel.pack(side=TOP)
        self.textlabel = ttk.Label(
            mainframe, text="Kindly enter the required information into the fields below", foreground='black', font=('times', 12, 'bold italic'))
        self.textlabel.pack(side=TOP)
        # id/Tag No.
        idframe = ttk.Labelframe(
            mainframe, text="Id/Tag no.: *", labelanchor=NW)
        idframe.pack(side=TOP, expand=0, fill=X, anchor=CENTER, padx=5, pady=2)
        self.idvar = tk.StringVar()
        self.identry = ttk.Entry(
            idframe, textvariable=self.idvar, width=40, justify=CENTER)
        self.identry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # First Name
        fnameframe = ttk.Labelframe(
            mainframe, text="First name: *", labelanchor=NW)
        fnameframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=5, pady=2)
        self.fnamevar = tk.StringVar()
        self.fnameentry = ttk.Entry(
            fnameframe, textvariable=self.fnamevar, width=40, justify=CENTER)
        self.fnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Last Name
        lnameframe = ttk.Labelframe(
            mainframe, text="Last name: *", labelanchor=NW)
        lnameframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=5, pady=2)
        self.lnamevar = tk.StringVar()
        self.lnameentry = ttk.Entry(
            lnameframe, textvariable=self.lnamevar, width=40, justify=CENTER)
        self.lnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Age
        ageframe = ttk.Labelframe(
            mainframe, text="Age: *", labelanchor=NW)
        ageframe.pack(side=TOP, expand=0, fill=BOTH, padx=5, pady=2)
        self.agevar = tk.StringVar()
        self.ageentry = ttk.Entry(
            ageframe, textvariable=self.agevar, cursor='hand2', width=40, justify=CENTER)
        self.ageentry.pack(side=TOP, expand=1, padx=5, anchor=CENTER)
        self.ageentry.insert(0, "---dd/mm/yyyy---")
        self.ageentry.bind("<Button-1>", self.select_DOB)
        # Gender
        genderframe = ttk.Labelframe(
            mainframe, text="Gender: *", labelanchor=NW)
        genderframe.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        gender = ["--Click to Select Gender--", "Male", "Female", "Transgender", "Gender-neutral", "Non-binary",
                  "Agender", "Pangender", "Genderqueer", "Two-spirit", "Third-gender"]
        self.gendervar = tk.StringVar(value=gender[0])
        self.genderdrop = ttk.OptionMenu(
            genderframe, self.gendervar, *gender, direction="right", style='TMenubutton')
        self.genderdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Ethnicity/Race
        ethnicframe = ttk.Labelframe(
            mainframe, text="Ethnicity: *", labelanchor=NW)
        ethnicframe.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        ethnic = ["--Click to Select Race--", "Arab", "Black",
                  "Chinese", "Indo-Asian", "Latin", "White"]
        self.ethnicvar = tk.StringVar(value=ethnic[0])
        self.ethnicdrop = ttk.OptionMenu(
            ethnicframe, self.ethnicvar, *ethnic, direction="right", style='TMenubutton')
        self.ethnicdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Disability
        disabilityframe = ttk.Labelframe(
            mainframe, text="Disability: *", labelanchor=NW)
        disabilityframe.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        self.disabilityvar = tk.StringVar()
        self.disability_firstradio = ttk.Radiobutton(
            disabilityframe, text='Yes', value="Yes", variable=self.disabilityvar, style='TRadiobutton')
        self.disability_firstradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        self.disability_secondradio = ttk.Radiobutton(
            disabilityframe, text='No', value="No", variable=self.disabilityvar, style='TRadiobutton')
        self.disability_secondradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        # Form Separator
        self.formdivide = ttk.Separator(
            mainframe, orient="horizontal", style='TSeparator')
        self.formdivide.pack(side=TOP, fill=X, expand=0, padx=5)
        # Question 1
        q1_frame = ttk.Labelframe(
            mainframe, text="1. Did you enjoy your tour around the singing sculpture? ", labelanchor=NW)
        q1_frame.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        self.q1_variable = tk.StringVar()
        self.q1_firstradio = ttk.Radiobutton(
            q1_frame, text='Yes', value="Yes", variable=self.q1_variable, style='TRadiobutton')
        self.q1_firstradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        self.q1_secondradio = ttk.Radiobutton(
            q1_frame, text='No', value="No", variable=self.q1_variable, style='TRadiobutton')
        self.q1_secondradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        # Question 2
        q2_frame = ttk.Labelframe(
            mainframe, text="2. Are you curious as to how the Ukulele sings? ", labelanchor=NW)
        q2_frame.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        self.q2_variable = tk.StringVar()
        self.q2_firstradio = ttk.Radiobutton(
            q2_frame, text='Yes', value="Yes", variable=self.q2_variable, style='TRadiobutton')
        self.q2_firstradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        self.q2_secondradio = ttk.Radiobutton(
            q2_frame, text='No', value="No", variable=self.q2_variable, style='TRadiobutton')
        self.q2_secondradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        # Question 3
        q3_frame = ttk.Labelframe(
            mainframe, text="3. Will you like to know more about the science of acoustics? ", labelanchor=NW)
        q3_frame.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        self.q3_variable = tk.StringVar()
        self.q3_firstradio = ttk.Radiobutton(
            q3_frame, text='Yes', value="Yes", variable=self.q3_variable, style='TRadiobutton')
        self.q3_firstradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        self.q3_secondradio = ttk.Radiobutton(
            q3_frame, text='No', value="No", variable=self.q3_variable, style='TRadiobutton')
        self.q3_secondradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        # Question 4
        q4_frame = ttk.Labelframe(
            mainframe, text="4. Will you attend future science events organised by the sponsors? ", labelanchor=NW)
        q4_frame.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        self.q4_variable = tk.StringVar()
        self.q4_firstradio = ttk.Radiobutton(
            q4_frame, text='Yes', value="Yes", variable=self.q4_variable, style='TRadiobutton', command=self.emailoption)
        self.q4_firstradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        self.q4_secondradio = ttk.Radiobutton(
            q4_frame, text='No', value="No", variable=self.q4_variable, style='TRadiobutton', command=self.emailoption)
        self.q4_secondradio.pack(
            side=LEFT, expand=1, padx=5, pady=2, anchor=W)
        # Email
        emailframe = ttk.Labelframe(
            mainframe, text="Email: ", labelanchor=NW)
        emailframe.pack(side=TOP, expand=0, fill=X, padx=5, pady=2)
        self.emailvar = tk.StringVar()
        self.emailentry = ttk.Entry(
            emailframe, textvariable=self.emailvar, width=40, justify=CENTER, state="disabled")
        self.emailentry.pack(side=TOP, expand=1, padx=5, anchor=CENTER)

        # Create Bottom Frame for Buttons
        bottomframe = ttk.Frame(master)
        bottomframe.pack(side=BOTTOM)
        # Create Submit Button for Survey Form
        self.submitbutton = ttk.Button(
            bottomframe, text='Submit', cursor='hand2', command=self.submitform)
        self.submitbutton.pack(side=RIGHT, expand=1,
                               padx=(20, 25), pady=2, anchor=CENTER)

        # Direct input focus to the first entry widget of the survey form
        self.identry.focus_set()

    # Class Functions
    def select_DOB(self, event):
        self.dob_window = tk.Toplevel()
        self.dob_window.grab_set()
        self.dob_window.title("Select Date of Birth")
        self.dob_window.geometry("350x250+450+100")
        self.cal = Calendar(
            self.dob_window, selectmode="day", datepattern="dd/mm/yyyy", background="violet red", foreground="white", headersforeground="violet red", selectforeground="violet red", headersbackground="white")
        self.cal.pack(expand=1, fill=BOTH)

        self.submit_date = ttk.Button(
            self.dob_window, text="Submit", style='TButton', command=self.grab_selection)
        self.submit_date.pack(expand=1, pady=5)

    def grab_selection(self):
        # Calculate Age using the Datetime Module
        self.today_date = datetime.today()
        self.birth_date = datetime.strptime(
            self.cal.get_date(), '%m/%d/%y')
        self.current_age = self.today_date.year - self.birth_date.year - \
            ((self.today_date.month, self.today_date.day) <
             (self.birth_date.month, self.birth_date.day))
        # Insert Current Age into Age
        self.ageentry.delete(0, END)
        self.ageentry.insert(0, self.current_age)
        self.dob_window.destroy()

    def emailoption(self):
        # Attach callback handler to display email entry if the respondent selects "Yes" to Question 4
        if self.q4_variable.get() == "Yes":
            self.emailentry.config(state="normal")
            # Direct input focus to the email entry widget
            self.emailentry.focus_set()
        else:
            self.emailentry.config(state="disabled")

    def submitform(self):
        """
            Before submitting entries a check should be run to ensure all required fields have been completed by the respondents
            This is important as the button submits the information directly to the database
            A tkinter messagebox should be used to ask respondent to confirm they have satisfactorily entered all required information 
            if any of the mandatory fields * are left empty, the button show throw/dispaly an error messagebox
        """
        if self.idvar.get() == "" or self.agevar.get() == "" or self.gendervar.get() == "" or self.ethnicvar.get() == "" or self.disabilityvar.get() == "":
            showerror('Mandatory Fields',
                      '* information fields cannot be empty')
        else:
            self.answer = askokcancel('Confirm Submission',
                                      'Click OK to confirm submission.')
            if self.answer:
                # Database takes it over from here
                showinfo('Survey Form',
                         'Thank you for your time\n Enjoy the rest of the event.')
                root.quit()
            print(f"{self.idvar.get()}\n{self.fnamevar.get()} {self.lnamevar.get()}\n{self.agevar.get()}\n{self.gendervar.get()}\n{self.ethnicvar.get()}\n{self.disabilityvar.get()}\n{self.q1_variable.get()}\n{self.q2_variable.get()}\n{self.q3_variable.get()}\n{self.q4_variable.get()}\n{self.emailvar.get()}")


if __name__ == "__main__":
    root = tk.Toplevel()
    window = Mainwindow(root)
    root.mainloop()
