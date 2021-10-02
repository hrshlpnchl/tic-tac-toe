referenceBoard = {'a':'a','b':'b','c':'c',
                  'd':'d','e':'e','f':'f',
                  'g':'g','h':'h','i':'i'}
def printBoard(board):
    print(board['a'] + '|' + board['b'] + '|' + board['c'])
    print('-+-+-')
    print(board['d'] + '|' + board['e'] + '|' + board['f'])
    print('-+-+-')
    print(board['g'] + '|' + board['h'] + '|' + board['i'])
print('Here is the identity of places for your reference:')
printBoard(referenceBoard)
print("Now let's start the game!")
theBoard = {'a':' ','b':' ','c':' ',
            'd':' ','e':' ','f':' ',
            'g':' ','h':' ','i':' '}
places = ['a','b','c','d','e','f','g','h','i']
previousMoves = []
turn = 'O'
printBoard(theBoard)
for i in range(9):
    print('Turn for ' + turn + '. Where do you want to mark ' + turn + '?')
    while True:
        move = input()
        if move not in places:
            print("You have chosen incorrect place. Please choose from 'a' to 'i'.")
        elif move in previousMoves:
            print('Sorry! This place already has an ' + theBoard[move] +
              '. Please choose an another place.')
        else:
            theBoard[move] = turn
            previousMoves += move
            break
    printBoard(theBoard)
    if theBoard['a'] != ' ' and ((theBoard['a'] == theBoard['b'] and theBoard['a'] == theBoard['c']) or (theBoard['a'] == theBoard['d'] and theBoard['a'] == theBoard['g'])):
        print('The player ' + theBoard['a'] + ' won.')
        break
    elif theBoard['e'] != ' ' and ((theBoard['e'] == theBoard['b'] and theBoard['e'] == theBoard['h']) or (theBoard['e'] == theBoard['d'] and theBoard['e'] == theBoard['f']) or (theBoard['e'] == theBoard['a'] and theBoard['e'] == theBoard['i']) or (theBoard['e'] == theBoard['c'] and theBoard['e'] == theBoard['g'])):
        print('The player ' + theBoard['e'] + ' won.')
        break
    elif theBoard['i'] != ' ' and ((theBoard['i'] == theBoard['c'] and theBoard['i'] == theBoard['f']) or (theBoard['i'] == theBoard['g'] and theBoard['i'] == theBoard['h'])):
        print('The player ' + theBoard['i'] + ' won.')
        break
    elif i == 8:
        print('Nobody won. The game is draw.')
    else:
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'
    
