import mysql.connector as mydb
con=mydb.connect(host="localhost",user="root",password="1234",database="palakbhondu")
mycursor=con.cursor()
from tkinter import *
sign_up=Tk()
sign_up.geometry("600x400")

name = Label(sign_up, text="Name").grid(row=0, column=1)
pas = Label(sign_up, text="Password").grid(row=1, column=1)
age = Label(sign_up, text="Age").grid(row=2, column=1)
gender = Label(sign_up, text="Gender").grid(row=3, column=1)

namevalue = StringVar()
passvalue = StringVar()
agevalue = IntVar()
gendervalue = StringVar()

nameentry = Entry(sign_up, textvariable=namevalue).grid(row=0, column=2)
passentry = Entry(sign_up, textvariable=passvalue).grid(row=1, column=2)
ageentry = Entry(sign_up, textvariable=agevalue).grid(row=2, column=2)
genderentry = Entry(sign_up, textvariable=gendervalue).grid(row=3, column=2)

def values():
    a = namevalue.get()
    b = passvalue.get()
    c = agevalue.get()
    d = gendervalue.get()
    try:
        mycursor.execute("insert into login values('{}','{}')".format(a, b, ))
         # mycursor.execute(f"insert into tkinter values('{a}','{b}','{c}','{d}')")
        con.commit()
    except:
        mycursor.execute("create table login(Name Varchar(20),Password Varchar(10)")
        mycursor.execute("insert into login values('{}','{}')".format(a, b, ))
        con.commit()
b12=Button(text="Submit",command=values).grid(row=4,column=1)