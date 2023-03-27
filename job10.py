class Voiture:
    def __init__(self, marque, modèle, année, kilometrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def SetMarque(self, marque):
        self.__marque = marque
    def SetModele(self, modèle):
        self.__modèle = modèle
    def SetAnnée(self, année):
        self.__année = année
    def SetKilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    def SetEn_marche(self, en_marche):
        self.__en_marche = en_marche
    def SetReservoir(self, reservoir):
        self.__reservoir = reservoir
    

    def GetMarque(self):
        return(self.__marque)
    def GetModele(self):
        return(self.__modèle)
    def GetAnnée(self):
        return(self.__année)
    def GetKilometrage(self):
        return(self.__kilometrage)
    def GetEn_marche(self):
        return(self.__en_marche)
    def GetReservoir(self):
        return(self.__reservoir)

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
    def arreter(self):
        self.__en_marche = False
    def __verifier_plein(self):
        return(self.__reservoir)

voiture1 = Voiture('Toyota', 'corola', 1700, 50)
print(voiture1.GetMarque(), voiture1.GetModele(), voiture1.GetAnnée(), voiture1.GetKilometrage())
voiture1.SetMarque('Citroen')
voiture1.SetModele('C4')
voiture1.SetAnnée(2131)
voiture1.SetKilometrage(4200)
print(voiture1.GetMarque(), voiture1.GetModele(), voiture1.GetAnnée(), voiture1.GetKilometrage())
print(voiture1.GetEn_marche())
voiture1.demarrer()
print(voiture1.GetEn_marche())
voiture1.arreter()
print(voiture1.GetEn_marche())
print(voiture1.GetReservoir())
voiture1.SetReservoir(0)
print(voiture1.GetReservoir())
print(voiture1.GetEn_marche())