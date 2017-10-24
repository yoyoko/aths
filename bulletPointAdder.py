#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the lines list
    lines[i] = f'* {lines[i]}' #add star to each line
text = '\n'.join(lines)

pyperclip.copy(text)
