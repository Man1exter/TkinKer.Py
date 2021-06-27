import tkinter
import random

root = tkinter.Tk()
root.title("TESTING BUTTON CHANGE SOMETHING")
root.geometry('800x700')
root.configure(background = 'green')

def background_change():
    color_list = ["yellow","black","orange","brown","blue","purple"]
    random_color = random.choice(color_list)
    root.configure(background = random_color)

button_test = tkinter.Button(root, text = 'CHANGE',bg = 'green', width = 11, font = ('ARIAL',15), command=background_change).pack()

root.mainloop()