
from Character import Enemy
from Character import Player

class Jatekter:
    def __init__(self):
        self.player=Player(0,"Warrior",0,0,"🤺",0,0)
        self.Godzilla=Enemy(0,"Monster",0,"🐱‍🐉",1)
        self.lista=["_","_"]
        self.lista[self.player.poz]=self.player.emo
        self.lista[self.Godzilla.poz]=self.Godzilla.emo
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
            self.player.set_pozicio() #lépett a harcos
            self.Godzilla.set_pozicio() #lépett a varázslo
            lista=["_","_","_"]
            self.lista[self.harcos.poz]=self.harcos.emo
            self.lista[self.varazslo.poz]=self.varazslo.emo
            if (self.harcos.poz==self.varazslo.poz):
                self.lista[self.varazslo.poz]="⚔"
                self.harcos.set_hp()
                self.varazslo.set_hp()
            self.kor+=1
            self.kiir()
            input()
