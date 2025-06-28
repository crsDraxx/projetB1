from tkinter import*
from tkinter import simpledialog,messagebox
#from joueur import*
from jeu import* 

if __name__ == "__main__":
    root =Tk()
    Game=Jeu(root,"player1","player2")
    Game.run()
    