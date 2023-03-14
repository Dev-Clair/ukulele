import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *

# Widget Styling
apply_style = ttk.Style()
apply_style.configure('TLabel', foreground="violet red",
                      font=("Helvetica", 12, "bold"))
apply_style.configure('TEntry', foreground="black",
                      background="WhiteSmoke", font=("sans serif", 12, "bold"), bd=2)
apply_style.configure('TButton', foreground="violet red",
                      background="MistyRose", font=("Helvetica", 12, "bold"))
apply_style.configure('TRadiobutton', foreground="violet red",
                      font=("Helvetica", 12, "bold"))


class Create_top(tk.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master


class Create_frame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master


class Create_label(ttk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TLabel')
        self.master = master


class Create_entry(ttk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TEntry')
        self.master = master


class Create_button(ttk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TButton')
        self.master = master


class Create_radbutton(ttk.Radiobutton):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs, style='TRadiobutton')
        self.master = master
