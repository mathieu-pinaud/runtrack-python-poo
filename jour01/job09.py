class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def GetNom(self):
        return(self.__nom)
    def GetPrenom(self):
        return(self.__prenom)
    def GetCredit(self):
        return(self.__credits)
     
    def __studentEval(self):
        if self.__credits >= 90:
            return('Excellent')
        elif self.__credits >= 80:
            return('Très bien')
        elif self.__credits >= 70:
            return('Bien')
        elif self.__credits >= 60:
            return('Passable')
        else:
            return('Insuffisant')

    def studentInfo(self):
        print("Nom =", self.__nom, '\nPrenom =', self.__prenom, "\nId =", self.__numero_etudiant, "\nNiveau =", self.__level)

    def add_credit(self, credit):
        if credit > 0:
            self.__credits += credit


etu1 = Student('Doe', 'Jhon', 145)
etu1.add_credit(10)
etu1.add_credit(10)
etu1.add_credit(10)
print("Le nombre de crédits de", etu1.GetPrenom(), etu1.GetNom(), "est de", etu1.GetCredit(), 'points')
etu1.studentInfo()
