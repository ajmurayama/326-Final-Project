import pytest
import contactbook as cbook

def test_contactinit():
    jake = cbook.contact("placeholder for image", "Jake","Stark", "Group Member", "Jakestark99@gmail.com", "(203) 913-5328")
    assert jake.first_name == "Jake"
    assert jake.last_name == "Stark"
    assert jake.title == "Group Member"
    assert jake.email == "Jakestark99@gmail.com"
    assert jake.phone == "(203) 913-5328"
    
def test_falseequals():
    john = cbook.contact("placeholder for image", "John","Stark", "Group Member", "Jakestark99@gmail.com", "(203) 913-5328")
    jake = cbook.contact("placeholder for image", "Jake","Stark", "Group Member", "Jakestark99@gmail.com", "(203) 913-5328")
    assert jake.equals(john) == False
    
def test_trueequals():
    sam = cbook.contact("placeholder for image", "Sam","Gold", "Friend", "samg@gmail.com", "(203) 933-5558")
    sam_two = cbook.contact("placeholder for image", "Sam","Gold", "Friend", "samg@gmail.com", "(203) 933-5558")
    assert sam.equals(sam_two) == True
    

