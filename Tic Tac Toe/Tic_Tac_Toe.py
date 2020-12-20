board = [' ' for x in range (10)]
def InsertLetter(letter , pos):
    board[pos] = letter
def SpaceIsFree(pos):
    return board[pos] == ' '
def PrintBoard(board):
    print("   |   |   ")
    print(" " + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print("   |   |   ")
def IsBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
def IsWinner(board , letter):
    return((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter))
def PlayerMove():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move <10:
                if SpaceIsFree(move):
                    run = False
                    InsertLetter("X" , move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number between 1 and 9 !")
        except:
            print("Please type a number ..!")
def ComputerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0
    for let in ["O" , "X"]:
        for i in possibleMoves:
            BoardCopy = board[:]
            BoardCopy [i] = let
            if IsWinner(BoardCopy , let):
                move = i
                return move
    CornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            CornersOpen.append(i)
    if len(CornersOpen) > 0:
        move = SelectRandom(CornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    EdgesOpen = []
    for i in possibleMoves:
        if i in [2 , 4 , 6 , 8]:
            EdgesOpen.append(i)
    if len(EdgesOpen) > 0:
        move = SelectRandom(EdgesOpen)
        return move
def SelectRandom(li):
    import random
    length = len(li)
    Rand = random.randrange(0,length)
    return li[Rand]

print("--------------------------")
print("Welcome to the Game: ")
PrintBoard(board)
while not(IsBoardFull(board)):
    if not(IsWinner(board , 'O')):
        PlayerMove()
        PrintBoard(board)
    else:
        print("Sorry you Loose !!")
        break
    if not(IsWinner(board , 'X')):
        move = ComputerMove()
        if move == 0:
            print(" ")
        else:
            if IsBoardFull(board):
                print("Tie Game ! Better luck next time ..!")
            else:
                InsertLetter('O' , move)
                print("Computer has placed an 'O' on position " , move , ":")
                PrintBoard(board)
    else:
        print("You Win !! Congratulations ...!!")
        break
