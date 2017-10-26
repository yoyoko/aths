#! python3
# madlibs.py - reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

import re

# define regex
verbRegex = re.compile(r'verb', re.I)
nounRegex = re.compile(r'noun', re.I)
adjectiveRegex = re.compile(r'adjective', re.I)

textfile = open('madlibs.txt')

content = textfile.read()
textfile.close()

index = 0
newMadLib = []

for word in content.split():
    newMadLib.append(word)
    if verbRegex.search(word) != None:
        x = input('Enter VERB:  ')
        newMadLib[index] = x
    elif nounRegex.search(word) != None:
        x = input('Enter NOUN:  ')
        newMadLib[index] = x
    elif adjectiveRegex.search(word) != None:
        x = input('Enter ADJECTIVE:  ')
        newMadLib[index] = x
    index += 1

newMadLib = (' ').join(newMadLib)

print(content)
print (newMadLib)
