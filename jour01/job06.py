class Rectangle:
    def __init__(self):
        self.__longueur = 10
        self.__largeur = 5

    def SetLargeur(self, L):
        self.__largeur = L
    
    def SetLongueur(self, l):
        self.__longueur = l

    def GetLargeur(self):
        return(self.__largeur)
    
    def GetLongueur(self):
        return(self.__longueur)
    
my_rect = Rectangle()
L = my_rect.GetLargeur()
l = my_rect.GetLongueur()
print(L, l)
my_rect.SetLargeur(42)
my_rect.SetLongueur(21)
L = my_rect.GetLargeur()
l = my_rect.GetLongueur()
print(L, l)