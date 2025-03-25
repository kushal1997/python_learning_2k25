import numpy as np

def rowWinner(board,player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x,y] != player:
                win = False
                continue
        if win == True:
            return win
        return win

def colWinner(board,player):
    for x in range(len(board)):
        win = True
        for y in range (len(board)):
            if board[y,x] != player:
                win = False
                continue
        if win == True:
            return win
        return win

def diagWinner(board,player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x,x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x,y] != player:
                win = False
    return win

def evaluate(board):
    winner = 0
    for player in [1,2]:
        if (rowWinner(board,player) or colWinner(board,player) or diagWinner(board,player)):
            winner = player
    if np.all(board !=0) and winner == 0:
        winner = -1
    return winner

def playGame():
    board = np.array([[0,0,0],[0,0,0],[0,0,0]])
    winner, counter = 0,1
    allPossibility = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    print(board)

    while winner == 0:
        for player in [1,2]:
            print("Turn for player --> Player : "+ str(player))
            selection = int(input("Select the number from "+ str(allPossibility) + " : "))
            if selection > len(allPossibility):
                print("Wrong selection, please select between 0 and ",len(allPossibility)-1)
                selection = int(input("Select the number from "+ str(allPossibility) + " : "))
            print(board[allPossibility[selection]])
            board[allPossibility[selection]] = player
            allPossibility.pop(selection)
            print("Board position after Round no "+ str(counter) + " - ")
            print(board)
            counter +=1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


                


print("Winner is : "+ str(playGame()))
