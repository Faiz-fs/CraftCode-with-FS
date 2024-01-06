from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root=Tk()

root.title("check button")
root.geometry("500x500")

java=StringVar()
python=StringVar()
ruby=StringVar()
golang=StringVar()
js=StringVar()


def show_detail():
    pro=(java.get(),python.get(),ruby.get(),golang.get(),js.get())
    val=""
    for i in pro:
        if i!="":
            val+=i+" "
    msg=messagebox.showinfo(title="Result",message="you know "+val)


label=Label(root,text="select the programming language u know?").pack()

#for lang in pro:
#    rdbtn=Radiobutton(root,text=lang,value=lang,variable=selected_var).pack()

ckbtn1=Checkbutton(root,text="Java",variable=java,onvalue="Java",offvalue="").pack()
ckbtn2=Checkbutton(root,text="Python",variable=python,onvalue="Python",offvalue="").pack()
ckbtn1=Checkbutton(root,text="Ruby",variable=ruby,onvalue="Ruby",offvalue="").pack()
ckbtn1=Checkbutton(root,text="Golang",variable=golang,onvalue="Golang",offvalue="").pack()
ckbtn1=Checkbutton(root,text="JavaScript",variable=js,onvalue="JavaScript",offvalue="").pack()

btn=Button(root,text="Submit",command=show_detail).pack()

root.mainloop()
