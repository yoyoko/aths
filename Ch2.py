#spam = 0
#if spam < 5:
    #print("Hello World.")
    #spam = spam + 1

#while spam < 5:
    #print(f"Hello World{spam}")
    #spam = spam + 1

#an annoying while loop
#name = ' '
#while name != 'your name':
    #print('Please type your name.')
    #name = input('> ')
#print("Thank you!")

name = ''
while not name:
    print('Enter your name')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print("Be sure to have enough room for all your guests.")
print('Done')
