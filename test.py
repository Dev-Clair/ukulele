from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *

sf = Toplevel()
sf.title("UKULELE - Survey Form")
sf.geometry('350x450+342+0')
sf.iconimage = PhotoImage(file='images/icon_img.ico')
sf.iconphoto(False, sf.iconimage)
sf.minsize(100, 100)
sf.resizable(0, 0)

if __name__ == "__main__":
    sf.mainloop()
