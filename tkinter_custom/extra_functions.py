from PIL import Image, ImageTk
from pathlib import Path

def getImage(path,x,y):
    load = Image.open(path).resize((x, y), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(load)
    return image



