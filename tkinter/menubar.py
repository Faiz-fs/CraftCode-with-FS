from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Menu bar demo")
root.geometry("600x400")

menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New File",command=None)
file.add_command(label="Open",command=None)
file.add_command(label="Save",command=None)
file.add_separator()

submenu=Menu(file,tearoff=0)
submenu.add_command(label="Profile")
submenu.add_command(label="Theme")

file.add_cascade(label="Preferences",menu=submenu)

file.add_separator()
file.add_command(label="Exit",command=root.destroy)

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)
edit.add_command(label="Select",command=None)
edit.add_separator()
edit.add_command(label="Find",command=None)
edit.add_command(label="Replace",command=None)


help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
help.add_command(label="Welcome",command=None)
help.add_command(label="Tutorial",command=None)
help.add_command(label="Join us",command=None)
help.add_separator()
help.add_command(label="About",command=None)

root.config(menu=menubar)
root.mainloop()