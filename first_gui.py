import tkinter
from PIL import Image, ImageTk

# settings of main root PANEL
root = tkinter.Tk()
root.title("ANIMAL IMAGES ON THE PANEL")
root.geometry('800x700')
root.configure(background='black')

# menu with click-list 
main_menu = tkinter.Menu()
root.config(menu = main_menu)

# section on the menu
file_menu = tkinter.Menu(main_menu)
main_menu.add_cascade(label='ROLL', menu = file_menu)
animal_section = file_menu.add_command(label='New Animal')
car_section = file_menu.add_command(label='New Car')
house_section = file_menu.add_command(label='New House')
game_section = file_menu.add_command(label='New Game')
file_menu.add_separator()

def animal_show(event):
    if event == animal_section:
       pass

def car_show(event):
    if event == car_section:
       pass

def house_show(event):
    if event == house_section:
       pass

def game_show(event):
    if event == game_section:
       pass

# bg_image = Image.open('elephant.jpg')
# bg_image = bg_image.resize((800,700),Image.ANTIALIAS)
# access_image = ImageTk.PhotoImage(bg_image)
# tkinter.Label(root,image = access_image).pack()

# exit from loop of the window PANEL
root.mainloop()