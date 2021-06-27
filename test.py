from tkinter import *
import random

root = Tk()
root.title("TESTING BUTTON CHANGE SOMETHING")
root.geometry('800x700')
root.configure(background = 'green')
img = PhotoImage(file="bll.jpg")

def background_change():
    color_list = ["yellow","black","orange","brown","blue","purple"]
    random_color = random.choice(color_list)
    root.configure(background = random_color)

def background_change_image():
    image_list = ["/animals/elephant.jpg","/animals/aninimal.jpg","/animals/hgfhgfhggf.jpg","/animals/jghjhjhgj.jpg","/animals/jhggjhj.jpg"]
    filename = root(file = random.choice(image_list)) 
    root.configure(background = filename)

button_test = Button(root, text = 'COLOR',bg = 'green', width = 11, font = ('ARIAL',15), command=background_change).pack()
button_test_image = Button(root, text = 'ANIMAL',bg = 'lightgreen', width = 11, font = ('ARIAL',15), command=background_change_image).pack()

root.mainloop()