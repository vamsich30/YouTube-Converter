from tkinter import filedialog
from tkinter import *

def location():
    root = Tk()
    root.withdraw()
    print("Choose your directory : ", end=" ")
    direc = filedialog.askdirectory()
    print(direc, "\n")
    return direc
