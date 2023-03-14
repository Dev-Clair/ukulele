import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter.constants import *


class _window():
    def __init__(self, master, **kwargs):
        mainframe = ttk.Frame(master)
        mainframe.pack(expand=1, fill=BOTH, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    window = _window(root)
    root.mainloop()
