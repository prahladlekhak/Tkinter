from tkinter import *
import mysql.connector as msql
import tkinter.messagebox as msg
con=msql.connect(host="localhost",user="root",password="1234")
cur=con.cursor()
try:
    cur.execute("use palakbhondu")
except:
    cur.execute("create database registration")
    cur.execute("use registration")
root=Tk()
root.geometry("600x400")
root.title("Login form")
l1 = Label(root, text="Name")
l6 = Label(root, text="Password")
l1.grid(row=1, column=1)
l6.grid(row=1, column=4)
name = StringVar()
password = StringVar()


e1 = Entry(root, textvariable=name)
e6 = Entry(root, textvariable=password)
e1.grid(row=1, column=2)
e6.grid(row=1, column=5)
def login():
    query="select * from login where name=%s and password=%s"
    cur.execute(query,(e1.get(),e6.get()))
    data=cur.fetchone()
    if data==None:
        msg.showinfo("", "login unsuccessful")
    else:
        msg.showinfo("","login successful")
b1 = Button(root, text="Login", command=login).grid(row=3, column=1)


def update():
    try:
        cur.execute(f"update login set password='{e6.get()}' where name='{e1.get()}'")
        con.commit()
    except:
        pass
# b2 = Button(root, text="Change password", command=update).grid(row=3, column=1)
root.mainloop()