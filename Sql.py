import mysql.connector as mydb
con=mydb.connect(host="localhost",user="root",password="1234",database="registration")
mycursor=con.cursor()

# mycursor.execute("create table tkinter(Name Varchar(20),Rollno Int Unique,Age Int,Gender Char(1))")
from tkinter import *
root=Tk()
root.geometry("800x600")


def register():
   name=Label(root,text="Name").grid(row=0,column=1)
   rno=Label(root,text="RollNo").grid(row=1,column=1)
   age = Label(root, text="Age").grid(row=2, column=1)
   gender = Label(root, text="Gender").grid(row=3, column=1)

   namevalue = StringVar()
   rnovalue = IntVar()
   agevalue = IntVar()
   gendervalue = StringVar()

   nameentry = Entry(root, textvariable=namevalue).grid(row=0, column=2)
   rnoentry = Entry(root, textvariable=rnovalue).grid(row=1, column=2)
   ageentry = Entry(root, textvariable=agevalue).grid(row=2, column=2)
   genderentry = Entry(root, textvariable=gendervalue).grid(row=3, column=2)

   def values():
      a = namevalue.get()
      b = rnovalue.get()
      c = agevalue.get()
      d = gendervalue.get()
      try:

         mycursor.execute("insert into tkinter values('{}',{},{},'{}')".format(a, b, c, d))
         # mycursor.execute(f"insert into tkinter values('{a}','{b}','{c}','{d}')")
         con.commit()
      except:
         mycursor.execute("create table tkinter(Name Varchar(20),Rollno Int Unique,Age Int,Gender Char(1))")
         mycursor.execute("insert into tkinter values('{}',{},{},'{}')".format(a, b, c, d))
         con.commit()


   b12=Button(text="Submit",command=values).grid(row=4,column=1)
rnovalue=IntVar()
def delete():
   rno = Label(root, text="RollNo").grid(row=1, column=1)
   rnoentry = Entry(root, textvariable=rnovalue).grid(row=1, column=2)

   def dlt():
         b = rnovalue.get()
         try:
            print(rnovalue.get())
            mycursor.execute("delete from tkinter where rollno={}".format(b))
            con.commit()
            print("removed")
         except:
            print("Data not available")
   b3=Button(text="done",command=dlt).grid(row=1,column=3)


b1=Button(text="Register",command=register).grid(row=6,column=2)
b2=Button(text="Delete",command=delete).grid(row=6,column=3)
root.mainloop()