# by Man1exter ==> https://github.com/Man1exter

import tkinter
from PIL import Image, ImageTk

# settings of main root
root = tkinter.Tk()
root.title("START TKINTER PROJECT")
root.geometry('800x700')
root.configure(background='black')

# buttons with pack
b1 = tkinter.Button(root,text="ANIMAL",bg="lightblue",width=10)
b2 = tkinter.Button(root,text="CAR",bg="red",width=10)
b3 = tkinter.Button(root,text="HOUSE",bg="yellow",width=10)

# grid mesh cache
b1.grid(row = 0,  column = 0)
b2.grid(row = 0,  column = 1)
b3.grid(row = 0,  column = 2)

# functions with event

# images (download)

# exit with [X]
root.mainloop()