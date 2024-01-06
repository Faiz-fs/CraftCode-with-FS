from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

root=Tk()
root.geometry("600x400")
root.title("Entry Widget")

username=StringVar()
passwd=StringVar()
def display():
    print("username: "+username.get())
    print("password: "+passwd.get())
    showinfo(title="user detail",message="username: "+username.get()+"\n"+"password: "+passwd.get())
    username.set("")
    passwd.set("")


name_label=Label(root,text="Username",font=("calibre",14,"bold"))
name_entry=Entry(root,textvariable=username,font=("calibre",14))
pass_label=Label(root,text="Password",font=("calibre",14,"bold"))
pass_entry=Entry(root,textvariable=passwd,font=("calibre",14),show="*")
submitbtn=Button(root,text="Submit",command=display)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

pass_label.grid(row=1,column=0)
pass_entry.grid(row=1,column=1)

submitbtn.grid(row=2,column=1)

root.mainloop()