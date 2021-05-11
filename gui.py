import sqlite3
from tkinter import *
from PIL import ImageTk,Image
#from foo import Foo
root = Tk()
root.title("Contact Book")
root.iconbitmap("c:/gui/finalproject.ico")
root.geometry("500x500")





submit_button = Button(root, text="Add Contact to Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_button = Button(root, text="show contacts", command=query)
query_button.grid()

def submit():

	conn = sqlite3.connect("contactbook.db")

	cursor = conn.cursor()

	cursor.execute("INSERT INTO contacts VALUES (:f_name, :l_name, :title, :email, :phonenumber)",

		{
			'f_name': f_name.get(),
			'l_name': l_name.get(),
			'title': title.get(),
			'email': email.get(),
			'phonenumber': phonenumber.get()
		})


	conn.commit()

	conn.close()

	#clear text boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	title.delete(0, END)
	email.delete(0, END)
	phonenumber.delete(0, END)
def query():
	conn = sqlite3.connect("contactbook.db")

	cursor = conn.cursor()

	cursor.execute("SELECT *, oid FROM contacts")

	records = cursor.fetchall()
	print(records)

	for record in records[0]:
		print_records += record + "\n"

	conn.commit()

	conn.close()
	

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
title = Entry(root, width=30)
title.grid(row=2, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=3, column=1, padx=20)
phonenumber = Entry(root, width=30)
phonenumber.grid(row=4, column=1, padx=20)
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
title_label = Label(root, text="Title")
title_label.grid(row=2, column=0)
email_label = Label(root, text="Email")
email_label.grid(row=3, column=0)
phonenumber_label = Label(root, text="Phonenumber")
phonenumber_label.grid(row=4, column=0)
