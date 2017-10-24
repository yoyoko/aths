#! python3
# mcb.py - saves and loads pieces of text to the clipboard
# usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - loads keyword to clipboard
#       py.exe mcb.pyw list - loads all keywords to clipboard
#       py.exe delete <keyword>
#       py.exe delete

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save Clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste() #keyword is argument[2] and contents are paste()
# List keywords and load content
elif len(sys.argv) == 2 and sys.argv[1].lower() is not 'delete':
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]] 

if len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    mcbShelf.clear()

mcbShelf.close()
