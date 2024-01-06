from tkinter import *
from tkinter.ttk import *

root=Tk()

root.title("Craftcode")
root.geometry("500x500")

styl=Style()
styl.configure("TButton",font=("Verdana",20,"bold"))
styl.map("Custom.TButton",background=[("active","blue")],foreground=[("active","white")])

photo=PhotoImage(file="img/icons8-quit-48.png")
pimg=photo.subsample(3,3)
main_frame=Frame(root,relief="groove",borderwidth=5)
main_frame.place(x=10,y=20,width=500,height=200)
label=Label(main_frame,text="welcome to craftcode with fs").pack()
btn_frame=LabelFrame(root,text="button frame",borderwidth=5,relief="groove")
btn_frame.place(x=10,y=250,width=400,height=300)
btn=Button(btn_frame,text="quit",command=root.destroy,style="Custom.TButton",image=pimg,compound="left").pack()
btn1=Button(btn_frame,text="notquit").pack()

root.mainloop()