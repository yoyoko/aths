#! python3
#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

#Create phone regex
phoneRegex = re.compile(r''' (
    (\d{3}|\(\d{3}\))?  #area code - group 1
    (\s|-|\.)?  #seperator - group 2
    (\d{3}) #first 3 digits - group 3
    (\s|-|\.)   #seperator - group 4
    (\d{4}) #last four digits - group 5
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #(optional) extension - group 6, 7, 8
    )''', re.VERBOSE)

#Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username
    @
    [a-zA-Z0-9._%+-]    #domain name
    (\.[a-zA-Z]{2, 4})  #dot something
    )''', re.VERBOSE)

#Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
