
from tkinter import ttk

class multi_img_tab(ttk.Notebook):
    def __init__(self, master, name):
        ttk.Notebook.__init__(self, master)

        master.add(self,text=name)
