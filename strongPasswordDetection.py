#! python3
#strongPasswordDetection.py - tests a password to see if it is a strong password

import pyperclip, re

def strongPasswordDetection():

# get the string from clipboard
    password = str(pyperclip.paste())
    checker = 0

# regex to test the string
    if len(re.findall(r'[a-zA-Z0-9!@#$%/^&*()\-_+=]{8}', password)) >= 1:
        checker += 1
    else:
        print("Password should be eight characters or longer")

    if len(re.findall('[a-z]{1,7}', password)) >= 1:
        checker += 1
    else:
        print("Password should contain a lower case letter")

    if len(re.findall('[A-Z]{1,7}', password)) >= 1:
        checker += 1
    else:
        print("Password should contain an upper case letter")

    if len(re.findall('[0-9]{1,7}', password)) >= 1:
        checker += 1
    else:
        print("Password should contain a number")

    if len(re.findall(r'[!@#$%^&*()\-_+=/]{1,7}', password)) >= 1:
        checker += 1
    else:
        print("Password should contain a special character")

    #junk testing
    #print(re.findall(r'[a-zA-Z0-9!@#$%^&*()\-_+=/]{8}', password))
    #print(re.findall('[a-z]{1,7}', password))
    #print(re.findall('[A-Z]{1,7}', password))
    #print(re.findall('[0-9]{1,7}', password))
    #print(re.findall(r'[!@#$%^&*()\-_+=]{1,7}', password))
    #print(checker)

# output decision
    if checker >= 5:
        print("Password is strong")
    else:
        print("Password is not strong")

strongPasswordDetection()
