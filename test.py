import tkinter

root = tkinter.Tk()
root.title("TESTING BUTTON CHANGE SOMETHING")
root.geometry('800x700')
root.configure(background = 'green')

button_test = tkinter.Button(root, text = 'CLICK',bg = 'green', width = 11, font = ('ARIAL',15))
button_test.pack()

root.mainloop()