from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import colorchooser
from PIL import Image, ImageTk
import pickle
import os
count = 0
primaryColorVar="SkyBlue1"
def resized_label(filename="", width=260, height=215, relx=.5, rely=.25, anchor=CENTER):
    global root
    image = Image.open(filename)
    resize_image = image.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(master=root, image=img, bg="CadetBlue1")
    label1.image = img
    label1.pack()
    label1.place(relx=relx, rely=rely, anchor=anchor)
    return label1

nameList = pickle.load(open("name.dat", "rb"))
activityList = pickle.load(open("activity.dat", "rb"))
timeList = pickle.load(open("time.dat", "rb"))
os.system("clear")
root = Tk()
root.geometry("700x950")
root.title("Activity Trackr")
def bgColor():
    bgColor = colorchooser.askcolor()[1]
    if bgColor:
        root.config(bg=bgColor)
        for label in root.winfo_children():
            if isinstance(label, Label):
                label.config(bg=bgColor)
        for widget in root.winfo_children():
            if isinstance(widget, Entry):
                widget.config(bg=bgColor)
        for widget in root.winfo_children():
            if isinstance(widget, Button):
                widget.config(bg=bgColor)
def primaryColor():
    global primaryColorVar
    primaryColorVar = colorchooser.askcolor()[1]
    if primaryColorVar:
        table.tag_configure(tagname='bg', background=primaryColorVar,font=("times", 15))
        style.configure("Treeview",bg=primaryColorVar,fg="black",rowheight=30,fieldbackground=primaryColorVar)
        style.configure("Treeview.Heading",bg=primaryColorVar,fg="black",rowheight=30,font=("times", 15))


def highlightColor():
    highlightColor = colorchooser.askcolor()[1]
    if highlightColor:
        style.map("Treeview",background=[('selected',highlightColor)],foreground=[('selected','black')])

def textColor():
    global primaryColorVar
    res=mb.askquestion("Change Text Color","Do you want black?\n(If no, white will be selected)")
    if res == 'yes':
        for label in root.winfo_children():
            if isinstance(label, Label):
                label.config(fg="black")
        for widget in root.winfo_children():
            if isinstance(widget, Entry):
                widget.config(fg="black")
        for widget in root.winfo_children():
            if isinstance(widget, Button):
                widget.config(fg="black")
        table.tag_configure(tagname='bg', background=primaryColorVar,foreground="black",font=("times", 15))
        style.configure("Treeview",bg=primaryColorVar,fg="black",rowheight=30,fieldbackground=primaryColorVar)
        style.configure("Treeview.Heading",bg=primaryColorVar,fg="black",rowheight=30,font=("times", 15))
    else:
        for label in root.winfo_children():
            if isinstance(label, Label):
                label.config(fg="white")
        for widget in root.winfo_children():
            if isinstance(widget, Entry):
                widget.config(fg="white")
        for widget in root.winfo_children():
            if isinstance(widget, Button):
                widget.config(fg="white")
        table.tag_configure(tagname='bg', background=primaryColor,foreground="white",font=("times", 15))
        style.configure("Treeview",bg=primaryColorVar,fg="white",rowheight=30,fieldbackground=primaryColorVar)
        style.configure("Treeview.Heading",bg=primaryColor,fg="white",rowheight=30,font=("times", 15))

def exit():
    res = mb.askquestion('Close', 'Do you really want to exit?')
    if res == 'yes':
        root.destroy()
    else:
        pass

myMenu = Menu(root)
root.config(bg="CadetBlue1", menu=myMenu)

optionMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Options", menu=optionMenu)

optionMenu.add_command(label="Background Color", command=bgColor)
optionMenu.add_command(label="Table Color", command=primaryColor)
optionMenu.add_command(label="Highlight Color", command=highlightColor)
optionMenu.add_command(label="Text Color", command=textColor)
optionMenu.add_separator()
optionMenu.add_command(label="Exit", command=exit)


