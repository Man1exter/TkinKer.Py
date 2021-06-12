# by Man1exter ==> https://github.com/Man1exter

import tkinter
import random
from PIL import Image, ImageTk

# settings of main root
root = tkinter.Tk()
root.title("START TKINTER PROJECT")
root.geometry('800x700')
root.configure(background='black')

# events
def but_left(event):
    print("left click")

def but_right(event):
    print("right click")

# images 

# elements
b1 = tkinter.Button(root,text = "BUTTON1")
b1.bind('<Button-3>',but_right)
b1.pack()

b2 = tkinter.Button(root,text = "BUTTON2")
b2.bind('<Button-1>',but_left)
b2.pack()

# exit from loop
root.mainloop()