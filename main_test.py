import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel, askyesno, askyesnocancel
from PIL import ImageTk, Image


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
        self.master = master

        # Create Variables
        self.idvar = tk.StringVar()
        self.fnamevar = tk.StringVar()
        self.lnamevar = tk.StringVar()
        self.agevar = tk.StringVar()
        self.gendervar = tk.StringVar()
        self.ethnicvar = tk.StringVar()
        self.disabilityvar = tk.StringVar()

        # Create First -Child-  Form Page
        # Information Frame
        labelframe1 = ttk.Frame(self)
        labelframe1.pack(side=TOP, expand=1, fill=BOTH)
        self.textlabel1 = ttk.Label(
            labelframe1, text="Kindly fill in the right information into the fields below", foreground='violet red', font=('times', 12, 'bold italic'))
        self.textlabel1.pack(side=TOP, expand=1,
                             fill=BOTH, padx=5, pady=5)
        # id/Tag No.
        idframe = ttk.Frame(self)
        idframe.pack(side=TOP, expand=1, fill=BOTH)
        self.idlabel = ttk.Label(idframe, text="Id/Tag No: *",
                                 style='TLabel')
        self.idlabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.identry = ttk.Entry(idframe, textvariable=self.idvar)
        self.identry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # First Name
        fnameframe = ttk.Frame(self)
        fnameframe.pack(side=TOP, expand=1, fill=BOTH)
        self.fnamelabel = ttk.Label(
            fnameframe, text="First name: ", style='TLabel')
        self.fnamelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.fnameentry = ttk.Entry(
            fnameframe, textvariable=self.fnamevar)
        self.fnameentry.pack(side=TOP, expand=1, fill=X,
                             padx=5, anchor=W)
        # Last Name
        lnameframe = ttk.Frame(self)
        lnameframe.pack(side=TOP, expand=1, fill=BOTH)
        self.lnamelabel = ttk.Label(
            lnameframe, text="Last name: ", style='TLabel')
        self.lnamelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.lnameentry = ttk.Entry(
            lnameframe, textvariable=self.lnamevar)
        self.lnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Age
        ageframe = ttk.Frame(self)
        ageframe.pack(side=TOP, expand=1, fill=BOTH)
        self.agelabel = ttk.Label(
            ageframe, text="Age: *", style='TLabel')
        self.agelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.ageentry = ttk.Entry(ageframe, textvariable=self.agevar)
        self.ageentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Gender
        genderframe = ttk.Frame(self)
        genderframe.pack(side=TOP, expand=1, fill=BOTH)
        self.genderlabel = ttk.Label(
            genderframe, text="Gender: *", style='TLabel')
        self.genderlabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.genderentry = ttk.Entry(
            genderframe, textvariable=self.gendervar)
        self.genderentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Ethnicity
        ethnicframe = ttk.Frame(self)
        ethnicframe.pack(side=TOP, expand=1, fill=BOTH)
        self.ethniclabel = ttk.Label(
            ethnicframe, text="Ethnicity: *", style='TLabel')
        self.ethniclabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.ethnicentry = ttk.Entry(
            ethnicframe, textvariable=self.ethnicvar)
        self.ethnicentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Disability
        disabilityframe = ttk.Frame(self)
        disabilityframe.pack(side=TOP, expand=1, fill=BOTH)
        self.disabilitylabel = ttk.Label(
            disabilityframe, text="Disability: *", style='TLabel')
        self.disabilitylabel.pack(side=TOP, expand=1, padx=5, anchor=W)
        self.disabilityentry = ttk.Entry(
            disabilityframe, textvariable=self.disabilityvar)
        self.disabilityentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
        # Mandatory Fields - this label will display when respondent tries to submit form without filling in information required in mandatory fields
        # self.mfframe = ttk.Frame(self)
        # self.mfframe.pack(side=TOP, expand=1, fill=BOTH)
        # self.mftext = ttk.Label(
        #     self.mfframe, text="* mandatory fields are required", foreground='black', font=('times', 10, 'bold italic'))
        # self.mftext.pack(side=TOP, expand=1,
        #                  fill=BOTH, padx=5, pady=5)

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
        # Information Frame
        labelframe2 = ttk.Frame(self)
        labelframe2.pack(side=TOP, expand=1, fill=BOTH)
        self.textlabel2 = ttk.Label(
            labelframe2, text="Kindly select the option that best describes your experience so far", foreground='violet red', font=('times', 12, 'bold italic'))
        self.textlabel2.pack(side=TOP, expand=1,
                             fill=BOTH, padx=5, pady=5)
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


class Mainwindow(tk.Toplevel):
    def __init__(self, master):
        """
            contains a top frame which holds the title label - "UKULELE"
            a mainframe which serves as a parent or container window to two child frames - Firstframe and Secondframe
            and a bottom frame which holds two buttons
            the ">>>" button allows us to move from one page to the other while the submit button submits entries entered by the user.
            The submit button is temporarily disabled while the respondent fills the information in the first window and comes normal when the respondent switches to the next frame 
        """
        # self.master = master
        # self.master.title("UKULELE - Survey Form")
        # self.master.geometry('500x600+342+50')
        # self.master.iconimage = PhotoImage(file='images/icon_img.ico')
        # self.master.iconphoto(False, root.iconimage)
        # self.master.minsize(100, 100)
        # self.master.resizable(0, 0)
        self.master = master
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

        # Create Title Frame for Title Label
        topframe = ttk.Frame(master)
        topframe.pack(side=TOP)
        self.titlelabel = ttk.Label(
            topframe, text='UKULELE!!!', foreground='violet red', font=('times', 20, 'bold'))
        self.titlelabel.pack(padx=5, pady=5, anchor=CENTER)

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


class Mainframe:
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
        self.topframe = ttk.Frame(main_win, width=950, height=250)
        self.topframe.pack(side=TOP, expand=0, fill=BOTH,
                           anchor=N, padx=10, pady=(5, 20))
        # Create Slider Label
        global count, text  # , slidertext

        def slider():
            count = 0
            text = ""
            if count == len(self.slidertext):
                count == 0
                text = ""
            text = text+self.slidertext[count]
            topLabel.config(text=text)
            count += 1
            topLabel.after(300, slider)

        labelFrame = ttk.Frame(self.topframe)
        labelFrame.pack(side=LEFT, expand=1, anchor=W)
        # slider text
        self.slidertext = "UKULELE - \"The Singing Sculpture\""
        topLabel = ttk.Label(
            labelFrame, text=self.slidertext, style='TLabel')
        topLabel.config(font=("Bell MT", 30, "bold"))
        topLabel.pack(expand=1, fill=BOTH)
        # Create Admin Log-in Button
        buttonFrame = ttk.Frame(self.topframe)
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
        # import surveyform
        # pass
        self.opentop = Mainwindow(self)


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
