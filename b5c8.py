import tkinter as tk
root= tk.Tk()
v= tk.IntVar()
v.set(1)
languages=[("Python",1),("Perl",2),("Java",3),("C",4),("C++",5)]
def ShowChoice():
    print(v.get())
tk.Label(root,text="""Choose your favourite programming langauage:""",justify=tk.LEFT,padx=20).pack()
for val, languages in enumerate(languages):
    tk.Radiobutton(root,text=languages,variable=v,command =ShowChoice, value=val).pack(anchor=tk.W)

root.mainloop()