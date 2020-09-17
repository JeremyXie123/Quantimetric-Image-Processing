import tkinter as tk
from tkinter import ttk
from tkinter_custom.extra_functions import getImage
from tkinter_custom.extra_widgets.image_panel import image_loader
from tkinter_custom.extra_widgets.single_action_panel import single_action_panel
class single_img_tab(ttk.Notebook):
    def __init__(self, master, name):
        ttk.Notebook.__init__(self, master)

        self.LoadPanel = image_loader(self, "Input Image","1x1.png", 0)
        self.LoadPanel.grid(row=0, column=0, sticky="NEWS")

        self.Arrow1 = getImage("Arrow.png",30,30)
        ttk.Label(self,image=self.Arrow1).grid(row=0,column=1,sticky="NEWS")

        self.ActionPanel = single_action_panel(self, "Actions")
        self.ActionPanel.grid(row=0,column=2, sticky="NEWS")

        self.SavePanel = image_loader(self, "Output Image", "1x1.png", 1)
        self.SavePanel.grid(row=0, column=4, sticky="NEWS")

        ttk.Label(self, image=self.Arrow1).grid(row=0, column=3, sticky="NEWS")

        master.add(self, text=name)
