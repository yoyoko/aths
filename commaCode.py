spam = ['apples', 'bananas', 'tofu', 'cats']
#print(len(spam))

def comma(example):
    newString = ''
    for i in example:
        if i == spam[len(example)-1]:
            newString = newString + 'and ' + str(i)
        else:
            newString = newString + str(i) + ', '
    return newString

comma(spam)
