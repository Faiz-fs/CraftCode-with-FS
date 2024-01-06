from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

root=Tk()
root.title("List box")
lang=("java","javascript","python","c","c++","Golang","php","swift")
var=Variable(value=lang)

def selection(event):
    selected=lstbox.curselection()
    selected_lang="".join([lstbox.get(i) for i in selected])
    showinfo(title="Info",message="you have selected "+selected_lang)


lstbox=Listbox(root,height=6,listvariable=var,selectmode=EXTENDED,)

scbar=Scrollbar(root,orient=VERTICAL,command=lstbox.yview)

lstbox['yscrollcommand']=scbar.set

lstbox.bind("<<ListboxSelect>>",selection)
lstbox.pack(expand=True,fill=BOTH,side=LEFT)
scbar.pack(side=LEFT,fill=Y,expand=True)

root.mainloop()

