import random                       #importing random module for random choices

#assigning variable to store the scores of user & computer
uscore=0
cscore=0

#function used to check the choice of the user
def uchoices(uchoice):
    if uchoice==1:
         uc="rock"
         return uc
    elif uchoice==2:
        uc="paper"
        return uc
    elif uchoice==3:
        uc="scissor"
        return uc

#defining the condition which states the winner of the game
while True:
    uc=eval(input('''Enter your choice                      
                  1 Rock,
                  2 Paper,
                  3 Scissor: '''))                      #taking input from the user
    c=random.choice(["paper", "rock", "scissor"])       #by random module computer chooses random options from given
    u=uchoices(uc)

    if u == c:
        print('draw\n',"You Choose",u,",","Computer choosen",c)
    elif (u=="rock" and c=="scissor") or (u=="paper" and c=="rock") or (u=="scissor" and c=="paper"):
        print('you won\n',"You Choose",u,",","Computer choosen",c)
        uscore+=1
        print()
    else:
        print("computer won\n","You Choose",u,",","Computer choosen",c)
        cscore+=1

    print("Your score=",uscore)
    print("computer score=",cscore,"\n")




