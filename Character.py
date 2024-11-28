import random

class Player:
    def __init__(self,skill:int=0, hp:int=0, luck:int=0, emo:str="H"):
        self.skill=self.dobas_skill()
        self.hp=self.dobas_hp()
        self.luck=self.dobas_luck()
        self.emo=emo
    
    def dobas_skill(self):
        return random.randint(1,6)+6
    
    def dobas_hp(self):
        return random.randint(1,6)+ random.randint(1,6)+12
    
    def dobas_luck(self):
        return random.randint(1,6)+6
    
    def __str__(self):
        return (f"Skill: {self.skill}, HP: {self.hp}, Luck: {self.luck}")
    
class Energy:
    def __init__(self,skill,hp):
        self.skill=skill
        self.hp=hp

    def __str__(self):
        return (f"Skill: {self.skill}, HP: {self.hp}")
