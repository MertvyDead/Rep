import random 
from task2 import *
import matplotlib.pyplot as plt

class warrior(Dagger,Sword):
    def __init__(self, name):
        self.name = name    
        self.health = 20
        self.attack_power = 2
        
        
    def show_cr_info(self):
        inf= (f'{self.name} Здоровье: {self.health}')
        print(inf)
        
    def dmg_taken(self, new_health):
        self.health = new_health
        
    def equip_weapone_Dagger(self,):
        self.attack_power = Dagger.dmg
        
    def equip_weapone_Sword(self):
        self.attack_power = Sword.dmg
    def rest(self):
        self.health = 20
 
 
 
war1 = warrior('Pena')
war1.equip_weapone_Dagger
war2= warrior('Glad')
war2.equip_weapone_Sword
war1.show_cr_info()
war2.show_cr_info()

def fight(a,b,c,t):
    for i in range(t): 
            while a.health > 0 and b.health > 0:
                new_health = a.health - random.randint(0,b.attack_power)
                a.dmg_taken(new_health)
                new_health = b.health - random.randint(0,a.attack_power)
                b.dmg_taken(new_health)
                a.show_cr_info()
                b.show_cr_info()
            if a.health <=0:
                    print(f'{b.name} победил!!!') 
                    c[1] += 1
                    a.rest()
                    b.rest()
            elif b.health <= 0:
                    print(f'{a.name} победил!!!') 
                    c[0]+= 1
            a.rest()
            b.rest()          
    return(c)

vals = [0,0]
fight(war1,war2,vals,5)
labels = ["Победы Pena", "Победы Glad"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение побед")
plt.show()