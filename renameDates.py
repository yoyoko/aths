#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# create a regex that matches files with the American date format
datePattern = re.compile("""^(.*?)) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir():
    mo = datepattern.search(amerFilename)

# Skip files without a date.
    if mo == None:
        continue

# Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# Form the European-style filenames
    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart) + afterPart

# Get the full, absolute file pats.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absworkingDir, amerFilename)
    euroFilename = os.path.join(absworkingDir, euroFilename)

# Rename the files
    shututil.move(amerFilename, euroFilename)
