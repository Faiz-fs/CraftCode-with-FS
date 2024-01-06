from tkinter import *
from tkinter.ttk import *

root=Tk()

root.geometry("800x600")
root.title("canvas")

def paint(event):
    x1,y1,x2,y2=(event.x-3),(event.y-3),(event.x+3),(event.y+3)
    canv.create_line(x1,y1,x2,y2,fill="blue")


l=Label(root,text="double click and drag to draw").pack()

canv=Canvas(root,width=600,height=400,bg="white")
canv.bind("<B1-Motion>",paint)
canv.pack(anchor=CENTER,expand=True)


"""
canv.create_rectangle((50,50),(150,150),fill="red")
canv.create_oval((200,200),(350,400),fill="green")
canv.create_polygon((10,300),(200,340),(400,400),fill="blue")
"""

root.mainloop()