from pprint import pprint
import random
import math
class hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname): #H mean hero to short it. A class is a blueprint for a way for us varibal pass throw it
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname
        
    def getHealth(self): # is creates a function in python that we can type in to to return the health variable or attribute
        return self.health 
    def getAttack(self):
        return self.attack #it means that i can return to them any time if i was to call them *ring ring*
    def getLuck(self):
        return self.luck
    def getRanged(self):
        return self.ranged
    def getDefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getName(self):
        return self.name
            #seter what we can change attribute, expel while in game then we want to change one of the attack then we use setter to set a new attack value cus this is a private class we dont want user just to be able to kind of makee changes of as and when we want changes to happend in the specific order that we programmed them to happen.

    def setHealth(self, newHealth):
            self.health = newHealth     #newHealth passed into this prameter new health then goes into my self.health and passed back to line 2 and we get a new health variable and doing all the same with my attributes 

    def setAttack(self, newAttack):
        self.attack = newAttack #future prrofing my class for i what i want  to actually change some attributes i can then do it later in the future by calling them
            #if i need to get  something here i can just use the functions
           #if i need to set, set anything new if anything changes in mid game then i can set them there becuas im cool and not you!!!! :)
    def setLuck(self, newLuck):
        self.luck = newLuck
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setDefence(self, newDefence):  
        self.defence = newDefence
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setName(self, newName):
        self.name = newName

class enemy:
    def __init__ (self, Ehealth, Eattack, Especial, Echance, Ename):
        self.health = Ehealth       #when we make a new  charcther will it go down from the list
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance 
        self.name = Ename

    def getHealth(self):    #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        return self.health
    def getAttack(self):
        return self.attack
    def getSpecial(self):
        return self.special
    def getChance(self):
        return self.chance
    def getName(self):
        return  self.name
    
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    def setChance(self, newChance):
        self.chance = newChance
    def setName(self,  newName):
        self.name = newName    
# we gonna make a boss class and inhert the class enemy code.
class boss (enemy):
    def __intit__(self, Ehealth, Eattack, Especial, Echance, Ename, EsuperMove):
        super().__init__ (Ehealth, Eattack, Especial, Echance, Ename,) #2 we used the super function and inherit this part of the enmey class  so we did have to do the geter and selfer #super  what we need to inherit the previous class listet above and super gonna look on the  class boss enemy and will look a part of enmey class this  super attibute will look att "code" and will inhert the will apper in the  enemey  
        self.superMove = EsuperMove
    def getSuper(self):
        return self.superMove
    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove

    
def enemyGen(levelBoss): 
    temp = []
    file = open ("adjective.txt","r")
    lines = file.readlines() #its look at every line in the adjective  
    adjective = lines[random.randint(0,len(lines)-1)][:-1] #it gonna be a random intger to 0 and the ammount of  lines in the file -1 it reads  from one and all the way don to the end [:-1] it remove symbol at end
    file.close
    file = open ("animal.txt","r")
    lines = file.readlines()
    animal = lines[random.randint(0,len(lines)-1)][:-1]
    file.close

    if levelBoss == False: #if we say dont generat a boss we re gonna generat a normal enemy
        health = random.randint(50,100)
        attack = random.randint(1,10)
        special = random.randint(10,20)
        chance = random.randint(1,10)

        return enemy(health, attack, special, chance, adjective+" "+animal)#the " " is going to genrat a name bettween adjective and animal. we call this class enemy and then just return  the argument in order, call the class  enemey these attibutes which  we creted  ones to be pluged in  and therfor creating the enemy
    else: # Here the boss if we dont ge a normal enemy
        health = random.randint(200,250)
        attack = random.randint(20,40)
        special = random.randint(50,60)
        chance = random.randint(1,8)
        superMove = random.randint(100,200)
        return boss(health, attack, special, chance, adjective+" "+animal, superMove) #pluging in the attriebute that we  creted these and we say return  the boss objcets  that we creted from the boss class and the attriebute  we just  genrtated.
    
levelBoss = False
en1 = enemyGen(levelBoss) #becuase this is set is false this will call the enemey genartor and it will go into full sper  and it will crete  a enemy objekt in enemy class  no a boss object
pprint(vars(en1)) 