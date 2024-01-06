from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os.path as p
import csv
import datetime

# set root window

root = Tk()
root.geometry("600x400")
root.config(bg="#acb1d6")
root.title("Data Entry")
root.resizable(False, False)

# icon
iconimg = PhotoImage(file="img/icons8-data-migration-96.png")
root.iconphoto(False, iconimg)

# variables

name = StringVar()
age = StringVar(value=0)
contact = StringVar()
# address=StringVar()
job = StringVar()
gender = StringVar()


# functions

def submit():
    field = ["name", "age", "contact", "gender", "job", "address"]
    value = {"name": name.get(), "age": age.get(), "contact": contact.get(), "gender": gender.get(), "job": job.get(),
             "address": addressentry.get("1.0", "end-1c").replace("\n", " ")}
    for key in value.keys():
        if value[key] == "" or value[key] == "0" or value[key] == "Please Enter the job":
            showerror(title="Missing value", message="Enter the value for " + key)
            break
    if (not value["contact"].isdigit()) or len(value["contact"]) != 10:
        showerror(title="Invalid format", message="Enter Proper contact information")
    else:
        val = [value]
        filename = str(datetime.date.today())
        path = "data/"
        if p.isfile(path + filename):
            with open(path + filename, "a+", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=field)
                writer.writerows(val)
        else:
            with open(path + filename, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=field)
                writer.writeheader()
                writer.writerows(val)
    name.set("")
    age.set("0")
    contact.set("")
    addressentry.delete("1.0", "end")
    jobentery.current(0)
    gender.set("")


def clear():
    name.set("")
    age.set("0")
    contact.set("")
    addressentry.delete("1.0", "end")
    jobentery.current(0)
    gender.set("")


def open_file():
    topwindow = Toplevel()
    topwindow.title("Data file")
    topicon = PhotoImage(file="img/icons8-csv-96.png")
    topwindow.iconphoto(False, topicon)

    filename = str(datetime.date.today())
    path = "data/"
    details = []
    with open(path + filename, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            details.append(tuple(row))

    # treeview
    tree = Treeview(topwindow, columns=details[0], show="headings")
    tree.heading("name", text="Name")
    tree.heading("age", text="Age")
    tree.heading("contact", text="Contact")
    tree.heading("gender", text="Gender")
    tree.heading("job", text="Job")
    tree.heading("address", text="Address")

    for v in details[1:]:
        tree.insert("", END, values=v)

    tree.grid(row=0, column=0, sticky="nsew")

    scbar = Scrollbar(topwindow, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scbar.set)
    scbar.grid(row=0, column=1, sticky="ns")

    topwindow.mainloop()


jobvalues = (
    "Please Enter the job", "Full-Stack Developer", "Support team", "Team Lead", "Project Manager", "Ui/Ux designer",
    "Frontend Developer", "Backend Developer", "HR")
# frames

entryframe = LabelFrame(root, relief="groove", borderwidth=3, text="Entry Details", width=570, height=300)
btnframe = Frame(root, relief="groove", borderwidth=5, width=570, height=70)

entryframe.place(x=10, y=10)
btnframe.place(x=10, y=320)

# entryframe

nameLabel = Label(entryframe, text="Name:", font=("calibre", 12, "bold"))
nameentry = Entry(entryframe, textvariable=name, font=("calibre", 12, "bold"))

ageLabel = Label(entryframe, text="Age:", font=("calibre", 12, "bold"))
ageentry = Spinbox(entryframe, textvariable=age, font=("calibre", 12, "bold"), from_=18, to=60, width=19)

contactLabel = Label(entryframe, text="Phone No:", font=("calibre", 12, "bold"))
contactentry = Entry(entryframe, textvariable=contact, font=("calibre", 12, "bold"))

addressLabel = Label(entryframe, text="Address:", font=("calibre", 12, "bold"))
addressentry = Text(entryframe, font=("calibre", 12, "bold"), width=40, height=5)

jobentery = Combobox(entryframe, textvariable=job, values=jobvalues)
jobentery.current(0)

GenderLabel = Label(entryframe, text="Gender:")
gender1entry = Radiobutton(entryframe, text="Male", value="Male", variable=gender)
gender2entry = Radiobutton(entryframe, text="Female", value="Female", variable=gender)

nameLabel.place(x=10, y=10)
nameentry.place(x=110, y=10)
ageLabel.place(x=10, y=50)
ageentry.place(x=110, y=50)
contactLabel.place(x=10, y=90)
contactentry.place(x=110, y=90)
jobentery.place(x=10, y=130)
GenderLabel.place(x=160, y=130)
gender1entry.place(x=220, y=130)
gender2entry.place(x=280, y=130)
addressLabel.place(x=10, y=170)
addressentry.place(x=110, y=170)

# btnframe

submitbtn = Button(btnframe, text="Submit", command=submit)
clearbtn = Button(btnframe, text="Clear", command=clear)
openbtn = Button(btnframe, text="Open Excel", command=open_file)
Exitbtn = Button(btnframe, text="Exit", command=root.destroy)

submitbtn.place(x=100, y=10)
clearbtn.place(x=190, y=10)
openbtn.place(x=290, y=10)
Exitbtn.place(x=370, y=10)

root.mainloop()
