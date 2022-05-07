from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health = 5, level = 1):
        self.__name = name
        self.__level = level
        self.__health = health

    #Getters
    def getName(self):
        return self.__name

    def getLevel(self):
        return self.__level

    def getHealth(self):
        return self.__health


    #Setters
    def setName(self, name):
        self.__name = name

    def setLevel(self, level):
        self.__level = level

    def setHealth(self, health):
        self.__health = health


    #Action
    @abstractmethod
    def battle(self, combat, level):
        pass


class Player(Character):

    def __init__(self, name, combat, health=5, level=1, xp=0, xpMax = 100, maxHealth = 5):
        super().__init__(name, health, level)
        self.__combat = combat
        self.__xp = xp
        self.__xpMax = xpMax
        self.__maxHealth = maxHealth

    #Getters
    def getCombat(self):
        return self.__combat
    
    def getXPMax(self):
        return self.__xpMax

    def getXP(self):
        return self.__xp

    def getMaxHealth(self):
        return self.__maxHealth

    #Setters
    def setCombat(self, combat):
        self.__combat = combat

    def setXPMax(self, xpMax):
        self.__xpMax = xpMax

    def setXP(self, xp):
        self.__xp = xp

    def setMaxHealth(self, health):
        self.__maxHealth = health


    #Level Up system
    def collectXP(self, xpCollected):
        self.setXP(self.getXP() + xpCollected)

    def checkXP(self):
        if (self.getXP() >= self.getXPMax()):
            self.levelUp()

        else:
            pass

    def levelUp(self):
        print (f'Congratulations! {self.getName()} has leveled up to level {self.getLevel()!}')

        self.setXP(self.getXP() % self.getXPMax())
        self.setLevel(self.getLevel() + 1)
        self.setXPMax(self.getXPMax + (self.getLevel() * 100))
        self.setMaxHealth(self.getMaxHealth() + 3)
        self.setHealth(self.getMaxHealth())

    #Combat System

    def checkCombat(self):
        if (self.getCombat() == True):
            self.inBattle()
        else:
            pass


    def inBattle(self):
        if (self.getHealth() > 0):
            print (f'Please select a move to use:\n'
                   f'1) Punch (1 Damage)\n'
                   f'2) kick (2 Damage)\n')
            
            attackChosen = int(input())

            self.attackResult(attackChosen)

        else:
            print('The player has lost the battle')

            self.setHealth(self.getMaxHealth() // 2)

    def attackResult(self, attackChosen):
        if (attackChosen == 1):
            inflictDamage = 1
            pass

    
        

    

        

