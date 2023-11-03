from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("600x400")
root.title("Tutorial Tkinter")
l1=Label(root,text="Username").grid()
l2=Label(root,text="Password").grid(row=1)
l3=Label(root,text="select choice").grid(row=2)
v1=StringVar()
v2=StringVar()
v3=StringVar()
ent1=Entry(root,textvariable=v1).grid(row=0,column=1)
ent2=Entry(root,textvariable=v2).grid(row=1,column=1)
com=ttk.Combobox(root,textvariable=v3)
com['state']='readonly'
com['values']=('cricket','tiktok','sleeping','singing','dancing')
com.current(0)
com.grid(row=2,column=1)
chkbtn1=StringVar()
chkbtn2=StringVar()
chkbtn3=StringVar()
l4=Label(root,text="select choice").grid(row=3)
select=Checkbutton(root,text="Krish",variable=chkbtn1,onvalue=1,offvalue=0).grid(row=4,column=1)
select=Checkbutton(root,text="Lagaan",variable=chkbtn2,onvalue=1,offvalue=0).grid(row=4,column=1)
select=Checkbutton(root,text="Dhoom",variable=chkbtn3,onvalue=1,offvalue=0).grid(row=4,column=1)
var=IntVar()
def fun2():
    q=var.get()
    if q==0:
        print("Male")
    else:
        print("Female")
radio=Radiobutton(root,text="male",variable=var,value=0).grid(row=4,column=0)
radio=Radiobutton(root,text="female",variable=var,value=1).grid(row=4,column=1)
btn2=Button(root,text="radiovalue",command=fun2).grid(row=5)
def getval():
    x=v3.get()
    y=chkbtn2.get()
    z=chkbtn3.get()
    print(x,y,z)
btn1=Button(root,text="Submit",command=getval).grid(row=8)

root.mainloop()