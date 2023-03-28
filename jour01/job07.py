class Livre:
    def __init__(self):
        self.__titre = ''
        self.__auteur = ''
        self.__pages = 0
    def SetTitre(self, titre):
        self.__titre = titre
    def SetAuteur(self, auteur):
        self.__auteur = auteur
    def SetPages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print('le nombrs de pages doit etre superieur a 0')
    def GetTitre(self):
        return(self.__titre)
    def GetAuteur(self):
        return(self.__auteur)
    def GetPages(self):
        return(self.__pages)
    

mon_livre = Livre()
mon_livre.SetAuteur('J.R.R Tolkien')
mon_livre.SetTitre('Les deux tours')
mon_livre.SetPages(-6)
mon_livre.SetPages(566)
print(mon_livre.GetTitre, mon_livre.GetAuteur, mon_livre.GetPages)