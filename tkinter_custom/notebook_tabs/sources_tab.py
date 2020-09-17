import tkinter as tk
from tkinter import ttk
from tkinter_custom.extra_widgets.info_panel import info_panel

class sources_tab(ttk.Notebook):
    def __init__(self, master, name):
        ttk.Notebook.__init__(self, master)

        purpose = "This project was created as a demonstration of concepts surrounding image processing, such as HDR.\nThe project was inspired by Steve Mann's [HDR Instructables]\nFeel free to modify and/or copy to any extent!"
        self.Purpose_Panel = info_panel(self, "Purpose", purpose, 43, 10)
        self.Purpose_Panel.grid(row=0, column=0,sticky="NEWS")

        sources = "Mann Eyetap Org:\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"
        self.Source_Panel = info_panel(self, "Sources", sources, 43, 10)
        self.Source_Panel.grid(row=0, column=1, sticky="NEWS")
        master.add(self, text=name)
