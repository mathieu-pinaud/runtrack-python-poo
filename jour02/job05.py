import math

class Forme:
    def __init__(self):
        pass
    def aire(self):
        return(0)

class Cercle(Forme):
    def __init__(self, r):
        Forme.__init__(self)
        self.__radius =  r

    def GetRadius(self):
        return(self.__radius)
    def SetRadius(self, r):
        self.__radius = r
    def aire(self):
        return(math.pi * (self.__radius * self.__radius))


class Rectangle(Forme):
    def __init__(self, l , L):
        Forme.__init__(self)
        self.__longueur = l
        self.__largeur = L
    
    def GetLongueur(self):
        return(self.__longueur)
    def GetLargeur(self):
        return(self.__largeur)
    
    def SetLongueur(self, l):
        self.__longueur = l
    def SetLargeur(self, L):
        self.__largeur= L
    
    def périmètre(self):
        return(self.__longueur + self.__largeur * 2)
    def surface(self):
        return(self.__longueur * self.__largeur)
    def aire(self):
        return(self.surface())
    
r1 = Rectangle(4, 5)
print(r1.aire())
c1 = Cercle(1)
print(c1.aire())