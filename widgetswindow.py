from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *

# Widget Styling
apply_style = Style()
apply_style.configure('TLabel', foreground="violet red",
                      font=("Helvetica", 12, "bold"))
apply_style.configure('TEntry', foreground="black",
                      background="WhiteSmoke", font=("sans serif", 12, "bold"), bd=2)
apply_style.configure('TButton', foreground="violet red",
                      background="MistyRose", font=("Helvetica", 12, "bold"))
apply_style.configure('TRadiobutton', foreground="violet red",
                      font=("Helvetica", 12, "bold"))


class Create_top(Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master


class Create_frame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master


class Create_label(Label):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TLabel')
        self.master = master


class Create_entry(Entry):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TEntry')
        self.master = master


class Create_button(Button):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TButton')
        self.master = master


class Create_radbutton(Radiobutton):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TRadiobutton')
        self.master = master
