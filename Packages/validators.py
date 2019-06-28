import re

def phoneNumberValidator(number):
    pattern="^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][6-9][0-9]{10}$"
    if re.match(pattern,str(number)):
        return True
    return False
phoneNumberValidator(987654322312)
def emailValidator(email):
    pat="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{2,18}[.][a-z]{2,4}$"
    if re.match(pat,str(email)):
        return True
    return False
emailValidator("sahithi123@gmail.com")