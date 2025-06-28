from tkinter import*
from tkinter import simpledialog,messagebox

class Jeu:
    def __init__(self,fenetre,player1,player2,taille=8):
        self.__fenetre=fenetre
        self.__fenetre.title("Reign of Queens")

        #initialisation du plateau 
        self.__taille=taille #plateau initialisé 
        self.__tailleCase= 60
        self.__initBoard = [[None for _ in range(self.__taille)] for _ in range(self.__taille)]
        self.__selectedPiece= None
        self.__selectionCercle=None
        self.__turn="white"

        #nom joueurs et phrase de debut de Game
        self.__player1_name= player1
        self.__player2_name=player2
        self.__joueur_actuel=self.__player1_name
        self.__label=Label(self.__fenetre,text="Bienvenue sur le champs de bataille",font=("Helvetica"))
        self.__label.pack(pady=20,padx=10)

        #Création Menu
        self.__menuBar=Menu(self.__fenetre)
        self.__fenetre.config(menu=self.__menuBar)
        self.__principal_menu=Menu(self.__menuBar,tearoff=0)
        self.__menuBar.add_cascade(label="Game Options",menu=self.__principal_menu)

        #Options du menu
        self.__principal_menu.add_command(label="Board size", command=self.__boardSize)
        self.__principal_menu.add_command(label="Player Names", command=self.__playerNames)
        
        #Canvas pour le plateau
        self.__canvas=Canvas(self.__fenetre,width=self.__taille*self.__tailleCase, height=self.__taille*self.__tailleCase, bg="bisque3")
        self.__canvas.pack(pady=10)

        #nbr de pieces restantes
        self.__piecesPlayer1= Label(self.__fenetre,text=f"{self.__player1_name} (Blanc)- Pièces restantes:0",font=("Helvetica", 12))
        self.__piecesPlayer1.pack(pady=5)
        self.__piecesPlayer2= Label(self.__fenetre,text=f"{self.__player2_name} (Noire)- Pièces restantes:0",font=("Helvetica", 12))
        self.__piecesPlayer2.pack(pady=5)

        #relier click souris a clic plateayu
        self.__canvas.bind("<Button-1>", self.__clicPlateau)

        #Afficher le joueur actuel
        self.__label_Joueur= Label(self.__fenetre, text =f"Joueur Actuel :{self.__joueur_actuel} ({self.__turn})", font=("Helvetica",14))
        self.__label_Joueur.pack()

        self.__message_label =Label(self.__fenetre, text="", fg="red", font=("Arial", 12))
        self.__message_label.pack()
        self.__dessinerPlateau()
        self.__placerPieces()

    def __dessinerPlateau(self):
        self.__canvas.delete("all")
        for i in range(self.__taille):
         for j in range(self.__taille):
             x1=j*self.__tailleCase
             y1=i*self.__tailleCase
             x2=x1+self.__tailleCase
             y2=y1+self.__tailleCase
             couleur= "MistyRose2" if (i+j)% 2 == 0 else "PaleTurquoise1"
             self.__canvas.create_rectangle(x1,y1,x2,y2,outline="black",fill=couleur)

    def __boardSize(self):  #modifier taille plateau
       def confirmer():
          try: #permet d'eviter que le programme plante en cas operation non aboutie ou val incorrectes
                new_BoardSize = int(Saisie_taille.get())
                if 6 <= new_BoardSize <= 12 and new_BoardSize%2 ==0:
                    self.__taille=new_BoardSize
                    self.__initBoard=[[None for _ in range(self.__taille)]for _ in range(self.__taille)]
                    self.__canvas.config(width=self.__taille*self.__tailleCase, height=self.__taille*self.__tailleCase)
                    self.__dessinerPlateau()
                    self.__placerPieces()
                    fenetre_taille.destroy()
                else:
                    message_Erreur.config(text="Taille saisie invalide (doit etre pair entre 6 et 12)")
          except ValueError:
             message_Erreur.config(text="Entrez un nombre VALIDE")

       fenetre_taille = Toplevel(self.__fenetre)
       fenetre_taille.title("Taille plateau")
       instruction= Label(fenetre_taille,text="Entrez la taille du plateau (pair entre 6 et 12:)")
       instruction.pack(padx=10,pady=5)

       Saisie_taille=Entry(fenetre_taille)
       Saisie_taille.pack(padx=10,pady=5)

       validerButt=Button(fenetre_taille,text="Valider", command=confirmer)
       validerButt.pack(padx=10,pady=10)

       message_Erreur= Label(fenetre_taille,text="",fg="red")
       message_Erreur.pack()

    def __placerPieces(self):
        #initialiser la position des reines
        self.__initBoard[0][self.__taille-1]= "R_white"
        self.__initBoard[self.__taille-1][0]= "R_black"

        #nbr de tours par reine
        nbrTours= (self.__taille**2)//4-1
        self.__placerTour(0, self.__taille-1,"T_white",nbrTours)
        self.__placerTour(self.__taille-1, 0,"T_black",nbrTours)

        #dessiner les pieces a leur position respective
        for i in range(self.__taille):
            for j in range(self.__taille):
                if self.__initBoard[i][j]:
                    self.__dessinerPiece(i,j,self.__initBoard[i][j])

    def __placerTour(self,posReine_i,posReine_j,couleurTour,nbrTours):
        tour_placée=0
        zoneTours= int(nbrTours**0.5) #calcul la racine carré pour avoir la longueur d'un coté

        for Rang in range(-zoneTours,zoneTours+1):
            for Col in range(-zoneTours,zoneTours+1):
                x,y=posReine_i+Col, posReine_j+Rang
                if 0 <= x < self.__taille and 0 <= y < self.__taille and self.__initBoard[x][y] is None:
                    self.__initBoard[x][y]= couleurTour
                    tour_placée+=1
                    if tour_placée == nbrTours:
                        return
                    
    def __dessinerPiece(self,i,j,piece):
        #coordonnée d'une piece a dessiner sur le plateau
        x1, y1=j*self.__tailleCase, i*self.__tailleCase
        x2, y2= x1 + self.__tailleCase, y1+ self.__tailleCase
        centreX,centreY= (x1+x2)//2,(y1+y2)//2

        #background piece
        self.__canvas.create_oval(x1+5,y1+5,x2-5,y2-5, fill=self.__couleurPiece(piece), outline="black",tags="piece")

        #symbole piece
        symbole, couleurSymbole=self.__symbolePiece(piece)
        self.__canvas.create_text(centreX,centreY,text=symbole,font=("Helvetica",24),fill=couleurSymbole,tags="piece")

    def __couleurPiece(self,piece):
        if "R_white" in piece:
            return "red2"
        elif "R_black" in piece:
            return "magenta3"
        elif "T_white" in piece:
            return "DarkGoldenrod2"
        elif "T_black" in piece:
            return "gray51"
        
    def __symbolePiece(self,piece):
        if "R" in piece:
            return "♛","white" if "white" in piece else "black"
        elif "T"in piece:
            return "♜","white" if "white" in piece else "black"
        
    def __clicPlateau(self,event): #gerer linteraction entre le joueur et le plateau
        j,i=event.x//self.__tailleCase,event.y//self.__tailleCase

        if self.__initBoard[i][j] and self.__turn in self.__initBoard[i][j]:
            self.__selectedPiece=(i,j)
            self.__highlight_selectedPiece()
        elif self.__selectedPiece:
            old_i, old_j=self.__selectedPiece
            if self.__deplacement(old_i,old_j,i,j):
                self.__selectedPiece=None
                self.__remove_selectionCercle()

    def __deplacement(self,old_i,old_j,new_i,new_j):
        piece= self.__initBoard[old_i][old_j]

        if not self.__deplacementPossible(piece,old_i,old_j,new_i,new_j):
            self.__message("Déplacement invalide!")
            return False
        
        #mettre a jour la position dune piece
        self.__initBoard[old_i][old_j]=None
        self.__initBoard[new_i][new_j]=piece
        self.__canvas.delete("piece")
        self.__canvas.delete("highlight")

        for i in range(self.__taille):
            for j in range(self.__taille):
                if self.__initBoard[i][j]:
                    self.__dessinerPiece(i,j,self.__initBoard[i][j])

        self.__turn="black" if self.__turn == "white" else "white"
        self.__joueur_actuel= self.__player2_name if self.__turn == "black" else self.__player1_name
        self.__label_Joueur.config(text=f"Joueur Actuel : {self.__joueur_actuel} ({self.__turn})")
        self.__MAJ_pieces_restante()
        self.__message("")
        return True

    def __deplacementPossible(self,piece,old_i,old_j,new_i,new_j):
        if not (0 <= new_i < self.__taille and 0 <= new_j < self.__taille):
            return False
        
        if self.__initBoard[new_i][new_j] and self.__turn in self.__initBoard[new_i][new_j]:
            return False
        
        #regle de deplacement des tours
        if "T" in piece:
            if old_i != new_i and old_j != new_j: #interdire les mvt en diago
                return False
            if old_i == new_i : #mvt orthogonaux
                step=1 if new_j > old_j else -1
                for j in range (old_j + step, new_j,step):
                    if self.__initBoard[old_i][j]:
                        return False
            elif old_j == new_j:
                step = 1 if new_i > old_i else -1
                for i in range(old_i+step,new_i,step):
                    if self.__initBoard[i][old_j]:
                        return False

            #regle deplacement reine
        elif "R" in piece:
            if old_i == new_i: #mvt orthogonaux
                step=1 if new_j > old_j else -1
                for j in range (old_j + step, new_j,step):
                    if self.__initBoard[old_i][j]:
                        return False
            elif old_j == new_j:
                step = 1 if new_i > old_i else -1
                for i in range(old_i+1,new_i,step):
                    if self.__initBoard[i][old_j]:
                        return False
            elif not (abs(new_i - old_i) == abs(new_j - old_j) or old_i==i or old_j==j):#mvt diago
                step_i = 1 if new_i > old_i else -1
                step_j = 1 if new_j > old_j else -1

                i, j = old_i + step_i, old_j + step_j
                while i != new_i and j != new_j:
                    if self.__initBoard[i][j]:
                        return False
                    i += step_i
                    j += step_j

        return True
    
        

    def __highlight_selectedPiece(self):
        if self.__selectionCercle:
            self.__canvas.delete(self.__selectionCercle)

        i, j = self.__selectedPiece
        x1, y1 = j * self.__tailleCase, i * self.__tailleCase
        x2, y2 = x1 + self.__tailleCase, y1 + self.__tailleCase

        self.__selectionCercle = self.__canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, outline="medium blue", width=3, tags="highlight")

   

    def __remove_selectionCercle(self):
        if self.__selectionCercle:
            self.__canvas.delete(self.__selectionCercle)
            self.__selectionCercle = None

    def __MAJ_pieces_restante(self):
        player1_count=sum( 1 for i in self.__initBoard for piece in i if piece and "white" in piece)
        player2_count=sum(1 for i in self.__initBoard for piece in i if piece and "black" in piece)

        self.__piecesPlayer1.config(text=f"{self.__player1_name} (Blanc)- Pieces restantes: {player1_count}")
        self.__piecesPlayer2.config(text=f"{self.__player2_name} (Noire)- Pieces restantes: {player2_count}")

    def __message(self, message):
        self.__message_label.config(text=message)
                
    def __playerNames(self):
        player1= simpledialog.askstring("Player 1 NAME","Entrer un nom pour le player 1")
        if player1:
            self.__player1_name=player1

        player2= simpledialog.askstring("Player 2 NAME","Entrer un nom pour le player 2")
        if player2:
            self.__player2_name=player2

    
    def getInitBoard(self):
        return self.__initBoard

    def run(self):
        self.__fenetre.mainloop()   

