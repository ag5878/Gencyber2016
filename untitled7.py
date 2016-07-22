# -*- coding: utf-8 -*-
"""
Anna Ganguly
Gencyber
Pokemon Go
7/13/16
"""

from random import randint

class Pokemon:
    def __init__(self, oriName, oriType, orihp):
        self.name = oriName        
        self. type = oriType
        self.hp = orihp
        self.cp = randint(1, 600)

def battle(self, opponent, opponentMove):
    print(self.name +"Used" +myMove + "!!!")
    opponent.hp -= (self. moves[myMove] *self.cp)
    print(opponent.name + "HAS" +str(opponent.hp) + "HP LEFT!!!")
    if opponent.hp <= 0:
        print(opponent.name + "DIED!!!")
        print("YOU WIN!!!")
        return
    print(opponent.name +"Used" +opponentMove + "!!!")
    self.hp -= (opponent. moves[opponentMove] *opponent.cp)
    print(self.name + "HAS" str(self.hp) + "HP LEFT!!!")
    if self.hp <= 0:
        print(self.name + "DIED!!!")
        print("YOU LOSE!!!")
        return
    print(opponent.name + "USED" +opponentMove):
        


eevee_moves = {"Swift": 10, "Dig":20}
vee = Pokemon("Eevee", "Normal", 5)    
 
squirtle_moves= {"Squirt": 40 "Water Gun":100}   
squats = Pokemon("Squirtle", "Fire", 90)


        