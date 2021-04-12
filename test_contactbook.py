import pytest
import contactbook as cbook

def test_contactinit():
    jake = contact("placeholder for image", "Jake","Stark", "Group Member", "Jakestark99@gmail.com", "(203) 913-5328")
    assert jake.first_name == "Jake"
