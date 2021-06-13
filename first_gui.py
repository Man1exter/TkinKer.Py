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
file_menu.add_command(label='New Animal')
file_menu.add_command(label='New Car')
file_menu.add_command(label='New House')
file_menu.add_command(label='New Game')


# exit from loop of the window PANEL
root.mainloop()