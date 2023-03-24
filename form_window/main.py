import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *
from tkinter.messagebox import showerror, showinfo, askokcancel
from tkcalendar import Calendar
from PIL import ImageTk, Image
import time
from datetime import *
# from database.form_database import addrecord  # Import -sqlite3- Database


class Mainframe:
    def __init__(self, master):
        self.master = master
        self.master.title("UKULELE")
        self.master.geometry('1350x680+5+5')
        self.master.iconimage = PhotoImage(file='images/icon_img.ico')
        self.master.iconphoto(True, self.master.iconimage)
        self.master.minsize(100, 100)
        self.master.resizable(0, 0)

        # Widget Styling
        apply_style = ttk.Style(master)
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
        # apply_style.configure('TLabelFrame', foreground="violet red",
        #                       font=("Helvetica", 10, "bold"))
        apply_style.configure('TSeparator', foreground="black")

        # Create Page Top Frame
        topframe = ttk.Frame(master)
        topframe.pack(side=TOP, fill=X, anchor=NW)
        # Top Label
        slidertext = 'UKULELE - \"The Singing Sculpture\"'  # Slider Text
        self.topLabel = ttk.Label(
            topframe, text=slidertext, style='TLabel')
        self.topLabel.config(font=("Bell MT", 30, "bold"))
        self.topLabel.pack(side=LEFT, anchor=W, padx=5)
        # Admin Log-in Button
        self.topButton = ttk.Button(
            topframe, text='Admin Log-in', cursor='hand2', style='TButton', command=self.adminlogin)
        self.topButton.pack(side=RIGHT, anchor=E, padx=5)

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

        # Create Frame for Label and Survey Button
        bottomframe = ttk.Frame(master)
        bottomframe.pack(side=TOP, fill=X,
                         anchor=CENTER, pady=20)
        # Create Label and Button
        self.surveyLabel = ttk.Label(
            bottomframe, text="Kindly Click on the Button Below to Take a Quick 60 Secs Survey", style='TLabel')
        self.surveyLabel.config(font=("Bell MT", 20, "bold"))
        self.surveyLabel.pack(side=TOP, anchor=CENTER, pady=10)
        self.surveyButton = ttk.Button(
            bottomframe, text="Take Survey", width=20, style='TButton', command=self.takesurvey)
        self.surveyButton.pack(side=TOP, anchor=CENTER, pady=10)

        # Create Copyright Label
        self.cpyrightLabel = ttk.Label(
            master, text="© Copyright 2023 | Lexi-Clair Designs", style='TLabel')
        self.cpyrightLabel.config(font=("times new roman", 8, "bold"))
        self.cpyrightLabel.config(foreground="blue")
        self.cpyrightLabel.config(background="light grey")
        self.cpyrightLabel.pack(side=BOTTOM, fill=X,
                                anchor=W, pady=(10, 0))

    # Admin Log-in Toplevel
    def adminlogin(self):
        """
            Launches a toplevel window for administrative authentication details
        """
        self.admin_win = tk.Toplevel()
        self.admin_win.title('Admin Login')
        self.admin_win.geometry("350x350+325+100")
        self.admin_win.resizable(0, 0)

        self.admin_img = PhotoImage(
            file='images/person_imgL.png')
        self.login_img = ttk.Label(
            self.admin_win, image=self.admin_img, justify=CENTER)
        self.login_img.grid(row=0, columnspan=2, padx=2, pady=10)
        # create Label Widgets
        self.usernamelabel = ttk.Label(
            self.admin_win, text="Admin Id:", style='TLabel', justify=LEFT)
        self.usernamelabel.grid(row=1, column=0, padx=2, pady=10)
        self.passwordlabel = ttk.Label(
            self.admin_win, text="Password:", style='TLabel', justify=LEFT)
        self.passwordlabel.grid(row=2, column=0, padx=2, pady=10)
        self.forgetlabel = ttk.Label(
            self.admin_win, text="forgot password? default password is surname in lowercase", style='TLabel', justify=LEFT)
        self.forgetlabel.config(font=("times", 8, "normal"))
        self.forgetlabel.grid(row=3, columnspan=2, padx=2, pady=(2, 3))
        # Create Entry Widgets
        self.uservar = tk.StringVar()
        self.usernameentry = ttk.Entry(
            self.admin_win, textvariable=self.uservar, width=40, justify=CENTER)
        self.usernameentry.grid(row=1, column=1, padx=2, pady=10)
        self.passvar = tk.StringVar()
        self.passwordentry = ttk.Entry(
            self.admin_win, textvariable=self.passvar, width=40, justify=CENTER, show="*")
        self.passwordentry.grid(row=2, column=1, padx=2, pady=10)
        # Create log-in Button
        self.logbutton = ttk.Button(
            self.admin_win, text="Log-in", command=self.adlog, style='TButton')
        self.logbutton.grid(row=4, columnspan=2, padx=2, pady=10)

        # Direct input focus to the first entry widget of the log-in window
        self.usernameentry.focus_set()

    # Admin Login Toplevel Functions
    def adlog(self):
        """
            Allows access to serverside / admin window
        """
        if self.uservar.get() == "admin" and self.passvar.get() == "ukulele":
            showinfo('Welcome', 'Log-in Successful', parent=self.admin_win)
            self.admin_win.quit()
            # import adminwindow

        if self.uservar.get() != "admin" and self.passvar.get() != "ukulele":
            showerror("Error", "Please enter the correct log-in details",
                      parent=self.admin_win)
            self.usernameentry.delete(0, END)
            self.passwordentry.delete(0, END)
            self.usernameentry.focus_set()

        if self.uservar.get() == "" and self.passvar.get() == "":
            showerror(
                "Error", "Username or Password fields cannot be empty", parent=self.admin_win)
            self.usernameentry.focus_set()

    # Survey Form Toplevel
    def takesurvey(self):
        """
            Launches a top level window of the surveyform to read input from user/respondent at runtime
        """
        self.survey_win = tk.Toplevel()
        self.survey_win.title("UKULELE - Survey Form")
        self.survey_win.geometry("550x650+342+20")
        self.master.minsize(100, 100)
        self.survey_win.resizable(0, 0)

        # Create Main Frame
        mainframe = ttk.Frame(self.survey_win)
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

        # Create Bottom Frame for Submit Button
        bottomframe = ttk.Frame(self.survey_win)
        bottomframe.pack(side=BOTTOM)
        # Create Submit Button for Survey Form
        self.submitbutton = ttk.Button(
            bottomframe, text='Submit', cursor='hand2', command=self.submitform)
        self.submitbutton.pack(side=RIGHT, expand=1,
                               padx=(20, 25), pady=2, anchor=CENTER)

        # Direct input focus to the first entry widget of the survey form
        self.identry.focus_set()

    # Survey Form Toplevel Functions
    def select_DOB(self, event):
        self.dob_window = tk.Toplevel()
        self.dob_window.grab_set()
        self.dob_window.title("Select Date of Birth")
        self.dob_window.geometry("350x250+450+100")
        self.cal = Calendar(
            self.dob_window, selectmode="day", datepattern="dd/mm/yyyy", background="violet red", foreground="white", headersforeground="violet red", selectforeground="violet red", headersbackground="white", )
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
        # Insert Current Age into Age Widget
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
