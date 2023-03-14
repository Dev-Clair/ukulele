from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from widgetswindow import Create_frame, Create_top, Create_label, Create_entry, Create_button


class Survey_win(Tk):
    def __init__(self):
        super().__init__()
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.title("UKULELE")
        self.geometry('1366x768+0+0')
        # self.iconimage = PhotoImage(file='images/icon_img.ico')
        # self.iconphoto(True, self.iconimage)
        self.minsize(100, 100)
        self.resizable(0, 0)

    def create_widgets(self):
        # Create top frame to hold slider text and admin log-in button
        self.topFrame = Create_frame(
            self, width=1300, height=200, relief=FLAT)
        self.topFrame.pack(side=TOP)
        # Create slider label
        self.slidertext = StringVar(
            value="UKULELE - \"The Singing Sculpture\"")
        self.topLabel = Create_label(
            self.topFrame, textvariable=self.slidertext)
        self.topLabel.config(font=('', 30, 'bold'))
        self.topLabel.place(x=10, y=10)
        # Create admin log-in button
        self.topButton = Create_button(
            self.topFrame, text='Admin Log-in', cursor='hand2')
        self.topButton.place(x=1250, y=10)

        # Create middle frame to hold welcome message
        self.midFrame = Create_frame(
            self, width=1300, height=200, relief=FLAT)
        self.midFrame.pack(side=TOP)
        # Create Texts
        self.firstWelcometext = StringVar(value="WELCOME TO UKULELE!!!")
        self.secondWelcometext = StringVar(
            value="We are glad you are here!!!")
        self.thirdWelcometext = StringVar(
            value="Will you like to share your experience?")
        # Create Labels
        self.firstwelcomeLabel = Label(
            self.midFrame, textvariable=self.firstWelcometext)
        self.firstwelcomeLabel.config(font=('', 40, 'bold'))
        self.firstwelcomeLabel.pack(padx=2, pady=5)
        self.secondwelcomeLabel = Label(
            self.midFrame, textvariable=self.secondWelcometext)
        self.secondwelcomeLabel.config(font=('', 25, 'bold'))
        self.secondwelcomeLabel.pack(padx=2, pady=(5, 0))
        self.thirdwelcomeLabel = Label(
            self.midFrame, textvariable=self.thirdWelcometext)
        self.thirdwelcomeLabel.config(font=('', 20, 'bold'))
        self.thirdwelcomeLabel.pack(padx=2, pady=(5, 0))
        # Create bottom frame to hold survey message label and button
        self.bottomFrame = Create_frame(
            self, width=1300, height=200, relief=FLAT)
        self.bottomFrame.pack(side=TOP)
        self.surveytext = StringVar(
            value="Kindly click the button to take the 60 seconds survey")
        self.surveyLabel = Create_label(
            self.bottomFrame, textvariable=self.surveytext)
        self.surveyLabel.pack(padx=5, pady=(5, 0))
        self.surveyLabel.config(font=('', 25, 'bold'))
        self.surveyButton = Create_button(
            self.bottomFrame, text="Take Survey", cursor='hand2', command=self.take_survey)
        self.surveyButton.pack(padx=5, pady=(5, 0))

    def take_survey(self):
        """
            Launches a toplevel window of the survey form
            takes inputs from user and updates local storage
            returns to main window and waits for another user event
        """
        self.topwin = Create_top(self)
        self.topwin.grab_set()
        self.topwin.title("UKULELE - Survey Form")
        self.topwin.geometry("900x700")
        self.topwin.resizable(0, 0)


if __name__ == "__main__":
    sw = Survey_win()
    sw.mainloop()
