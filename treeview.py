from tkinter import *
import tkinter.messagebox as MessageBox
import tkinter.ttk as ttk
import mysql.connector as mysql
def insert():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status","All Fields are required ")
    else:
        con=mysql.connect(host="localhost",password="1234",user="root",database="crud")
        cursor=con.cursor()
        query="insert into operation values(%s,%s,%s)"
        cursor.execute(query,(id,name,phone))
        con.commit()
        MessageBox.showinfo("Data Inserted","Data Inserted successfully")
        e_id.delete(0, END)
        e_name.delete(0, END)
        e_phone.delete(0, END)

def update():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status","All Fields are required ")
    else:
        con=mysql.connect(host="localhost",password="1234",user="root",database="crud")
        cursor=con.cursor()
        query="update operation set name=%s,phone=%s where id=%s"
        cursor.execute(query,(name,phone,id))
        con.commit()
        MessageBox.showinfo("Data Inserted","Data updated successfully")
        e_id.delete(0,END)
        e_name.delete(0,END)
        e_phone.delete(0,END)
def delete():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()

    con=mysql.connect(host="localhost",password="1234",user="root",database="crud")
    cursor=con.cursor()
    query="delete from operation where id=%s and name=%s"
    cursor.execute(query,(id,name))
    con.commit()
    MessageBox.showinfo("Data Deleted","Data Deleted successfully")
    e_id.delete(0, END)
    e_name.delete(0, END)
    e_phone.delete(0, END)

root=Tk()
root.geometry("600x300")
root.title("Python CRUD operation")
id=Label(root,text="Enter id",font=("poppins",10,"bold"))
id.grid(column=0,row=0)
name=Label(root,text="Name",font=("poppins",10,"bold"))
name.grid(column=0,row=1)
phone=Label(root,text="Phone",font=("poppins",10,"bold"))
phone.grid(column=0,row=2)
e_id=Entry()
e_id.grid(column=1,row=0)
e_name=Entry()
e_name.grid(column=1,row=1)
e_phone=Entry()
e_phone.grid(column=1,row=2)
insert=Button(root,text="insert",command=insert)
insert.grid(column=0,row=4)
update=Button(root,text="update",command=update)
update.grid(column=1,row=4)
delete=Button(root,text="delete",command=delete)
delete.grid(column=2,row=4)
tree=ttk.Treeview()
style=ttk.Style()
style.configure("Treeview.Heading")
tree["columns"]=["id","name","phone"]
tree.column("#0",width=0)
tree.column("id",width=50, minwidth=100, anchor="w")
tree.column("name",width=50, minwidth=100,anchor="w")
tree.column("phone",width=50, minwidth=100,anchor="w")
tree.heading("id",text="Id")
tree.heading("name",text="Name")
tree.heading("phone",text="Phone")
tree.grid(row=6,columnspan=3)
con=mysql.connect(host="localhost",password="1234",user="root",database="crud")
cursor=con.cursor()
query="select * from operation order by id"
cursor.execute(query)
data=cursor.fetchall()
i=0
for row in data:
    tree.insert("",i,text="",values=(row[0],row[1],row[2]))
    i+=1

root.mainloop()
