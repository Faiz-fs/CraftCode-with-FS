from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

root=Tk()
root.geometry("300x200")
root.title("combobox")

selected_month=StringVar()
def display(event):
    showinfo(title="Result",message="you selected "+ selected_month.get())
    cbox.current(0)
month=("Please select the month","January","February","March","April","May","June","July","August","September","October","November","December")
label=Label(root,text="Please select the month:").pack()
cbox=Combobox(root,textvariable=selected_month,values=month)
cbox.current(0)
cbox.bind("<<ComboboxSelected>>",display)
cbox.pack()

root.mainloop()

