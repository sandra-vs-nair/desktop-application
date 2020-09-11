# -----------------------------------------------------------
# Desktop Application front-end.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

from tkinter import *
import backend

#Displays the selected row and saves it in a global tuple.
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[0])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[1])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[2])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[3])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name.get(),roll.get(),section.get(),country.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(name.get(),roll.get(),section.get(),country.get())
    list1.delete(0,END)
    list1.insert(END,(name.get(),roll.get(),section.get(),country.get()))

#Select a row and press button delete entry.
def delete_command():
    backend.delete(selected_tuple[1])

#Select a row and press button update entry.
def update_command():
    backend.update(selected_tuple[1],name.get(),roll.get(),section.get(),country.get())

def search_command():
    list1.delete(0,END)
    for row in backend.search(name.get(),roll.get(),section.get(),country.get()):
        list1.insert(END,row)

window=Tk()
window.title("Student data")

label1=Label(window,text="Student name")
label1.grid(row=0,column=0)

label2=Label(window,text="Roll Number")
label2.grid(row=0,column=2)

label3=Label(window,text="Section")
label3.grid(row=1,column=0)

label4=Label(window,text="Country")
label4.grid(row=1,column=2)

name=StringVar()
e1=Entry(window,textvariable=name)
e1.grid(row=0,column=1)

roll=StringVar()
e2=Entry(window,textvariable=roll)
e2.grid(row=0,column=3)

section=StringVar()
e3=Entry(window,textvariable=section)
e3.grid(row=1,column=1)

country=StringVar()
e4=Entry(window,textvariable=country)
e4.grid(row=1,column=3)

list1=Listbox(window,height=5,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind('<<ListboxSelect>>',get_selected_row)

sb=Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)

b1=Button(window,text="View all",width=10,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search",width=10,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=10,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update entry",width=10,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete entry",width=10,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=10,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()