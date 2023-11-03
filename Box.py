from tkinter import *
import tkinter.messagebox as msg
root=Tk()
root.geometry("600x400")
def func():
    print("This is python")
def help():
    print("I see")
    msg.showinfo("Popup","Helped")
def Rate():
    v=msg.askquestion("","Do you liked our app")
    if v=="yes":
        print("Rate us on playstore")
    else:
        msg.showinfo("","Our team will contact you")
filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="File",command=func)
m1.add_command(label="Save",command=func)
m1.add_separator()
m1.add_command(label="Save as",command=func)
m1.add_command(label="Help",command=help)
m1.add_command(label="Rate",command=Rate)
m1.add_command(label="Quit",command=quit)
root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)
root.mainloop()

