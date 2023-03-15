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

        # Widget Styling - Labels, Entrys, Buttons
        self.apply_style = ttk.Style()
        self.apply_style.configure('TLabel', foreground="violet red",
                                   font=("Helvetica", 12, "bold"))
        self.apply_style.configure('TEntry', foreground="blue",
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
                             fill=BOTH, padx=5, pady=5)
        # Question 1
        self.q1_frame = ttk.Frame(self)
        self.q1_frame.pack(side=TOP, expand=1, fill=BOTH)
        self.q1_variable = tk.BooleanVar()
        self.q1_label = ttk.Label(
            self.q1_frame, text="1. Did you enjoy your tour around the singing sculpture? ")
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
            self.emailframe, text="Email: ", foreground='violet red', font=('times', 12, 'bold'))
        self.emaillabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.emailentry = ttk.Entry(self.emailframe)
        self.emailentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)


class Mainwindow():
    def __init__(self, master):
        """
            contains a top frame which holds the title label - "UKULELE"
            a mainframe which serves as a parent or container window to two child frames - Firstframe and Secondframe
            and a bottom frame which holds two buttons
            the ">>>" button allows us to move from one page to the other while the submit button submits entries entered by the user.
            The submit button is temporarily disabled while the respondent fills the information in the first window and comes normal when the respondent switches to the next frame 
        """
        # Create Title Frame for Title Label
        topframe = ttk.Frame(master)
        topframe.pack(side=TOP)
        titlelabel = ttk.Label(
            topframe, text='UKULELE!!!', foreground='violet red', font=('times', 20, 'bold'))
        titlelabel.pack(padx=5, pady=5, anchor=CENTER)

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
        switchbutton = ttk.Button(
            bottomframe, text='>>>', cursor='hand2', command=self.switchframe)
        switchbutton.pack(side=LEFT, expand=1, padx=(
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
    root.title("UKULELE - Survey Form")
    root.geometry('500x600+342+50')
    root.iconimage = PhotoImage(file='images/icon_img.ico')
    root.iconphoto(False, root.iconimage)
    root.minsize(100, 100)
    root.resizable(0, 0)
    window = Mainwindow(root)
    root.mainloop()
