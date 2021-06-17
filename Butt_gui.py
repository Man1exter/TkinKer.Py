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
b1.pack()
b2 = tkinter.Button(root,text="CAR",bg="red",width=10)
b2.pack()
b3 = tkinter.Button(root,text="HOUSE",bg="yellow",width=10)
b3.pack()

# functions with event

# images (download)

# exit with [X]
root.mainloop()