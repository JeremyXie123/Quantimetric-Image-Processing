import tkinter as tk
from tkinter import ttk

from pathlib import Path
from tkinter import filedialog as fd
import os

from tkinter_custom.extra_functions import getImage
from PIL import Image, ImageTk

class single_action_panel(tk.Frame):
    def __init__(self, master, title):
        tk.Frame.__init__(self, master)
        self.LabelFrame = ttk.LabelFrame(self, text=title)
        self.LabelFrame.grid(row=0, column=0, sticky="NEWS")

        self.ApplyButton = ttk.Button(self.LabelFrame,text="Apply")
        self.ApplyButton.grid(row=0, column=0)

        self.SelectedLabel = ttk.Label(self.LabelFrame, text="----")
        self.SelectedLabel.grid(row=1, column=0)

        self.ListBox = tk.Listbox(self.LabelFrame)
        self.ListBox.grid(row=2, column=0, sticky='NEWS')

        self.scrollbar = ttk.Scrollbar(self.LabelFrame, command=self.ListBox.yview)
        self.scrollbar.grid(row=2, column=1, sticky='NS')
        self.ListBox.config(yscrollcommand=self.scrollbar.set)
        self.ListBox.config(height=16)

        for values in range(100):
            self.ListBox.insert("end", values)




