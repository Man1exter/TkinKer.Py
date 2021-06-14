import tkinter
import random
from PIL import Image, ImageTk

# settings of main root PANEL
root = tkinter.Tk()
root.title("GRAPHICS AND IMAGES ON THE PANEL / BACKGROUND")
root.geometry('800x700')
root.configure(background='black')

# menu with click-list 
main_menu = tkinter.Menu()
root.config(menu = main_menu)

# -------------------------------------------------------
# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))

# bg_image = Image.open('elephant.jpg')
# bg_image = bg_image.resize((800,700),Image.ANTIALIAS)
# access_image = ImageTk.PhotoImage(bg_image)
# tkinter.Label(root,image = access_image).pack()
# -------------------------------------------------------

def animal_show():
       pack_animal = ['elephant.jpg','mini_monkey.jpg','monkey.jpg','.lion.jpg','chogath.jpg']
       bg_image = Image.open(random.choice(pack_animal))
       bg_image = bg_image.resize((800,700),Image.ANTIALIAS)
       access_image = ImageTk.PhotoImage(bg_image)
       tkinter.Label(root,image = access_image).pack()

def car_show():
       pack_car = ['elephant.jpg','mini_monkey.jpg','monkey.jpg','lion.jpg','chogath.jpg']
       bg_image = Image.open(random.choice(pack_car))
       bg_image = bg_image.resize((800,700),Image.ANTIALIAS)
       access_image = ImageTk.PhotoImage(bg_image)
       tkinter.Label(root,image = access_image).pack()

def house_show():
       pack_house = ['elephant.jpg','mini_monkey.jpg','monkey.jpg','lion.jpg','chogath.jpg']
       bg_image = Image.open(random.choice(pack_house))
       bg_image = bg_image.resize((800,700),Image.ANTIALIAS)
       access_image = ImageTk.PhotoImage(bg_image)
       tkinter.Label(root,image = access_image).pack()

def game_show():
       pack_game = ['elephant.jpg','mini_monkey.jpg','monkey.jpg','lion.jpg','chogath.jpg']
       bg_image = Image.open(random.choice(pack_game))
       bg_image = bg_image.resize((800,700),Image.ANTIALIAS)
       access_image = ImageTk.PhotoImage(bg_image)
       tkinter.Label(root,image = access_image).pack()

# section on the menu
file_menu = tkinter.Menu(main_menu)
main_menu.add_cascade(label='ROLL', menu = file_menu)
animal_section = file_menu.add_command(label='New Animal',command = animal_show())
car_section = file_menu.add_command(label='New Car',command = car_show())
house_section = file_menu.add_command(label='New House',command = house_show())
game_section = file_menu.add_command(label='New Game',command = game_show())
file_menu.add_separator()


# exit from loop of the window PANEL
root.mainloop()