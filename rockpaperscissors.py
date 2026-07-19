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
    computerscore.config(text="computer score : "+str(cscore))
    playerscore.config(text="player score : "+str(pscore))

def playerwins():
    global pscore,cscore
    pscore+=1
    winner.config(text="player won")
    computerscore.config(text="computer score : "+str(cscore))
    playerscore.config(text="player score : "+str(pscore))
def tie():
    global pscore,cscore
    winner.config(text="tie")
    computerscore.config(text="computer score : "+str(cscore))
    playerscore.config(text="player score : "+str(pscore))

def getcomputerchoice():
    return random.choice(options)
    
def getplayerchoice(playerinput):
    global pscore,cscore
    print(playerinput)
    computerinput=getcomputerchoice()
    print(computerinput)
    playerchoice.config(text="you selected: "+playerinput[0])
    computerchoice.config(text="computer selected: "+computerinput[0])
    if playerinput==computerinput:
        tie()
    if playerinput[1]==0:
        if computerinput[1]==1:
            computerwins()
        elif computerinput[1]==2:
            playerwins()
    elif playerinput[1]==1:
        if computerinput[1]==0:
            playerwins()
        elif computerinput[1]==2:
            computerwins()
    elif playerinput[1]==2:
        if computerinput[1]==0:
            computerwins()
        elif computerinput[1]==1:
            playerwins()
        

title=Label(screen,text="Rock Paper Scissors",font=("Calibri",20))
title.place(x=150,y=0)
winner=Label(screen,text="Lets start the game",fg="green")
winner.place(x=200,y=100)

playeroptions=Label(screen,text="Your options",fg="red")
playeroptions.place(x=50,y=170)
rockb=Button(screen,text="Rock",bg="blue",fg="white",width=10,command=lambda:getplayerchoice(options[0]))
rockb.place(x=150,y=200)
paperb=Button(screen,text="Paper",bg="yellow",fg="black",width=10,command=lambda:getplayerchoice(options[1]))
paperb.place(x=250,y=200)
scissorsb=Button(screen,text="Rock",bg="green",fg="white",width=10,command=lambda:getplayerchoice(options[2]))
scissorsb.place(x=350,y=200)

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
