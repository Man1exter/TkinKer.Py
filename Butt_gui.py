# by Man1exter ==> https://github.com/Man1exter

import tkinter
from tkinter import font
from PIL import Image, ImageTk
import random

# settings of main root
root = tkinter.Tk()
root.title("START TKINTER PROJECT")
root.geometry('800x700')
root.configure(background='black')

# random color
color = ["red","yellow","green","orange","purple","lightblue","olive","pink"]
colors = random.choice(color)

# functions with event to add images after click
def change_image_animal():
   pack_animal = ['./animals/elephant.jpg','./animals/fhdf.jpg','./animals/hgfhgfhggf.jpg','./animals/jghjhjhgj.jpg','./animals/jhggjhj.jpg']
   bg_image = Image.open(random.choice(pack_animal))
   bg_image = bg_image.resize((700,500),Image.ANTIALIAS)
   access_image = ImageTk.PhotoImage(bg_image)
   tkinter.Label(root,image = access_image).pack()
# bug / fix / error ===> feature :D

def car_change():
   pack_car = ['./cars/2020-Toyota-Supra-13.jpg','./cars/27142_social-supercar-le-auto-dei-sogni.jpg','./cars/9370122a.jpg','./cars/mclaren-720s_0.jpg','/cars/SharpJan20_Supercars_feat.jpg','./cars/MW-AQ797_bugatt_20120410172421_MG.jpg']
   bg_image = Image.open(random.choice(pack_car))
   bg_image = bg_image.resize((800,700),Image.ANTIALIAS)
   access_image = ImageTk.PhotoImage(bg_image)
   tkinter.Label(root,image = access_image).pack()

# buttons with pack
b1 = tkinter.Button(root,text="ANIMAL",bg = colors,width = 10,font = ('Arial', 12),command = change_image_animal)
b1.pack()
b2 = tkinter.Button(root,text="CAR",bg = colors,width = 10,font = ('Arial', 12),command = car_change)
b2.pack()
b3 = tkinter.Button(root,text="HOUSE",bg = colors,width = 10,font = ('Arial', 12))
b3.pack()
b4 = tkinter.Button(root,text="JOB",bg = colors,width = 10,font = ('Arial', 12))
b4.pack()
b5 = tkinter.Button(root,text="COUNTRY",bg = colors,width = 10,font = ('Arial', 12))
b5.pack()
b6 = tkinter.Button(root,text="CLUB",bg = colors,width = 10,font = ('Arial', 12))
b6.pack()
b7 = tkinter.Button(root,text="NAME",bg = colors,width = 10,font = ('Arial', 12))
b7.pack()
b8 = tkinter.Button(root,text="WEATHER",bg = colors,width = 10,font = ('Arial', 12))
b8.pack()

# grid mesh cache (oversize with image)
#b1.grid(row = 1,  column = 0)
#b2.grid(row = 0,  column = 1)
#b3.grid(row = 1,  column = 2)
#b4.grid(row = 0,  column = 3)
#b5.grid(row = 1,  column = 4)
#b6.grid(row = 0,  column = 5)
#b7.grid(row = 1,  column = 6)
#b8.grid(row = 0,  column = 7)

# exit with [X]
root.mainloop()