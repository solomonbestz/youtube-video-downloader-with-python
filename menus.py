from tkinter import *
from PIL import ImageTk, Image


screen = Tk()
screen.title('Switch Menus')


my_menu = Menu(screen)
screen.config(menu=my_menu)

def new():
    pass

def cut():
    pass

def copy():
    pass


#Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=screen.quit)


#Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="cut", command=cut)
edit_menu.add_separator()
edit_menu.add_command(label="copy", command=copy)


if __name__=='__main__':
    screen.mainloop()