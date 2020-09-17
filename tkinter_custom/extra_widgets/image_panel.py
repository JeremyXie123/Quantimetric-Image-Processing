import tkinter as tk
from tkinter import ttk

from pathlib import Path
from tkinter import filedialog as fd
import os

from tkinter_custom.extra_functions import getImage
from PIL import Image, ImageTk

class image_loader(tk.Frame):
    def __init__(self, master, title, default, mode):
        tk.Frame.__init__(self, master)
        self.LabelFrame = ttk.LabelFrame(self, text=title)
        self.LabelFrame.grid(row=0, column=0, sticky="NEWS")

        if mode == 0:
            self.LoadButton = ttk.Button(self.LabelFrame, text="Load Image", command=self.load_callback)
        else:
            self.LoadButton = ttk.Button(self.LabelFrame, text="Save Image", command=self.save_callback)


        self.LoadButton.grid(row=0, column=0, sticky="NEWS")

        self.LoadedLabel = ttk.Label(self.LabelFrame, text="----")
        self.LoadedLabel.grid(row=1, column=0, sticky="NEWS")

        self.cur_image = getImage(default, 256, 256)

        self.ImageLabel = ttk.Label(self.LabelFrame,text="No Image Loaded",image = self.cur_image)
        self.ImageLabel.grid(row=2, column=0, sticky="NEWS")

    def load_callback(self):
        file = fd.askopenfile(title="Open an image", defaultextension=".png", initialdir=os.getcwd(),
                              filetypes=(("picture files", "*.png"), ("all files", "*.*")))
        if file is not None:
            self.cur_image = getImage(file.name,256,256)
            self.ImageLabel.config(image=self.cur_image)
            self.cur_path = Path(file.name)
            self.LoadedLabel.config(text=self.cur_path.relative_to(self.cur_path.parent.parent))

    def save_callback(self):
        file = fd.asksaveasfile(title="Save as an Image", defaultextension=".png", initialdir=os.getcwd(),
                              filetypes=(("picture files", "*.png"), ("all files", "*.*")))
        if file is not None:
            pass
