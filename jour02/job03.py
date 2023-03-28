class Rectangle:
    def __init__(self, l , L):
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
    
class Parallélépipède(Rectangle):
    def __init__(self, l, L, h):
        Rectangle.__init__(self, l , L)
        self.__hauteur = h
        
    def GetHauteur(self):
        return(self.__hauteur)
    def SetHauteur(self, h):
        self.__hauteur = h
    
    def volume(self):
        return(self.surface() * self.__hauteur)
    
r1 = Rectangle(2, 3)
r1.SetLongueur(4)
r1.SetLargeur(5)
print(r1.GetLongueur())
print(r1.GetLargeur())
print(r1.périmètre())
print(r1.surface())

p1 = Parallélépipède(4, 5, 2)
p1.SetHauteur(4)
print(p1.GetHauteur())
print(p1.volume())
