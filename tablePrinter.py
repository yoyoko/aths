tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)

    for line in range(len(table)):
        for word in range(len(table[line])):
            if colWidths[line] <= len(table[line][word]):
                colWidths[line] = len(table[line][word])
            else:
                colWidths[line] = colWidths[line]

    for li in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][li].rjust(colWidths[i]), end =" ")
        print()

printTable(tableData)
