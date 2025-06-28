from tkinter import *
from joueur import *
from ReignOfQueen import *
 
class Joueur:
    def __init__(self,fenetre,player1,player2,nom, couleur ):
        self.__fenetre=fenetre
        self.__fenetre.title("Reign of Queens")
 
        #nom joueurs et phrase de debut de Game
        self.__player1_name= player1
        self.__player2_name=player2
        self.__joueur_actuel=self.__player1_name
        self.__label=Label(self.__fenetre,text="Bienvenue sur le champs de bataille",font=("Helvetica"))
        self.__label.pack(pady=20,padx=10)
        #Afficher le joueur actuel
        self.__label_Joueur= Label(self.__fenetre, text =f"Joueur Actuel :{self.__joueur_actuel} ({self.__turn})", font=("Helvetica",14))
        self.__label_Joueur.pack()
 
        self.__message_label =Label(self.__fenetre, text="", fg="red", font=("Arial", 12))
        self.__message_label.pack()
 
 
        self.nom = nom
        self.couleur = couleur