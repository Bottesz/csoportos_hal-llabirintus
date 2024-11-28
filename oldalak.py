from Character import Player

def oldalak(oldal_szam,player):
        
        if oldal_szam == 1:
            print("1. oldal:\nEgy kőasztalhoz érsz. Mit teszel?")
            print("1) Kinyitod a saját neveddel ellátott dobozt (270. oldal).")
            print("2) Továbbmész észak felé (66. oldal).")
<<<<<<< HEAD
            if oldal_szam == 1:
                kerdes:int=int(input("1-es ha ládát nyitsz, 2 es ha továbbmész északra: "))
            return [(270, "Kinyitod a dobozt"), (66, "Továbbmész észak felé")]

=======
            if oldal_szam==1:
                print("Kinyitod a dobozt! Lapozz a 270.oldalra. ")
                return 270
            elif oldal_szam==2:
                print("Továbbmész Észak felé! Lapozz a 66.oldalra")
                return 66
            
>>>>>>> 420d7ea6c1e58b393c466167765b870b3c520954
        elif oldal_szam == 270:
            print("270. oldal:\nTalálsz két aranypénzt és egy tanácsot.")
            player.set_gold(2)
            if oldal_szam==270:
                print("Továbbmész észak felé")
                return 66
            

        elif oldal_szam == 66:
            print("66. oldal:\nElágazáshoz érsz.")
            print("1) Nyugat felé mész (293. oldal).")
            print("2) Kelet felé mész (56. oldal).")
            if oldal_szam==293:
                print("Nyugat felé")
                return 293
            elif oldal_szam==56:
                print( "Kelet felé")
                return 56
            

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
            player.set_hp(+2)
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