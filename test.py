"""
    Procedural Style
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *
from widgetswindow import Create_frame, Create_label, Create_entry, Create_button, Create_radbutton

sf = Toplevel()
sf.title("UKULELE - Survey Form")
sf.geometry('350x450+342+0')
# sf.iconimage = PhotoImage(file='images/icon_img.ico')
# sf.iconphoto(False, sf.iconimage)
sf.minsize(100, 100)
sf.resizable(0, 0)

global windowNum
global framelist
global parentframe


def nextframe():
    framelist[windowNum.forget()]
    windowNum = ((windowNum + 1) % len(framelist))
    framelist[windowNum].tkraise()
    framelist[windowNum].pack(side=TOP, expand=1, fill=BOTH, pady=(0, 5))


# Create main frame - survey form
mainForm = Create_frame(sf)

# CREATE TOP FRAME FOR TITLE AND LABEL
topframe = Create_frame(mainForm)
topframe.pack(side=TOP, expand=1, fill=BOTH, pady=(0, 5))
# Frame Title
titletext = StringVar(
    value="UKULELE!!!")
frametitle = Create_label(
    topframe, textvariable=titletext)
frametitle.pack(side=TOP, pady=(0, 5))
frametitle.config(font=('times', 25, 'bold'))

# CREATE MIDDLE PARENT and CHILD FRAMES FOR LABELS AND ENTRY FIELDS
# Create Parent Frame
parentframe = Create_frame(mainForm)
parentframe.pack(side=TOP, expand=1, fill=BOTH, pady=(0, 5))

# framelist.append(firstframe(parentframe))
# framelist.append(secondframe(parentframe))
# framelist.forget[1]

# Create First -Child-  Form Page
firstframe = Create_frame(parentframe)
firstframe.pack(side=TOP, expand=1, fill=BOTH, pady=10)
# Toplabel Message
currentlabelframe = Create_frame(firstframe)
currentlabelframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
currenttext = StringVar(
    value="Kindly fill in the right information into the fields below")
currentlabel = Create_label(
    currentlabelframe, textvariable=currenttext)
currentlabel.pack(side=TOP, padx=5, pady=(0, 10))
currentlabel.config(font=('times', 15, 'bold italic'))
# id/Tag No.
idframe = Create_frame(firstframe)
idframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
idlabel = Create_label(idframe, text="Id/Tag No: *")
idlabel.pack(side=TOP, expand=1, padx=5, anchor=W)
identry = Create_entry(idframe)
identry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
# First Name
fnameframe = Create_frame(firstframe)
fnameframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
fnamelabel = Create_label(fnameframe, text="First name: ")
fnamelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
fnameentry = Create_entry(fnameframe)
fnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
# Last Name
lnameframe = Create_frame(firstframe)
lnameframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
lnamelabel = Create_label(lnameframe, text="Last name: ")
lnamelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
lnameentry = Create_entry(lnameframe)
lnameentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
# Age
ageframe = Create_frame(firstframe)
ageframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
agelabel = Create_label(ageframe, text="Age: *")
agelabel.pack(side=TOP, expand=1, padx=5, anchor=W)
ageentry = Create_entry(ageframe)
ageentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
# Gender
genderframe = Create_frame(firstframe)
genderframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
genderlabel = Create_label(genderframe, text="Gender: *")
genderlabel.pack(side=TOP, expand=1, padx=5, anchor=W)
genderentry = Create_entry(genderframe)
genderentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
# Ethnicity
ethnicframe = Create_frame(firstframe)
ethnicframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
ethniclabel = Create_label(ethnicframe, text="Ethnicity: *")
ethniclabel.pack(side=TOP, expand=1, padx=5, anchor=W)
ethnicentry = Create_entry(ethnicframe)
ethnicentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
# Disability
disabilityframe = Create_frame(firstframe)
disabilityframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
disabilitylabel = Create_label(disabilityframe, text="Disability: *")
disabilitylabel.pack(side=TOP, expand=1, padx=5, anchor=W)
disabilityentry = Create_entry(disabilityframe)
disabilityentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)

# Create Second -Child-  Form Page
secondframe = Create_frame(parentframe)
secondframe.pack(side=TOP, expand=1, fill=BOTH, pady=10)
# Toplabel Message
nextlabelframe = Create_frame(secondframe)
nextlabelframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
nexttext = StringVar(
    value="Kindly select the option that best describes your experience so far")
secondlabel = Create_label(
    nextlabelframe, textvariable=nexttext)
secondlabel.pack(side=TOP, padx=5, pady=(5))
secondlabel.config(font=('times', 15, 'bold italic'))
# Question 1
q1_frame = Create_frame(secondframe)
q1_frame.pack(side=TOP, expand=1, fill=BOTH)
q1_variable = BooleanVar()
q1_label = Create_label(
    q1_frame, text="1. Did you enjoy your tour around the singing sculpture? ")
q1_label.pack(side=TOP, expand=1, fill=BOTH, padx=5, anchor=W)
q1_radioframe = Create_frame(q1_frame)
q1_radioframe.pack(side=TOP, expand=1, fill=BOTH)
q1_firstradio = Create_radbutton(
    q1_radioframe, text='Yes', value="Yes", variable=q1_variable)
q1_firstradio.pack(side=TOP, expand=1, padx=(20, 25), pady=2, anchor=W)
q1_secondradio = Create_radbutton(
    q1_radioframe, text='No', value="No", variable=q1_variable)
q1_secondradio.pack(side=TOP, expand=1, padx=(20, 25), pady=2, anchor=W)
# Question 2
q2_frame = Create_frame(secondframe)
q2_frame.pack(side=TOP, expand=1, fill=BOTH)
q2_variable = BooleanVar()
q2_label = Create_label(
    q2_frame, text="2. Are you curious as to how the Ukulele sings? ")
q2_label.pack(side=TOP, expand=1, padx=5, anchor=W)
q2_radioframe = Create_frame(q2_frame)
q2_radioframe.pack(side=TOP, expand=1, fill=BOTH)
q2_firstradio = Create_radbutton(
    q2_frame, text='Yes', value="Yes", variable=q2_variable)
q2_firstradio.pack(side=TOP, expand=1,
                   padx=(20, 25), pady=2, anchor=W)
q2_secondradio = Create_radbutton(
    q2_frame, text='No', value="No", variable=q2_variable)
q2_secondradio.pack(side=TOP, expand=1,
                    padx=(20, 25), pady=2, anchor=W)
# Question 3
q3_frame = Create_frame(secondframe)
q3_frame.pack(side=TOP, expand=1, fill=BOTH)
q3_variable = BooleanVar()
q3_label = Create_label(
    q3_frame, text="3. Will you like to know more about the science of acoustics? ")
q3_label.pack(side=TOP, expand=1, padx=5, anchor=W)
q3_radioframe = Create_frame(q3_frame)
q3_radioframe.pack(side=TOP, expand=1, fill=BOTH)
q3_firstradio = Create_radbutton(
    q3_frame, text='Yes', value="Yes", variable=q3_variable)
q3_firstradio.pack(side=TOP, expand=1,
                   padx=(20, 25), pady=2, anchor=W)
q3_secondradio = Create_radbutton(
    q3_frame, text='No', value="No", variable=q3_variable)
q3_secondradio.pack(side=TOP, expand=1,
                    padx=(20, 25), pady=2, anchor=W)
# Question 4
q4_frame = Create_frame(secondframe)
q4_frame.pack(side=TOP, expand=1, fill=BOTH)
q4_variable = BooleanVar()
q4_label = Create_label(
    q4_frame, text="4. Will you attend future science events organised by the sponsors? ")
q4_label.pack(side=TOP, expand=1, padx=5, anchor=W)
q4_radioframe = Create_frame(q3_frame)
q4_radioframe.pack(side=TOP, expand=1, fill=BOTH)
q4_firstradio = Create_radbutton(
    q4_frame, text='Yes', value="Yes", variable=q4_variable)
q4_firstradio.pack(side=TOP, expand=1,
                   padx=(20, 25), pady=2, anchor=W)
q4_secondradio = Create_radbutton(
    q4_frame, text='No', value="No", variable=q4_variable)
q4_secondradio.pack(side=TOP, expand=1,
                    padx=(20, 25), pady=2, anchor=W)
# Question 5
emailframe = Create_frame(secondframe)
emailframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
emaillabel = Create_label(
    emailframe, text="Email: ")
emaillabel.pack(side=TOP, expand=1, padx=5, anchor=W)
emailentry = Create_entry(emailframe)
emailentry.pack(side=TOP, expand=1, fill=X, padx=5, anchor=W)
# Submit Button
submitbutton = Create_button(secondframe, text='Submit')
submitbutton.pack(side=TOP, expand=1, anchor=CENTER, pady=(10))

# CREATE BOTTOM PARENT AND CHILD FRAMES FOR BUTTONS AND LABEL
bottomframe = Create_frame(mainForm)
bottomframe.pack(side=TOP, expand=1, fill=BOTH, pady=(0, 5))
# Create button frame
buttonframe = Create_frame(bottomframe)
buttonframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
# Create back button to switch survey frames backwards
backbutton = Create_button(buttonframe, text="<<<")
backbutton.pack(side=LEFT, padx=(20, 0), anchor=W)
# Create next button to switch survey frames forward
nextbutton = Create_button(buttonframe, text=">>>", command=lambda: nextframe)
nextbutton.pack(side=RIGHT, padx=(0, 20), anchor=E)
# Create label frame
labelframe = Create_frame(bottomframe)
labelframe.pack(side=TOP, expand=1, fill=BOTH, pady=5)
# Create label to display form page number
pagenumber = StringVar(value="1/1")
pagelabel = Create_label(
    labelframe, textvariable=pagenumber)
pagelabel.pack(side=BOTTOM, anchor=S)

# Display main frame - survey form
mainForm.pack(padx=10, pady=20)
# mainForm.pack_propagate(True)


if __name__ == "__main__":
    sf.mainloop()
