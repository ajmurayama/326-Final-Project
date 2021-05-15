#Tim, GUI
import sqlite3
import tkinter as tk
from PIL import ImageTk,Image
import os.path
""" This python file contains a script that creates a database in your present working directory(the one you save this file to/import to)
called "contactsbook.db"(assuming one does not already exist) Using tkinter, a gui interface was created that displays text box widgets which allow
a user to input contact information. The buttons on the GUI application store contact information and display contact database results """
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

def submit():
	conn = sqlite3.connect("contactsbook.db")
	c = conn.cursor()

	c.execute(""" CREATE TABLE IF NOT EXISTS contacts (
                                        f_name text,
                                        l_name text,
                                        title text,
                                        email text,
                                        phonenumber integer
                                        ) """)
	
	c.execute("INSERT INTO contacts VALUES (:f_name, :l_name, :title, :email, :phonenumber)",

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
	f_name.delete(0, )
	l_name.delete(0, END)
	title.delete(0, END)
	email.delete(0, END)
	phonenumber.delete(0, END)
def query():
	conn = sqlite3.connect("contactsbook.db")

	c = conn.cursor()

	c.execute("SELECT * FROM contacts")

	records = c.fetchall()
	print(records)

	for record in records:
		print_records += str(record) + "\n"
		query_label = tk.Label(root, text=print_records)
		query_label.grid(row=8, column=0, columnspan=2)
		query_label.pack()
	conn.commit()

	conn.close()
		
#creating and editing labels for buttons
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
title = tk.Entry(root, width=30)
title.grid(row=2, column=1, padx=20)
email = tk.Entry(root, width=30)
email.grid(row=3, column=1, padx=20)
phonenumber = tk.Entry(root, width=30)
phonenumber.grid(row=4, column=1, padx=20)
f_name_label = tk.Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = tk.Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
title_label = tk.Label(root, text="Title")
title_label.grid(row=2, column=0)
email_label = tk.Label(root, text="Email")
email_label.grid(row=3, column=0)
phonenumber_label = tk.Label(root, text="Phonenumber")
phonenumber_label.grid(row=4, column=0)

#create buttons on interface, submit
submit_button = tk.Button(root, text="Add Contact to Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
#create buttons on interface, query
query_button = tk.Button(root, text="Show Contacts", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


#Commit
#
#Close connection
#conn.close()

root.mainloop()
