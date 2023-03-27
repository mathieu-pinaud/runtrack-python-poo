class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)

gerard = Personne("Menvussa", "Gerard")
saber = Personne("Lipopette", "Saber")
aragorn = Personne("Fils d'Arathorn", 'Aragorn')

gerard.SePresenter()
saber.SePresenter()
aragorn.SePresenter()