# by Man1exter ==> https://github.com/Man1exter

import tkinter
import random
from PIL import Image, ImageTk

# settings of main root
root = tkinter.Tk()
root.title("START TKINTER PROJECT")
root.geometry('800x700')
root.configure(background='black')

# background image / graphic
# ----- size of image ----- #
bg_image = Image.open('elephant.jpg')
bg_image = bg_image.resize((797,697),Image.ANTIALIAS)
access_image = ImageTk.PhotoImage(bg_image)
tkinter.Label(root,image = access_image).pack()

# events
#def but_left(event):
    #print("left click")

#def but_right(event):
    #print("right click")

# download images / graphics

# elements
#b1 = tkinter.Button(root,text = "BUTTON1")
#b1.bind('<Button-3>',but_right)
#b1.pack()

#b2 = tkinter.Button(root,text = "BUTTON2")
#b2.bind('<Button-1>',but_left)
#b2.pack()

# exit from loop
root.mainloop()