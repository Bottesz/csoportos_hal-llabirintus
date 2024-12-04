import random

class Player:
    def __init__(self,skill:int=0,Warrior_name:str="FoxRudy", hp:int=0, luck:int=0, emo:str="H", poz:int=0, gold:int=0,item:int=0):
        self.skill=self.dobas_skill()
        self.Warrior_name=Warrior_name
        self.hp=self.dobas_hp()
        self.luck=self.dobas_luck()
        self.emo=emo
        self.poz=poz
        self.gold=gold
        self.item=item
    
    def set_hp(self,hp):
        self.hp -= hp

    def set_gold(self,gold):
        self.gold+=gold;
        
    def dobas_skill(self):
        return random.randint(1,6)+6
    
    def dobas_hp(self):
        return random.randint(1,6)+ random.randint(1,6)+12
    
    def dobas_luck(self):
        return random.randint(1,6)+6
    
    def __str__(self):
        return (f"Skill: {self.skill}, Név: {self.Warrior_name} HP: {self.hp}, Luck: {self.luck}, Karakter: {self.emo}, Pozíció: {self.poz}")
    
class Enemy:
    def __init__(self, skill:int=0, hp:int=0, emo_e:str="👺", enemy_poz:int=0, enemy_name:str="Monster"):
        self.skill=self.dobas_skill()
        self.enemy_name=enemy_name
        self.hp=self.dobas_hp()
        self.emo_e=emo_e
        self.enemy_poz=enemy_poz

    def dobas_skill(self):
        return random.randint(1,6)+6
    
    def dobas_hp(self):
        return random.randint(1,6)+ random.randint(1,6)+12

    def __str__(self):
        return (f"Skill: {self.skill}, Név: {self.enemy_name}, HP: {self.hp}, Karakter: {self.emo_e}, Pozíció: {self.enemy_poz}")
 