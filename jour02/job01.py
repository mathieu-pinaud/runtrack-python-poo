class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)
    def bonjour(self):
        print('Hello')
    def modifierAge(self, age):
        if age >= 0:
            self.age = age

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
    def allerEnCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print("J'ai", self.age, 'ans')

class Professeur(Personne):
    def __init__(self, matiere):
        Personne.__init__(self)
        self.__matiereEnseignée = matiere
    
    def SetMatiere(self, matiere):
        self.__matiereEnseignée = matiere
    def enseigner(self):
        print('Le cours va commencer')

p1 = Personne()
e1 = Eleve()
e1.afficherAge()