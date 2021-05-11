### INST326 Group Project\
###Jake Stark
import sqlite3

    
### Amanda Murayama
class contact_book():
    def __init__(self):
        filename = "contactbook.db"
        connection = sqlite3.connect(filename)
        self.my_cursor = connection.cursor()
        #create ="CREATE TABLE contact (first_name TEXT, last_name TEXT, title TEXT, Email TEXT, phone TEXT)"
        #self.my_cursor.execute(create)
    
    def add_contact(self, first_name, last_name, title, email, phone):
        sql = "Insert into contact values ('"+first_name+"','"+last_name+"','"+title+"','"+email+"','"+phone+"');"
        self.my_cursor.execute(sql)
        
    def delete_contact(self, first_name, last_name):
        sql = "Select count(*) from contact where first_name = '"+first_name+"' and last_name = '"+last_name+";"
        self.my_cursor.execute(sql)
        count = self.my_cursor.fetchone()[0]
        if count == 0:
            print("Not a valid contact")
        elif count > 1:
            print("More than one contact with that name")
        else:
            sql = "Delete from contact where first_name = '"+first_name+"' and last_name = '"+last_name+";"
            self.my_cursor.execute(sql)
    
    def edit_contact(self, first_name, last_name, title, email, phone):
        sql = "Select count(*) from contact where first_name = '"+first_name+"' and last_name = '"+last_name+";"
        self.my_cursor.execute(sql)
        count = self.my_cursor.fetchone()[0]
        if count == 0:
            print("Not a valid contact")
        elif count > 1:
            print("More than one contact with that name")
        else:
            sql = "Update contact set title = '"+title+"', email = '"+email+"', phone = '"+phone+"' where first_name = '"+first_name+"' and last_name = '"+last_name+";"
            self.my_cursor.execute(sql)
    
    def view_contacts(self):
        sql = "Select * FROM contact"
        result = self.my_cursor.execute(sql).fetchall()
        for row in result:
            print(row)
            print("\n")
    
#Jake Stark
#This if for presentation use to show the SQL features are currently working
if __name__ == "__main__":
    cbook = contact_book()
    cbook.add_contact("Jake", "Stark", "group member", "jakestark99@gmail.com", "203-913-5328")
    cbook.add_contact("Jim", "Bob", "guy", "jimbob@gmail.com", "207-943-5528")
    cbook.add_contact("Joe", "Goodman", "guy", "jgoodman@gmail.com", "207-943-5528")
    cbook.add_contact("Karen", "Wally", "cousin", "kwal@yahoo.com", "750-260-3215")
    cbook.add_contact("Gabriel", "Cruz", "Teacher", "gcruz@umd.edu", "240-854-9567")
    cbook.add_contact("Kim", "Smith", "TA", "kismith@umd.du", "240-978-6754")
    cbook.add_contact("Un", "Wanted", "random", "unwan@gmail.com", "965-454-7865")
    
    cbook.delete_contact('Un', 'Wanted',)
    cbook.view_contacts()