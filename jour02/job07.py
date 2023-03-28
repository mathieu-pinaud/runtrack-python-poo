import random

class Carte:
    def __init__(self, valeur, couleur):
        self.__valeur = valeur
        self.__couleur = couleur
    
    def GetValeur(self):
        return(self.__valeur)
    def GetCouleur(self):
        return(self.__couleur)
    def points(self):
        if  1 <= self.__valeur <= 10:
            return(self.__valeur)
        elif 11 <= self.__valeur <=13:
            return(10)
        # else:
        #     i = int(input("Souhaitez vous que l'as prenne une valeur de 1 ou de 11 ? "))
        #     while(i != 1 and i != 11):
        #         i = int(input("Saisie incorrecte:\nSouhaitez vous que l'as prenne une valeur de 1 ou de 11 ? "))
        #     return(i)

class Jeu:
    def __init__(self):
        self.__paquet = self.creer_paquet()
        self.__nb_cartes = 52
    
    def GetPaquet(self):
        print(self.__paquet)
        return(self.__paquet)
    def GetNb_cartes(self):
        return(self.__nb_cartes)
    
    def print_paquet(self):
        for i in self.__paquet:
            print(i.GetValeur(), i.GetCouleur())
    
    def creer_paquet(self):
        l = []
        self.my_liste_fusion(l, self.creer_couleur("coeur"))
        self.my_liste_fusion(l, self.creer_couleur("trefle"))
        self.my_liste_fusion(l, self.creer_couleur("carreau"))
        self.my_liste_fusion(l, self.creer_couleur("pic"))
        return(l)

    def my_liste_fusion(self, l, famille):
        for i in famille:
            l.append(i)
    
    def creer_couleur(self, couleur):
        l = []
        for i in range(1, 14):
            l.append(Carte(i,couleur))
        return(l)
    
    def pioche(self):
        i = random.randint(0, self.__nb_cartes -1)
        self.__nb_cartes -= 1
        carte_piochée = self.__paquet[i]
        self.__paquet.pop(i)
        return(carte_piochée)

class Joueur:
    def __init__(self, paquet):
        self.__mes_cartes = []
        self.__mon_score = 0
        self.stop = False
        self.le_paquet = paquet
    
    def GetMesCartes(self):
        return(self.__mes_cartes)
    def GetScore(self):
        return(self.__mon_score)
    
    def print_main_joueur(self):
        for i in self.__mes_cartes:
            print(i.GetValeur(), i.GetCouleur())

    def pioche(self):
        self.__mes_cartes.append(self.le_paquet.pioche())
        self.__change_score()
        self.__check_stop()

    def __change_score(self):
        score = 0
        for i in self.__mes_cartes:
            score += i.points()
        self.mon_score = score

    def __check_stop(self):
        if self.__mon_score > 21:
            self.stop = True

    def mon_tour(self):
        self.__check_stop()
        if self.stop == False:
            print("Votre score est de", self.mon_score, "Voulez vous continuer a jouer ?")
            if input('tapez O pour continuer a jouer une autre entrée sera considédrée comme un stop') == 'O':
                self.pioche()
            else:
                self.stop = True


class Croupier(Joueur):
    def __init__(self, paquet):
        Joueur.__init__(self, paquet)

    def CroupierTurn(self):
        if self.stop == False:
            self.pioche()
        self.__check_stop()
        
    def __check_stop(self):
        if self.mon_score >= 17:
            self.stop = True

def creer_liste_joueurs(paquet):
    l = []
    stop = int(input('Combien de joueurs vont-ils jouer (minimum 1) ?'))
    i = 0
    while i < stop:
        l.append(Joueur(paquet))
        i += 1
    l.append(Croupier(paquet))
    return(l)

def stop_game(liste_joueurs):
    for i in liste_joueurs:
        if i.stop == False:
            return(False)
    return(True)

def le_jeu(liste_joueurs):
    for i in liste_joueurs:
        i.pioche()
        i.pioche()
    nb_joueurs = len(liste_joueurs) - 1
    while (stop_game(liste_joueurs) == False):
        for i in range(nb_joueurs):
            print("Joueur", i + 1)
            print(type(liste_joueurs[i]))
            liste_joueurs[i].mon_tour()
        liste_joueurs[nb_joueurs].CroupierTurn()
    return(liste_joueurs)
        
paquet = Jeu()
liste_joueurs = creer_liste_joueurs(paquet)
random.seed()
le_jeu(liste_joueurs)
i : Joueur
for i in liste_joueurs:
    i.print_main_joueur()
    print(i.GetScore(), '\n')



# lecroupier = Croupier(paquet)
# ma_Joueur = Joueur(paquet)
# sa_Joueur = Joueur(paquet)
# ma_Joueur.pioche()
# ma_Joueur.pioche()
# ma_Joueur.print_main_joueur()
# ma_Joueur.change_score()
# lecroupier.pioche()
# lecroupier.pioche()
# lecroupier.check_stop(0)
# lecroupier.print_main_joueur()
# paquet.print_paquet()
