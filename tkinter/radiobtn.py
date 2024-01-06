from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root=Tk()

root.title("Radio button")
root.geometry("500x500")

selected_var=StringVar()
pro=("java","python","Ruby","Golang","javascript")

def show_detail():
    msg=messagebox.showinfo(title="Result",message="you know "+selected_var.get())


label=Label(root,text="select the programming language u know?").pack()

for lang in pro:
    rdbtn=Radiobutton(root,text=lang,value=lang,variable=selected_var).pack()

btn=Button(root,text="Submit",command=show_detail).pack()

root.mainloop()
