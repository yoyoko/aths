theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(f"It is {turn}'s turn. Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
