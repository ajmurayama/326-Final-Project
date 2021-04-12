### INST326 Group Project\
###Jake Stark

class contact():
    """ A class representing a contact that will exist within the contact book
        
        Attributes:
            pic: An image of the person
            first_name(str): The first name of the person on in the contact book
            last_name(str): The last name of the person
            title(str): Title of the person
            email(str): Contact's email
            phone(str): Contact's phone number
        
        Methods:
            edit_contact: Allows user to edit details of a contact
            equals: Allows for comparison of contact objects
        
    """
    pass
    def __init__(self, pic, first_name, last_name, title, email, phone):
        self.pic = pic
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.email = email
        self.phone = phone
    
    def equals(self, other):
        """ A method that will compare two contacts and return true if they are the same and false otherwise

            Params:
                other: contact that is being compared
            
            Returns:
                A boolean that returns true if the contacts are the same.
        """
        if self.first_name != other.first_name:
            return False
        if self.last_name != other.last_name:
            return False
        if self.title != other.title:
            return False
        if self.email != other.email:
            return False
        if self.phone != other.phone:
            return False
        return True
    
    
    