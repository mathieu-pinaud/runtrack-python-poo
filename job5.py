class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ''

    def vieillir(self):
        self.age += 1
    def nommer(self, name):
        self.prenom = name

mon_chat = Animal()
print("mon chat a : ", mon_chat.age)
mon_chat.vieillir()
print("mon chat a : ", mon_chat.age)
mon_chat.nommer("Ramsès")
print("mon chat s'appelle", mon_chat.prenom)
