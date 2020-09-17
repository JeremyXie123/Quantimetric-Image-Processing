import tkinter as tk
from tkinter import ttk
from single_img_tab import single_img_tab
from tkinter_custom.notebook_tabs.multi_img_tab import multi_img_tab
from tkinter_custom.notebook_tabs.sources_tab import sources_tab

from tkinter_custom.extra_functions import getImage


if __name__ == "__main__":
    root = tk.Tk()
    root.tk.call('wm', 'iconphoto', root._w, getImage("temp.png", 500, 500))
    root.title("HDR Expierimentation Project")
    root.protocol("WM_DELETE_WINDOW", quit)

    mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))
    mainframe.grid(column=0, row=0, sticky="NEWS")

    mainnote = ttk.Notebook(mainframe)
    mainnote.grid(column=0, row=0, sticky="NEWS")

    single_img_tab(mainnote,"Single Image")

    multi_img_tab(mainnote, "Multiple Image")

    sources_tab(mainnote, "Extra Info")

    root.mainloop()
