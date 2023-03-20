"""
    The code contained in this file is to be imported as a top level frame into Main.
    The program is basically a Main Window which contains,
     1. A topframe - holds title label
     2. A mainframe - serves as a container/parent to two child frames: Firstframe and Secondframe
     3. A bottomframe - holds the buttons for switching between frames and submitting the survey form
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel, askyesno, askyesnocancel
from tkcalendar import Calendar


class Firstframe(ttk.Frame):
    def __init__(self, master):
        """
            The first frame or window is displayed in the mainframe until the ">>>" button is clicked
            This window collects personal and demographic information from respondents
            Information fields required are;
            1. ID/Tag No.
            2. First and Last Names
            3. Age
            4. Gender
            5. Ethnicity and 
            6. Disability status
        """
        super().__init__(master, width=500, height=600)
        self.pack(side=TOP, expand=1, fill=BOTH)
        # self.master = master

        # Create First -Child-  Form Page
        # Title Label
        titlelabel = ttk.Label(
            self, text='UKULELE!!!', foreground='violet red', font=('times', 20, 'bold'))
        titlelabel.pack(side=TOP)
        self.textlabel = ttk.Label(
            self, text="Kindly enter the required information into the fields below", foreground='violet red', font=('times', 12, 'bold italic'))
        self.textlabel.pack(side=TOP)
        # id/Tag No.
        idframe = ttk.Labelframe(
            self, text="Id/Tag no.: *", labelanchor=NW)
        idframe.pack(side=TOP, expand=0, fill=X, anchor=CENTER, padx=5, pady=5)
        self.idvar = tk.StringVar()
        self.identry = ttk.Entry(
            idframe, textvariable=self.idvar, width=40, justify=CENTER)
        self.identry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # First Name
        fnameframe = ttk.Labelframe(
            self, text="First name: *", labelanchor=NW)
        fnameframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=5, pady=5)
        self.fnamevar = tk.StringVar()
        self.fnameentry = ttk.Entry(
            fnameframe, textvariable=self.fnamevar, width=40, justify=CENTER)
        self.fnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Last Name
        lnameframe = ttk.Labelframe(
            self, text="Last name: *", labelanchor=NW)
        lnameframe.pack(side=TOP, expand=0, fill=X,
                        anchor=CENTER, padx=5, pady=5)
        self.lnamevar = tk.StringVar()
        self.lnameentry = ttk.Entry(
            lnameframe, textvariable=self.lnamevar, width=40, justify=CENTER)
        self.lnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Age
        ageframe = ttk.Labelframe(
            self, text="Age: *", labelanchor=NW)
        ageframe.pack(side=TOP, expand=0, fill=BOTH, padx=5, pady=5)
        self.agevar = tk.StringVar()
        self.ageentry = ttk.Entry(
            ageframe, textvariable=self.agevar, width=40, justify=CENTER)
        self.ageentry.pack(side=TOP, expand=1, padx=5, anchor=CENTER)
        self.ageentry.insert(0, "---dd/mm/yyyy---")
        self.ageentry.bind("<Button-1>", self.select_DOB)
        # Gender
        genderframe = ttk.Labelframe(
            self, text="Gender: *", labelanchor=NW)
        genderframe.pack(side=TOP, expand=0, fill=X, padx=5, pady=5)
        gender = ["--Click to Select--", "Male", "Female", "Transgender", "Gender-neutral", "Non-binary",
                  "Agender", "Pangender", "Genderqueer", "Two-spirit", "Third-gender"]
        self.gendervar = tk.StringVar(value=gender[0])
        self.genderdrop = ttk.OptionMenu(
            genderframe, self.gendervar, *gender, direction="above", style='TMenubutton', )
        self.genderdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Ethnicity
        ethnicframe = ttk.Labelframe(
            self, text="Ethnicity: *", labelanchor=NW)
        ethnicframe.pack(side=TOP, expand=0, fill=X, padx=5, pady=5)
        ethnic = ["--Click to Select--", "Arab", "Black",
                  "Chinese", "Indo-Asian", "Latin", "White"]
        self.ethnicvar = tk.StringVar(value=ethnic[0])
        self.ethnicdrop = ttk.OptionMenu(
            ethnicframe, self.ethnicvar, *ethnic, direction="above", style='TMenubutton', )
        self.ethnicdrop.pack(side=TOP, expand=1, anchor=CENTER)
        # Disability
        disabilityframe = ttk.Labelframe(
            self, text="Disability: *", labelanchor=NW)
        disabilityframe.pack(side=TOP, expand=0, fill=X, padx=5, pady=5)
        disability = ["--Click to Select--", "Yes", "No"]
        self.disabilityvar = tk.StringVar(value=disability[0])
        self.disabilitydrop = ttk.OptionMenu(
            disabilityframe, self.disabilityvar, *disability, direction="above", style='TMenubutton', )
        self.disabilitydrop.pack(side=TOP, expand=1, anchor=CENTER)

    # Widget Functions
    def select_DOB(self, event):
        self.dob_window = tk.Toplevel()
        self.dob_window.grab_set()
        self.dob_window.title("Select Date of Birth")
        self.dob_window.geometry("350x250+450+100")
        self.cal = Calendar(
            self.dob_window, selectmode="day", date_pattern="dd/mm/yyyy", background="violet red", foreground="white", headersforeground="violet red", selectforeground="violet red", headersbackground="white", )
        self.cal.pack(expand=1, fill=BOTH)

        self.submit_date = ttk.Button(
            self.dob_window, text="SUBMIT", style='TButton', command=self.grab_selection)
        self.submit_date.pack(expand=1, pady=5)

    def grab_selection(self):
        self.ageentry.delete(0, END)
        self.ageentry.insert(0, self.cal.get_date())
        self.dob_window.destroy()

    # if self.identry.get() or self.ageentry.get() or self.genderentry.get() or self.ethnicentry.get() or self.disabilityentry.get() == "":
    #     showerror('Mandatory Fields',
    #               '* information fields cannot be empty')
    # else:
    #     pass


class Secondframe(ttk.Frame):
    def __init__(self, master):
        """
            The second frame or window is displayed after the ">>>" button is clicked
            This window collects information about the event from respondents
            Information fields required are;
            1. if the respondents enjoyed the tour
            2. will they love to find out about the science of acoustics
            3. will they attend future events hosted by the funders/sponsors
        """
        super().__init__(master, width=500, height=600)
        self.pack(side=TOP, expand=1, fill=BOTH)
        self.master = master

        # Create Variables
        self.q1_variable = tk.BooleanVar()
        self.q2_variable = tk.BooleanVar()
        self.q3_variable = tk.BooleanVar()
        self.q4_variable = tk.BooleanVar()
        self.emailvar = tk.StringVar()

        # Create Second -Child-  Form Page
        # Title Label
        titlelabel = ttk.Label(
            self, text='UKULELE!!!', foreground='violet red', font=('times', 20, 'bold'))
        titlelabel.pack(side=TOP)
        self.textlabel = ttk.Label(
            self, text="Kindly select the option that best describes your experience so far", foreground='violet red', font=('times', 12, 'bold italic'))
        self.textlabel.pack(side=TOP)
        # Question 1
        q1_frame = ttk.Frame(self)
        q1_frame.pack(side=TOP, expand=1, fill=BOTH)
        # self.q1_variable = tk.BooleanVar()
        self.q1_label = ttk.Label(
            q1_frame, text="1. Did you enjoy your tour around the singing sculpture? ")
        self.q1_label.pack(side=TOP, expand=1, fill=BOTH, padx=5, anchor=W)
        q1_radioframe = ttk.Frame(q1_frame)
        q1_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q1_firstradio = ttk.Radiobutton(
            q1_radioframe, text='Yes', value="Yes", variable=self.q1_variable, style='TRadiobutton')
        self.q1_firstradio.pack(
            side=TOP, expand=1, padx=(20, 25), pady=2, anchor=W)
        self.q1_secondradio = ttk.Radiobutton(
            q1_radioframe, text='No', value="No", variable=self.q1_variable, style='TRadiobutton')
        self.q1_secondradio.pack(
            side=TOP, expand=1, padx=(20, 25), pady=2, anchor=W)
        # Question 2
        q2_frame = ttk.Frame(self)
        q2_frame.pack(side=TOP, expand=1, fill=BOTH)
        # self.q2_variable = tk.BooleanVar()
        self.q2_label = ttk.Label(
            q2_frame, text="2. Are you curious as to how the Ukulele sings? ")
        self.q2_label.pack(side=TOP, expand=1, padx=5, anchor=W)
        q2_radioframe = ttk.Frame(q2_frame)
        q2_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q2_firstradio = ttk.Radiobutton(
            q2_radioframe, text='Yes', value="Yes", variable=self.q2_variable, style='TRadiobutton')
        self.q2_firstradio.pack(side=TOP, expand=1,
                                padx=(20, 25), pady=2, anchor=W)
        self.q2_secondradio = ttk.Radiobutton(
            q2_radioframe, text='No', value="No", variable=self.q2_variable, style='TRadiobutton')
        self.q2_secondradio.pack(side=TOP, expand=1,
                                 padx=(20, 25), pady=2, anchor=W)
        # Question 3
        q3_frame = ttk.Frame(self)
        q3_frame.pack(side=TOP, expand=1, fill=BOTH)
        # self.q3_variable = tk.BooleanVar()
        self.q3_label = ttk.Label(
            q3_frame, text="3. Will you like to know more about the science of acoustics? ")
        self.q3_label.pack(side=TOP, expand=1, padx=5, anchor=W)
        q3_radioframe = ttk.Frame(q3_frame)
        q3_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q3_firstradio = ttk.Radiobutton(
            q3_radioframe, text='Yes', value="Yes", variable=self.q3_variable, style='TRadiobutton')
        self.q3_firstradio.pack(side=TOP, expand=1,
                                padx=(20, 25), pady=2, anchor=W)
        self.q3_secondradio = ttk.Radiobutton(
            q3_radioframe, text='No', value="No", variable=self.q3_variable, style='TRadiobutton')
        self.q3_secondradio.pack(side=TOP, expand=1,
                                 padx=(20, 25), pady=2, anchor=W)
        # Question 4
        q4_frame = ttk.Frame(self)
        q4_frame.pack(side=TOP, expand=1, fill=BOTH)
        # self.q4_variable = tk.BooleanVar()
        self.q4_label = ttk.Label(
            q4_frame, text="4. Will you attend future science events organised by the sponsors? ")
        self.q4_label.pack(side=TOP, expand=1, padx=5, anchor=W)
        q4_radioframe = ttk.Frame(q4_frame)
        q4_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q4_firstradio = ttk.Radiobutton(
            q4_radioframe, text='Yes', value="Yes", variable=self.q4_variable, style='TRadiobutton')
        self.q4_firstradio.pack(side=TOP, expand=1,
                                padx=(20, 25), pady=2, anchor=W)
        self.q4_secondradio = ttk.Radiobutton(
            q4_radioframe, text='No', value="No", variable=self.q4_variable, style='TRadiobutton')
        self.q4_secondradio.pack(side=TOP, expand=1,
                                 padx=(20, 25), pady=2, anchor=W)
        # Email
        emailframe = ttk.Frame(self)
        emailframe.pack(side=TOP, expand=1, fill=BOTH)
        self.emaillabel = ttk.Label(
            emailframe, text="Email: ", style='TLabel')
        self.emaillabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.emailentry = ttk.Entry(
            emailframe, textvariable=self.emailvar)
        self.emailentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)


class Mainwindow:
    def __init__(self, master):
        """
            contains a top frame which holds the title label - "UKULELE"
            a mainframe which serves as a parent or container window to two child frames - Firstframe and Secondframe
            and a bottom frame which holds two buttons
            the ">>>" button allows us to move from one page to the other while the submit button submits entries entered by the user.
            The submit button is temporarily disabled while the respondent fills the information in the first window and comes normal when the respondent switches to the next frame 
        """
        self.master = master
        self.master.title("UKULELE - Survey Form")
        self.master.geometry('500x600+342+50')
        self.master.iconimage = PhotoImage(file='images/icon_img.ico')
        self.master.iconphoto(True, root.iconimage)
        self.master.minsize(100, 100)
        self.master.resizable(0, 0)

        # Widget Styling
        apply_style = ttk.Style(master)
        apply_style.configure('TLabel', foreground="violet red",
                              font=("Helvetica", 10, "bold"))
        apply_style.configure('TEntry', foreground="blue",
                              background="WhiteSmoke", font=("Helvetica", 12, "normal"))
        apply_style.configure('TButton', foreground="violet red",
                              background="MistyRose", font=("Helvetica", 10, "bold"))
        apply_style.configure('TRadiobutton', foreground="violet red",
                              font=("times new roman", 10, "bold"))
        apply_style.configure('TMenubutton', foreground="blue",
                              font=("Helvetica", 10, "bold"))
        # apply_style.configure('TLabelFrame', foreground="violet red",
        #                       font=("Helvetica", 10, "bold"))

        # Create Title Frame for Title Label
        # topframe = ttk.Frame(master)
        # topframe.pack(side=TOP)
        # self.titlelabel = ttk.Label(
        #     master, text='UKULELE!!!', foreground='violet red', font=('times', 20, 'bold'))
        # self.titlelabel.pack(side=TOP, padx=5, pady=5, anchor=CENTER)

        # Create Main Frame to act as Parent for Child Frames
        mainframe = ttk.Frame(master)
        mainframe.pack(expand=1, fill=BOTH)

        # Initialize Page/Child Frame Counter
        self.windowNum = 0

        # Add Child Frames to Parent Window
        self.framelist = []
        self.framelist.append(Firstframe(mainframe))
        self.framelist.append(Secondframe(mainframe))
        self.framelist[1].forget()

        # Create Bottom Frame for Buttons
        bottomframe = ttk.Frame(master)
        bottomframe.pack(side=BOTTOM)
        # Create Button for Switching Frames
        self.switchbutton = ttk.Button(
            bottomframe, text='>>>', cursor='hand2', command=self.switchframe)
        self.switchbutton.pack(side=LEFT, expand=1, padx=(
            20, 25), pady=2, anchor=CENTER)
        # Create Submit Button for Survey Form
        self.submitbutton = ttk.Button(
            bottomframe, text='Submit', cursor='hand2', command=self.submitform, state="disabled")  # Submit button is disabled in the first window
        self.submitbutton.pack(side=RIGHT, expand=1,
                               padx=(20, 25), pady=2, anchor=CENTER)

        # Trying to automate the state of the button with respect to the frame/window view.
        # I think can be achieved via threading. will try it out later
        # if self.framelist[self.windowNum] == 0:
        #     self.submitbutton.config(state="disabled")
        # elif self.framelist[self.windowNum] == 0:
        #     self.submitbutton.config(state="normal")

    def switchframe(self):
        """
            This button allows the respondent to switch between information/entry field windows
            This function keeps the child frames in the main frame in a continuous loop instead of clicking separate next or previous buttons to change views
        """
        # if self.idvar.get() or self.agevar.get() or self.gendervar.get() or self.ethnicvar.get() or self.disabilityvar.get() == "":
        #     showerror('Mandatory Fields',
        #               '* information fields cannot be empty')
        # else:
        #     # pass
        self.framelist[self.windowNum].forget()
        self.windowNum = (self.windowNum+1) % len(self.framelist)
        # Using the tk.raise() method to switch form frames
        self.framelist[self.windowNum].tkraise()
        # Packing the current frame as the .forget() method unpacks whichever frame is current
        self.framelist[self.windowNum].pack(expand=1, fill=BOTH, pady=5)
        # Activate submit button in next frame
        self.submitbutton.config(state="normal")

    def submitform(self):
        """
            Before submitting entries a check should be run to ensure all required fields have been completed by the respondents
            This is important as the button submits the information directly to the database
            A tkinter messagebox should be used to ask respondent to confirm they have satisfactorily entered all required information 
            if any of the mandatory fields * are left empty, the button show throw/dispaly an error messagebox
        """
        print("\nSubmit button was clicked")


if __name__ == "__main__":
    root = tk.Toplevel()
    window = Mainwindow(root)
    root.mainloop()
