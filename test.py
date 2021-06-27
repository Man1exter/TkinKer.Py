from tkinter import * 
import random

root = Tk()
root.title("TESTING BUTTON CHANGE SOMETHING")
root.geometry('800x700')
root.configure(background = 'green')

def change_color(i = 0):
    if i < 50:
        colors = ('red', 'blue', 'green', 'black', "pink", "blue")
        root.config(bg=colors[i])
        root.after(500, change_color, i+1)
    else:
        colors = ("white")
        root.config(bg=colors[i])
        root.after(500, change_color, i+1)

def background_change():
    color_list = ["yellow","black","orange","brown","blue","purple"]
    random_color = random.choice(color_list)
    root.configure(background = random_color)

button_test = Button(root, text = 'COLOR',bg = 'green', width = 11, font = ('ARIAL',15), command=background_change).pack()

change_color()
root.mainloop()