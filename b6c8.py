#a
from tkinter import *

def NewFile():
    print('New File!')
def About():
    print("This is a simple example of the menu")
def openfile():
    print(" Open")
def text():
    print('Text')
def picture():
    print('Picture')

root=Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu= Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label=" Exit", command=root.quit)

inset=Menu(menu)
menu.add_cascade(label="Insert",menu=inset)
inset.add_command(label="Text", command=text)
inset.add_command(label="Picture", command=picture)

helpmenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)


mainloop()

