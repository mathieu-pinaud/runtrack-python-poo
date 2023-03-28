class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__prix =  prix

    def SetMarque(self, marque):
        self.__marque = marque
    def SetModele(self, modèle):
        self.__modèle = modèle
    def SetAnnée(self, année):
        self.__année = année
    def Setprix(self, prix):
        self.__prix = prix
    

    def GetMarque(self):
        return(self.__marque)
    def GetModele(self):
        return(self.__modèle)
    def GetAnnée(self):
        return(self.__année)
    def GetPrix(self):
        return(self.__prix)
    
    def informationsVehicule(self):
        print("Marque =", self.__marque, "\nModele =", self.__modèle, "\nAnnée =", self.__année, "\nPrix =", self.__prix)
    def demarrer(self):
        print('Attention, je roule')

class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        Vehicule.__init__(self, marque, modèle, année, prix)
        self.__portes = 4
    
    def GetPortes(self):
        return(self.__portes)
    def SetPortes(self, p):
        self.__portes = p
    def informationsVehicule(self):
        print("Marque =", self.GetMarque(), "\nModele =", self.GetModele(), "\nAnnée =", self.GetAnnée(), "\nPrix =", self.GetPrix(), "\nNombre de portes =", self.GetPortes())
    def demarrer(self):
        print('Attention, je roule en voiture')

class Moto(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        Vehicule.__init__(self, marque, modèle, année, prix)
        self.__roue = 2
    
    def GetRoue(self):
        return(self.__roue)
    def SetRoue(self, r):
        self.__roue = r
    def informationsVehicule(self):
        print("Marque =", self.GetMarque(), "\nModele =", self.GetModele(), "\nAnnée =", self.GetAnnée(), "\nPrix =", self.GetPrix(), "\nNombre de roues =", self.GetRoue())
    def demarrer(self):
        print('Attention, je roule en moto')


vé1 = Vehicule('citroen', 'C4', 2006, 1999)
vé1.informationsVehicule()
voi1 = Voiture('Audi', 'R5', 2020, 2500)
voi1.informationsVehicule()
m1 = Moto('Tmax', 'volé', 2023, 4000)
m1.informationsVehicule()
vé1.demarrer()
voi1.demarrer()
m1.demarrer()