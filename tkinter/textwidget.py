from tkinter import *
from tkinter.ttk import *

root=Tk()
root.geometry("600x400")
root.title("text widget")

def display():
    text_content=txt.get("1.0","end")
    print(text_content)



txt=Text(root,width=50,height=10)
btn=Button(root,text="display",command=display)

txt.pack()
btn.pack()

root.mainloop()