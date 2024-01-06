from tkinter import *
from tkinter.ttk import *

root=Tk()
root.geometry("400x300")
root.title("Spin box")

spinbox_value=StringVar(value=0)

def display():
    print(spinbox_value.get())

#spbox=Spinbox(root,from_=0,to=20,textvariable=spinbox_value,command=display).pack()
spbox=Spinbox(root,values=(10,20,30,40,50,60),textvariable=spinbox_value,command=display).pack()
root.mainloop()
