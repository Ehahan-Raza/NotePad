from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os        
root=Tk()

root.geometry("700x500")
root.title("Notepad")
root.config(background="grey")

def new():
    global file
    root.title("Untitled - Notepad")
    file=None
    text.delete(1.0,END)

def open():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("text Documents",".txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "- Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untititled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #Save as a new file
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ "- Notepad")
            print("File Saved")
    else:
        #Save the File
        f=open(file,"W")
        f.write(text.get(1.0,END))
        f.close()

def cut():
    text.event_generate(("<<Cut>>"))        
def copy():
    text.event_generate(("<<Copy>>"))        
def Paste():
    text.event_generate(("<<Paste>>"))        
def find():
    text.event_generate(("<<Find>>"))        
def undo():
    text.event_generate(("<<Undo>>"))        
def Redo():
    text.event_generate(("<<Redo>>")) 

def about():
    showinfo("Notepad","Notepad by Ehshan Raza")
def help():
    showinfo("Notepad","We will Contact you soon!")

scroll=Scrollbar(root,bg="grey")
scroll.pack(side=RIGHT,fill=Y)

mymenu=Menu(root)

m1=Menu(mymenu,tearoff=0)
m1.add_command(label="New Project",command=new)
m1.add_command(label="Open",command=open)
m1.add_separator()
m1.add_command(label="Save",command=save)
# m1.add_command(label="Save as",)
m1.add_separator()
m1.add_command(label="Print",)
m1.add_command(label="Exit",command=quit)
root.config(menu=mymenu)
mymenu.add_cascade(label="File",menu=m1)

m1=Menu(mymenu,tearoff=0)
m1.add_command(label="Undo",command=undo)
m1.add_command(label="Redo",command=Redo)
m1.add_separator()
m1.add_command(label="Cut",command=cut)
m1.add_command(label="Copy",command=copy)
m1.add_command(label="Paste",command=Paste)
m1.add_separator()
m1.add_command(label="Find",command=find)
root.config(menu=mymenu)
mymenu.add_cascade(label="Edit",menu=m1)

m1=Menu(mymenu,tearoff=0)
m1.add_command(label="Help",command=help)
m1.add_command(label="About",command=about)

root.config(menu=mymenu)
mymenu.add_cascade(label="Help",menu=m1)

# var=StringVar()
file=None
text=Text(root,bg="grey",fg="white",font="Lucida 15",width=700,height=500,yscrollcommand=scroll.set)
text.pack(fill=BOTH,padx=5,pady=5)

scroll.config(command=text.yview)

root.mainloop()