import tkinter as tk
from tkinter import ttk

class info_panel(tk.Frame):
    def __init__(self, master, title, text, sizex, sizey):
        tk.Frame.__init__(self, master)
        self.LabelFrame = ttk.LabelFrame(self, text=title)
        self.LabelFrame.grid(row=0, column=0, sticky="NEWS")

        self.TextBox = tk.Text(self.LabelFrame, width=sizex, height=sizey)
        self.TextBox.grid(row=0, column=0, sticky="NEWS")
        self.TextBox.insert('1.0', text)
        self.TextBox.config(wrap="word")

        self.scrollbar = ttk.Scrollbar(self, command=self.TextBox.yview)
        self.scrollbar.grid(row=0, column=1, sticky='NS')
        self.TextBox.config(yscrollcommand = self.scrollbar.set)

        self.TextBox.config(state="disabled")
