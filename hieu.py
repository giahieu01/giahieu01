from tkinter import *
root = Tk()
Label(root, text="Red Sun", bg="red", fg="white").pack()
Label(root, text="Green Grass", bg="green", fg="black").pack()
Label(root, text="Blue Sky", bg="blue", fg="white").pack()
mainloop()
from tkinter import *
colours = ['red','green','orange','white','yellow','blue']
r = 0
for c in colours:
 Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
 Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
 r = r + 1
mainloop()
