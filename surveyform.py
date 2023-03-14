"""
    OOP Style
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *


class Firstframe(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width=500, height=600)
        self.pack(side=TOP, expand=1, fill=BOTH)

        # Widget Styling - Labels, Entrys, Buttons
        self.apply_style = ttk.Style()
        self.apply_style.configure('TLabel', foreground="violet red",
                                   font=("Helvetica", 12, "bold"))
        self.apply_style.configure('TEntry', foreground="black",
                                   background="WhiteSmoke", font=("Helvetica", 12, "bold"), bd=2)
        self.apply_style.configure('TButton', foreground="violet red",
                                   background="MistyRose", font=("Helvetica", 12, "bold"))
        self.apply_style.configure('TRadiobutton', foreground="violet red",
                                   font=("times new roman", 10, "bold"))

        # Create First -Child-  Form Page
        # Information Frame
        self.labelframe1 = ttk.Frame(self)
        self.labelframe1.pack(side=TOP, expand=1, fill=BOTH)
        self.textlabel1 = ttk.Label(
            self.labelframe1, text="Kindly fill in the right information into the fields below", foreground='violet red', font=('times', 12, 'bold italic'))
        self.textlabel1.pack(side=TOP, expand=1,
                             fill=BOTH, padx=5, pady=5)
        # id/Tag No.
        self.idframe = ttk.Frame(self)
        self.idframe.pack(side=TOP, expand=1, fill=BOTH)
        self.idlabel = ttk.Label(self.idframe, text="Id/Tag No: *",
                                 foreground='violet red', font=('times', 12, 'bold'))
        self.idlabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.identry = ttk.Entry(self.idframe)
        self.identry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # First Name
        self.fnameframe = ttk.Frame(self)
        self.fnameframe.pack(side=TOP, expand=1, fill=BOTH)
        self.fnamelabel = ttk.Label(
            self.fnameframe, text="First name: ", foreground='violet red', font=('times', 12, 'bold'))
        self.fnamelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.fnameentry = ttk.Entry(self.fnameframe)
        self.fnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Last Name
        self.lnameframe = ttk.Frame(self)
        self.lnameframe.pack(side=TOP, expand=1, fill=BOTH)
        self.lnamelabel = ttk.Label(
            self.lnameframe, text="Last name: ", foreground='violet red', font=('times', 12, 'bold'))
        self.lnamelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.lnameentry = ttk.Entry(self.lnameframe)
        self.lnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Age
        self.ageframe = ttk.Frame(self)
        self.ageframe.pack(side=TOP, expand=1, fill=BOTH)
        self.agelabel = ttk.Label(
            self.ageframe, text="Age: *", foreground='violet red', font=('times', 12, 'bold'))
        self.agelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.ageentry = ttk.Entry(self.ageframe)
        self.ageentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Gender
        self.genderframe = ttk.Frame(self)
        self.genderframe.pack(side=TOP, expand=1, fill=BOTH)
        self.genderlabel = ttk.Label(
            self.genderframe, text="Gender: *", foreground='violet red', font=('times', 12, 'bold'))
        self.genderlabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.genderentry = ttk.Entry(self.genderframe)
        self.genderentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Ethnicity
        self.ethnicframe = ttk.Frame(self)
        self.ethnicframe.pack(side=TOP, expand=1, fill=BOTH)
        self.ethniclabel = ttk.Label(
            self.ethnicframe, text="Ethnicity: *", foreground='violet red', font=('times', 12, 'bold'))
        self.ethniclabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.ethnicentry = ttk.Entry(self.ethnicframe)
        self.ethnicentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Disability
        self.disabilityframe = ttk.Frame(self)
        self.disabilityframe.pack(side=TOP, expand=1, fill=BOTH)
        self.disabilitylabel = ttk.Label(
            self.disabilityframe, text="Disability: *", foreground='violet red', font=('times', 12, 'bold'))
        self.disabilitylabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.disabilityentry = ttk.Entry(self.disabilityframe)
        self.disabilityentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Mandatory Fields - this label will display when respondent tries to submit form without filling in information required in mandatory fields
        self.mfframe = ttk.Frame(self)
        self.mfframe.pack(side=TOP, expand=1, fill=BOTH)
        self.mftext = ttk.Label(
            self.mfframe, text="* mandatory fields are required", foreground='black', font=('times', 10, 'bold italic'))
        self.mftext.pack(side=TOP, expand=1,
                         fill=BOTH, padx=5, pady=5)


class Secondframe(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width=500, height=600)
        self.pack(side=TOP, expand=1, fill=BOTH)

        # Widget Styling - Labels, Entrys, Buttons
        self.apply_style = ttk.Style()
        self.apply_style.configure('TLabel', foreground="violet red",
                                   font=("Helvetica", 12, "bold"))
        self.apply_style.configure('TEntry', foreground="black",
                                   background="WhiteSmoke", font=("Helvetica", 12, "bold"), bd=2)
        self.apply_style.configure('TButton', foreground="violet red",
                                   background="MistyRose", font=("Helvetica", 12, "bold"))
        self.apply_style.configure('TRadiobutton', foreground="violet red",
                                   font=("times new roman", 10, "bold"))

        # Create Second -Child-  Form Page
        # Information Frame
        self.labelframe2 = ttk.Frame(self)
        self.labelframe2.pack(side=TOP, expand=1, fill=BOTH)
        self.textlabel2 = ttk.Label(
            self.labelframe2, text="Kindly select the option that best describes your experience so far", foreground='violet red', font=('times', 12, 'bold italic'))
        self.textlabel2.pack(side=TOP, expand=1,
                             fill=X, padx=5, pady=5)
        # Question 1
        self.q1_frame = ttk.Frame(self)
        self.q1_frame.pack(side=TOP, expand=1, fill=BOTH)
        self.q1_variable = tk.BooleanVar()
        self.q1_label = ttk.Label(
            self.q1_frame, text="1. Did you enjoy your tour around the singing sculpture? ", foreground='violet red', font=('times', 12, 'bold'))
        self.q1_label.pack(side=TOP, expand=1, fill=BOTH, padx=5, anchor=W)
        self.q1_radioframe = ttk.Frame(self.q1_frame)
        self.q1_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q1_firstradio = ttk.Radiobutton(
            self.q1_radioframe, text='Yes', value="Yes", variable=self.q1_variable, style='TRadiobutton')
        self.q1_firstradio.pack(
            side=TOP, expand=1, padx=(20, 25), pady=2, anchor=W)
        self.q1_secondradio = ttk.Radiobutton(
            self.q1_radioframe, text='No', value="No", variable=self.q1_variable, style='TRadiobutton')
        self.q1_secondradio.pack(
            side=TOP, expand=1, padx=(20, 25), pady=2, anchor=W)
        # Question 2
        self.q2_frame = ttk.Frame(self)
        self.q2_frame.pack(side=TOP, expand=1, fill=BOTH)
        self.q2_variable = tk.BooleanVar()
        self.q2_label = ttk.Label(
            self.q2_frame, text="2. Are you curious as to how the Ukulele sings? ")
        self.q2_label.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.q2_radioframe = ttk.Frame(self.q2_frame)
        self.q2_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q2_firstradio = ttk.Radiobutton(
            self.q2_frame, text='Yes', value="Yes", variable=self.q2_variable, style='TRadiobutton')
        self.q2_firstradio.pack(side=TOP, expand=1,
                                padx=(20, 25), pady=2, anchor=W)
        self.q2_secondradio = ttk.Radiobutton(
            self.q2_frame, text='No', value="No", variable=self.q2_variable, style='TRadiobutton')
        self.q2_secondradio.pack(side=TOP, expand=1,
                                 padx=(20, 25), pady=2, anchor=W)
        # Question 3
        self.q3_frame = ttk.Frame(self)
        self.q3_frame.pack(side=TOP, expand=1, fill=BOTH)
        self.q3_variable = tk.BooleanVar()
        self.q3_label = ttk.Label(
            self.q3_frame, text="3. Will you like to know more about the science of acoustics? ")
        self.q3_label.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.q3_radioframe = ttk.Frame(self.q3_frame)
        self.q3_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q3_firstradio = ttk.Radiobutton(
            self.q3_frame, text='Yes', value="Yes", variable=self.q3_variable, style='TRadiobutton')
        self.q3_firstradio.pack(side=TOP, expand=1,
                                padx=(20, 25), pady=2, anchor=W)
        self.q3_secondradio = ttk.Radiobutton(
            self.q3_frame, text='No', value="No", variable=self.q3_variable, style='TRadiobutton')
        self.q3_secondradio.pack(side=TOP, expand=1,
                                 padx=(20, 25), pady=2, anchor=W)
        # Question 4
        self.q4_frame = ttk.Frame(self)
        self.q4_frame.pack(side=TOP, expand=1, fill=BOTH)
        self.q4_variable = tk.BooleanVar()
        self.q4_label = ttk.Label(
            self.q4_frame, text="4. Will you attend future science events organised by the sponsors? ")
        self.q4_label.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.q4_radioframe = ttk.Frame(self.q4_frame)
        self.q4_radioframe.pack(side=TOP, expand=1, fill=BOTH)
        self.q4_firstradio = ttk.Radiobutton(
            self.q4_frame, text='Yes', value="Yes", variable=self.q4_variable, style='TRadiobutton')
        self.q4_firstradio.pack(side=TOP, expand=1,
                                padx=(20, 25), pady=2, anchor=W)
        self.q4_secondradio = ttk.Radiobutton(
            self.q4_frame, text='No', value="No", variable=self.q4_variable, style='TRadiobutton')
        self.q4_secondradio.pack(side=TOP, expand=1,
                                 padx=(20, 25), pady=2, anchor=W)
        # Email
        self.emailframe = ttk.Frame(self)
        self.emailframe.pack(side=TOP, expand=1, fill=BOTH)
        self.emaillabel = ttk.Label(
            self.emailframe, text="Email: *", foreground='violet red', font=('times', 12, 'bold'))
        self.emaillabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.emailentry = ttk.Entry(self.emailframe)
        self.emailentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)


class Mainwindow():
    def __init__(self, master):
        # Title Frame
        self.topframe = ttk.Frame(master)
        self.topframe.pack(side=TOP)
        self.titlelabel = ttk.Label(
            self.topframe, text='UKULELE!!!', foreground='violet red', font=('times', 20, 'bold'))
        self.titlelabel.pack(padx=5, pady=5, anchor=CENTER)
        # Create mainframe to act as parent for subframes
        mainframe = ttk.Frame(master)
        mainframe.pack(expand=1, fill=BOTH)
        self.windowNum = 0

        # Putting frames into parent window
        self.framelist = []
        self.framelist.append(Firstframe(mainframe))
        self.framelist.append(Secondframe(mainframe))
        self.framelist[1].forget()

        # Create buttons to switch frames
        bottomframe = ttk.Frame(master)
        bottomframe.pack(side=BOTTOM)
        switchbutton = ttk.Button(
            bottomframe, text='>>>', cursor='hand2', command=self.switchframe)
        switchbutton.pack(side=LEFT, expand=1, padx=(
            20, 25), pady=2, anchor=CENTER)
        self.submitbutton = ttk.Button(
            bottomframe, text='Submit', cursor='hand2', command=self.submitform, state="disabled")  # Submit button is disabled in the first window
        self.submitbutton.pack(side=RIGHT, expand=1,
                               padx=(20, 25), pady=2, anchor=CENTER)

    def switchframe(self):
        self.framelist[self.windowNum].forget()
        self.windowNum = (self.windowNum+1) % len(self.framelist)
        # Using the tk.raise() method to switch form frames
        self.framelist[self.windowNum].tkraise()
        # Packing the current frame as the .forget() method unpacks whichever frame is current
        self.framelist[self.windowNum].pack(expand=1, fill=BOTH, pady=5)
        # Activate submit button in next frame
        self.submitbutton.config(state="normal")

    def submitform(self):
        pass


if __name__ == "__main__":
    root = tk.Toplevel()
    root.title("UKULELE - Survey Form")
    root.geometry('600x700+342+0')
    root.iconimage = PhotoImage(file='images/icon_img.ico')
    root.iconphoto(False, root.iconimage)
    root.minsize(100, 100)
    root.resizable(0, 0)
    window = Mainwindow(root)
    root.mainloop()
