import random

class Player:
    def __init__(self,skill:int=0, hp:int=0, luck:int=0, emo:str="H", poz:int=0):
        self.skill=self.dobas_skill()
        self.hp=self.dobas_hp()
        self.luck=self.dobas_luck()
        self.emo=emo
        self.poz=poz
    
    def dobas_skill(self):
        return random.randint(1,6)+6
    
    def dobas_hp(self):
        return random.randint(1,6)+ random.randint(1,6)+12
    
    def dobas_luck(self):
        return random.randint(1,6)+6
    
    def __str__(self):
        return (f"Skill: {self.skill}, HP: {self.hp}, Luck: {self.luck}, Karakter: {self.emo}, Pozíció: {self.poz}")
    
class Enemy:
    def __init__(self,skill,hp,emo_e:str="E", enemy_poz:int=0):
        self.skill=skill
        self.hp=hp
        self.emo_e=emo_e
        self.enemy_poz=enemy_poz
    def __str__(self):
        return (f"Skill: {self.skill}, HP: {self.hp}, Karakter: {self.emo_e}, Pozíció: {self.enemy_poz}")
