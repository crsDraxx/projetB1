def newBoard(n) :
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1) :
        board[i][0] = 1  # Pions du joueur 1 (colonne de gauche)
    for j in range(1, n) :
        board[n-1][j] = 2  # Pions du joueur 2 (ligne du bas)
    return board

def displayBoard(board, n) :
    for i in range(n):
        print(i+1, " ", end="")
        for j in range(n):
            if board[i][j]==0:
                print(" . ", end="")
            elif board[i][j]==1:
                print(" x ", end="")
            elif board[i][j]==2:
                print(" o ", end="")
        print()
    print("  ",end="")
    for col in range(n):
        print(" ", col+1, end="")
    print()

def possiblePawn(board, n, directions, player,  i, j):
    def validPosition():
        return 0 <= i < n and 0 <= j < n
    def playerPawn():
        return board[i][j] == player
    def possibleMove():
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
                return True
        return False
    return validPosition() and possibleMove() and playerPawn()

def selectPawn(board, n, directions, player):
    while True:
        print("Au joueur", str(player), "de jouer")
        i = int(input("Choisir la ligne d'un pion :"))-1
        j = int(input("Choisir la colonne d'un pion :"))-1
        if possiblePawn(board, n, directions, player, i, j):
            return i, j

def possibleMove(board, n, directions, player, i, j, m):
    ni, nj = 1 + directions[m-1][0], j + directions[m-1][1]

    def isInBounds():
        return 0 <= ni < n and 0 <= nj < n
    
    def targetEmpty():
        return board[ni][nj] == 0
    
    return isInBounds() and targetEmpty()

def selectMove(board, n, directions, player, i, j):
    while True:
        m= int(input("Choisir la direction du mouvement (1 pour Nord, 2 pour Est, 3 pour Sud et 4 pour Ouest) :"))
        if 1 <= m <= 4 and possibleMove(board, n, directions, player, i, j, m):
            return m

def move(board, n, directions, player, i, j, m):
    ni, nj = i + directions[m-1][0], j + directions[m-1][1]
    board[ni][nj] = player
    board[i][j] = 0

def win(board, n, directions, player):
    if player == 1:
        return any(board[i][n-1] == 1 for i in range(n)) #joueur 1 gagne s'il atteint la derniere colonne
    elif player == 2:
        return any(board[0][j] == 2 for j in range(n)) #joueur 2 gagne s'il atteint le haut
    return False

def dodgem(n):
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    board = newBoard(n)
    player = 1
    while True:
        displayBoard(board, n)
        i,j= selectPawn(board, n, directions, player)
        m = selectMove(board, n, directions, player, i, j)
        move(board, n, directions, player, i, j, m)
        if win(board, n, directions, player):
            displayBoard(board, n)
            print("Vainqueur :",player)
            break
        player = 2 if player == 1 else 1
#choissisez un nombre pour faire un plateau n*n cases(exemple:5)
dodgem(5)




