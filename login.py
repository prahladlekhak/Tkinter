from tkinter import *
login=Tk()
login.geometry("600x400")
import mysql.connector as msql
import tkinter.messagebox as msg
con=msql.connect(host="localhost",user="root",password="1234")
cur=con.cursor()
try:
    cur.execute("use palakbhondu")
except:
    cur.execute("create database registration")
    cur.execute("use registration")
login.title("Login form")
l1 = Label(login, text="Name")
l6 = Label(login, text="Password")
l1.grid(row=1, column=1)
l6.grid(row=1, column=4)
name = StringVar()
password = StringVar()


e1 = Entry(login, textvariable=name)
e6 = Entry(login, textvariable=password)
e1.grid(row=1, column=2)
e6.grid(row=1, column=5)
def loginn():
    query="select * from login where name=%s and password=%s"
    cur.execute(query,(e1.get(),e6.get()))
    data=cur.fetchone()
    if data==None:
        msg.showinfo("", "login unsuccessful")
        b2 = Button(login, text="Change password", command=update).grid(row=4, column=1)
    else:
        msg.showinfo("","login successful")
b1 = Button(login, text="Login", command=loginn).grid(row=3, column=1)


def update():
    try:
        cur.execute(f"update login set password='{e6.get()}' where name='{e1.get()}'")
        con.commit()
    except:
        pass

    query="select * from login where name=%s and password=%s"
    cur.execute(query,(e1.get(),e6.get()))

def sign_up():
   login.destroy()
   import signn
b2=Button(text="signup",command=sign_up).grid(row=3,column=2)



login.mainloop()
