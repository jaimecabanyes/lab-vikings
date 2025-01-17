
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
         self.health = health
         self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
   
# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
    
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"



# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        return None
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def VikingAttack(self):
        