checklist = resized_label("checklist.png", 235, 215, 0.5, 0.17)
label1 = Label(root, text="Name:", font=("times", 15), bg="CadetBlue1", fg="black")
label1.place(relx=0.3, rely=0.4, anchor=CENTER)
nameInput = Entry(root, font=("times", 12), bg="CadetBlue1", fg="black")
nameInput.place(relx=0.7, rely=0.4, anchor=CENTER)
label2 = Label(root, text="Activity:", font=("times", 15), bg="CadetBlue1", fg="black")
label2.place(relx=0.3, rely=0.45, anchor=CENTER)
activityInput = Entry(root, font=("times", 12), bg="CadetBlue1", fg="black")
activityInput.place(relx=0.7, rely=0.45, anchor=CENTER)
label3 = Label(root, text="Time:", font=("times", 15), bg="CadetBlue1", fg="black")
label3.place(relx=0.3, rely=0.5, anchor=CENTER)
timeInput = Entry(root, font=("times", 12), bg="CadetBlue1", fg="black")
timeInput.place(relx=0.7,rely=0.5,anchor=CENTER)
style=ttk.Style()
style.theme_use('clam')
style.configure("Treeview",bg="SkyBlue1",fg="black",rowheight=30,fieldbackground="SkyBlue1",font=("times", 15))
style.configure("Treeview.Heading",bg="SkyBlue1",fg="black",rowheight=30,font=("times", 15))
style.map("Treeview",background=[('selected','aquamarine')],foreground=[('selected','black')])
table=ttk.Treeview(root,columns=('name','activity','time'),show='headings')
table.heading('name',text="Name")
table.heading('activity',text="Activity")
table.heading('time',text="Time")
table.place(relx=0.5,rely=0.8,anchor=CENTER)
table.tag_configure(tagname='bg',background="SkyBlue1")
def Add():
    global nameList
    global activityList
    global timeList
    global count
    val1=nameInput.get()
    val2=activityInput.get()
    val3=timeInput.get()
    nameList.append(val1)
    activityList.append(val2)
    timeList.append(val3)
    pickle.dump(nameList,open("name.dat","wb"))
    print("Name:")
    print(nameList)
    pickle.dump(activityList,open("activity.dat","wb"))
    print("Activity:")
    print(activityList)
    pickle.dump(timeList,open("time.dat","wb"))
    print("Time:")
    print(timeList)
    name=val1
    activity=val2
    time=val3
    data=(name,activity,time)
    table.insert(parent="", index=END,values=data,tags=('bg',))
    count=count+1
def Clear():
    global count
    def clearTable():
        for thing in table.get_children():
            table.delete(thing)
    nameList.clear()
    activityList.clear()
    timeList.clear()
    pickle.dump(nameList,open("name.dat","wb"))
    pickle.dump(activityList,open("activity.dat","wb"))
    pickle.dump(timeList,open("time.dat","wb"))
    print("Name:")
    print(nameList)
    print("Activity:")
    print(activityList)
    print("Time:")
    print(timeList)
    clearTable()
    count=0
def Show():
    global count
    for i in range(len(nameList)):
        name=nameList[i]
        activity=activityList[i]
        time=timeList[i]
        data=(name,activity,time)
        table.insert(parent="", index=END,values=data,tags=('bg',))
        count=count+1
    btnShow.destroy()
btnAdd=Button(root,text="Add",command=Add,font=("times",12),fg="black")
btnAdd.place(relx=0.3,rely=0.6,anchor=CENTER)
btnClear=Button(root,text="Clear",command=Clear,font=("times",12),fg="black")
btnClear.place(relx=0.7,rely=0.6,anchor=CENTER)
btnShow=Button(root,text="Show",command=Show,font=("times",12),fg="black")
btnShow.place(relx=0.5,rely=0.6,anchor=CENTER) 
root.mainloop()