from Character import Enemy
from Character import Player

class Jatekter:
    def __init__(self):
        self.player=Player(0,"Warrior",0,0,"🤺",0,0)
        self.Godzilla=Enemy(0,"Monster",0,"🐱‍🐉",1)
        self.lista=["_","_"]
        self.lista[self.player.poz]=self.player.emo
        self.lista[self.Godzilla.enemy_poz]=self.Godzilla.emo_e
        self.kor=1
        self.kiir()


    def kiir(self):
        print(f"{self.kor}. kör")
        print("*"*15," ","-"*27," "*29," ")
        print(f"* {self.lista[0]:<3} {self.lista[1]:^3} {self.lista[2]:>3} * | A {self.harcos.nev}| A {self.varazslo.nev} életereje: {self.varazslo.hp} | Ügyessége FoxRudy-nak: {self.skill} , Név: {self.Warrior_name} HP: {self.hp}, Luck: {self.luck}, Karakter: {self.emo}, Pozíció: {self.poz} |")
        print("*"*15," ","-"*27," "*29," ")
        print("")



    def jatekmenet(self):
        while(self.player.hp>0 and self.Godzilla.hp> 0):
            self.player.poz() 
            self.Godzilla.enemy_poz() 
            lista=["_","_"]
            self.lista[self.player.poz]=self.player.emo
            self.lista[self.Godzilla.enemy_poz]=self.Godzilla.emo_e
            if (self.player.poz==self.Godzilla.enemy_poz):
                self.lista[self.Godzilla.enemy_poz]="⚔"
                self.player.hp()
                self.Godzilla.hp()
            self.kor+=1
            self.kiir()
            input()
