# by Man1exter ==> https://github.com/Man1exter

import tkinter
from PIL import Image, ImageTk
import random

# settings of main root
root = tkinter.Tk()
root.title("START TKINTER PROJECT")
root.geometry('800x700')
root.configure(background='black')

# random color
color = ["blue","yellow","green","black","orange","purple","lightblue","olive","indygo","pink"]
colors = random.choice(color)

# buttons with pack
b1 = tkinter.Button(root,text="ANIMAL",bg=colors,width=10)
b2 = tkinter.Button(root,text="CAR",bg=colors,width=10)
b3 = tkinter.Button(root,text="HOUSE",bg=colors,width=10)
b4 = tkinter.Button(root,text="JOB",bg=colors,width=10)
b5 = tkinter.Button(root,text="COUNTRY",bg=colors,width=10)
b6 = tkinter.Button(root,text="CLUB",bg=colors,width=10)
b7 = tkinter.Button(root,text="NAME",bg=colors,width=10)
b8 = tkinter.Button(root,text="WEATHER",bg=colors,width=10)
b9 = tkinter.Button(root,text="GAME",bg=colors,width=10)
b10 = tkinter.Button(root,text="BEER",bg=colors,width=10)

# grid mesh cache
b1.grid(row = 1,  column = 0)
b2.grid(row = 0,  column = 1)
b3.grid(row = 1,  column = 2)
b4.grid(row = 0,  column = 3)
b5.grid(row = 1,  column = 4)
b6.grid(row = 0,  column = 5)
b7.grid(row = 0,  column = 5)
b8.grid(row = 0,  column = 5)
b9.grid(row = 0,  column = 5)
b10.grid(row = 0,  column = 5)

# functions with event

# images (download)

# exit with [X]
root.mainloop()