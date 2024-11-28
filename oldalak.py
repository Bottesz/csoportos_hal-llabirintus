from Character import Player

def oldalak(oldal_szam,player,hp):
        
        if oldal_szam == 1:
            print("1. oldal:\nEgy kőasztalhoz érsz. Mit teszel?")
            print("1) Kinyitod a saját neveddel ellátott dobozt (270. oldal).")
            print("2) Továbbmész észak felé (66. oldal).")
            return [(270, "Kinyitod a dobozt"), (66, "Továbbmész észak felé")]

        elif oldal_szam == 270:
            print("270. oldal:\nTalálsz két aranypénzt és egy tanácsot.")
<<<<<<< HEAD
            player(2)
=======
            self.player.adjust_gold(2)
>>>>>>> 413af38275a71dcf762a926c6e9f19f6c42680ab
            return [(66, "Továbbmész észak felé")]

        elif oldal_szam == 66:
            print("66. oldal:\nElágazáshoz érsz.")
            print("1) Nyugat felé mész (293. oldal).")
            print("2) Kelet felé mész (56. oldal).")
            return [(293, "Nyugat felé"), (56, "Kelet felé")]

        elif oldal_szam == 56:
            print("56. oldal:\nEgy akadállyal találkozol.")
            print("1) Átmászol rajta (373. oldal).")
            print("2) Kettévágod karddal (215. oldal).")
            return [(373, "Átmászol"), (215, "Kettévágod karddal")]

        elif oldal_szam == 373:
            print("373. oldal:\nÁtvergődsz az akadályon.")
            return [(56, "Kelet felé folytatod az utat.")]

        elif oldal_szam == 215:
            print("215. oldal:\nMegsebez a spóra, életerőd csökken.")
<<<<<<< HEAD
            player.set_hp(+2)
=======
            self.player.adjust_health(-2)
>>>>>>> 413af38275a71dcf762a926c6e9f19f6c42680ab
            return [(56, "Kelet felé folytatod az utat.")]

        elif oldal_szam == 293:
            print("293. oldal:\nÚjabb elágazás.")
            print("1) Tovább mész nyugatra (137. oldal).")
            print("2) Észak felé fordulsz (387. oldal).")
            return [(137, "Nyugatra"), (387, "Észak felé")]

        elif oldal_szam == 387:
            print("387. oldal:\nEgy Barlangi Emberrel találkozol. Harcolnod kell!")
            (Player("Barlangi Ember", 7, 7, 0))
            return []

        else:
            print("Oldal nem elérhető.")
            return []