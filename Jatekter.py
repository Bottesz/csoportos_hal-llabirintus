from Character import Player
from Character import Enemy
import oldalak

class Jatekter:
    def __init__(self):
        self.player=Player(0,"Warrior",0,0,"🤺",0,0)
        self.Godzilla=Enemy(0,0,"🐱‍🐉",1,"Monster")
        self.lista=["_","_"]
        self.lista[self.player.poz]=self.player.emo
        self.lista[self.Godzilla.enemy_poz]=self.Godzilla.emo_e
        self.kor=1
        self.kiir()


    def kiir(self):
        print(f"{self.kor}. kör")
        print("*"*15," ","-"*27," "*29," ")
        print(f"* {self.lista[0]:<2} {self.lista[1]:^2} * | A {self.player.Warrior_name}, Életereje: {self.player.hp}, Támadóereje: {self.player.skill}, Szerencséje: {self.player.luck}, Arany: {self.player.gold}, Item: {self.player.item} |A {self.Godzilla.enemy_name} Életereje: {self.Godzilla.hp}, Támadóereje: {self.Godzilla.skill}|")
        print("*"*15," ","-"*27," "*29," ")
        print("")



    def jatekmenet(self):
        oldalszam=oldalak.oldalak(1,self.player)
        while(self.player.hp>0 and self.Godzilla.hp> 0):
            self.player.poz
            self.Godzilla.enemy_poz 
            lista=["_","_"]
            self.lista[self.player.poz]=self.player.emo
            self.lista[self.Godzilla.enemy_poz]=self.Godzilla.emo_e
            if (self.player.poz==self.Godzilla.enemy_poz):
                self.lista[self.Godzilla.enemy_poz]="⚔"
                self.player.hp
                self.Godzilla.hp
            self.kor+=1
            self.kiir()
            input()
<<<<<<< HEAD
<<<<<<< HEAD
            oldalak.oldalak(self,self.player)
=======
            oldalak.oldalak(oldalszam,self.player)
>>>>>>> 420d7ea6c1e58b393c466167765b870b3c520954
=======
            
>>>>>>> c54819f92d4e5068f5f87b102169a32db4f3650d
