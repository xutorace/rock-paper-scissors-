from tkinter import *
import random
screen = Tk()
screen.geometry("500x500")
pscore=0
cscore=0
options=[("rock",0),("paper",1),("scissors",2)]
def computerwins():
    global cscore,pscore
    cscore+=1
    winner.config(text="computer won")
    computerscore.config(text="computer score : "+str(csore))
    playerscore.config(text="player score : "+str(psore))

def playerwins():
    global pscore,cscore
    pscore+=1
    winner.config(text="player won")
    computerscore.config(text="computer score : "+str(csore))
    playerscore.config(text="player score : "+str(psore))
def tie():
    global pscore,cscore
    winner.config(text="tie")
    computerscore.config(text="computer score : "+str(csore))
    playerscore.config(text="player score : "+str(psore))

def getcomputerchoice():
    return random.choice(options)
    
title=Label(screen,text="Rock Paper Scissors",font=("Calibri",20))
title.place(x=150,y=0)
winner=Label(screen,text="Lets start the game",fg="green")
winner.place(x=200,y=100)

playeroptions=Label(screen,text="Your options",fg="red")
playeroptions.place(x=50,y=170)
rock=Button(screen,text="Rock",bg="blue",fg="white",width=10)
rock.place(x=150,y=200)
paper=Button(screen,text="Paper",bg="yellow",fg="black",width=10)
paper.place(x=250,y=200)
scissors=Button(screen,text="Rock",bg="green",fg="white",width=10)
scissors.place(x=350,y=200)

score=Label(screen,text="score")
score.place(x=50,y=250)
playerchoice=Label(screen,text="you selected : ---")
playerchoice.place(x=150,y=300)
computerchoice=Label(screen,text="computer selected : ---")
computerchoice.place(x=150,y=350)
playerscore=Label(screen,text="your score : -")
playerscore.place(x=300,y=300)
computerscore=Label(screen,text="computer score : -")
computerscore.place(x=300,y=350)
screen.mainloop()
