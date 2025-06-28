def newBoard(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def displayBoard(board,n):
    for i in range(n):
        print(i +1, " ",end="")
        for j in range(n):
            if board[i][j] == 0:
                print(" . ",end="")
            elif board[i][j] == 1:
                print(" x ",end="")
            elif board[i][j] == 2:
                print(" o ",end="")
        print()
    print("    ", end="")
    for col in range(1, n + 1):
        print(col, " ", end="")
    print()
            
def possibleSquare(board,n,player,i,j):
    if 0 < i >= n and 0 < j >= n :
        return False
    if board[i][j] != 0:
        return False
    opponent = 2 if player == 1 else 1
    if (i>0 and board[i-1][j] == player) or \
    (i< n-1 and board [i+1][j] == player) or \
    (j>0 and board[i][j-1] == player) or \
    (j < n-1 and board[i][j+1] == player):
        return False
    return True

def selectSquare(board,n,player):
    while True:
        print("Au joueur", str(player), "de jouer")
        i = int(input("Choisir un numéro de ligne :"))-1
        j = int(input("Choisir un numéro de colonne :"))-1
        if possibleSquare(board, n, player, i, j):
            return i, j

def updateBoard(board,player,i,j):
    board[i][j] = player

def again(board,n,player):
    for i in range(n):
        for j in range(n):
            if possibleSquare(board, n, player, i, j):
                return True
    return False

def snort(n):
    board = newBoard(n)
    current_player = 1
    player = 1
    while True:
        displayBoard(board,n)
        i, j = selectSquare(board,n,current_player)
        updateBoard(board, current_player, i, j)
        if not again(board,player, current_player):
            print("Vainqueur :",3-current_player)
        break
        current_player = 3- current_player

snort(6)
