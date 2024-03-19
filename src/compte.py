class Compte:
    numeroDeCompte = 0
    def __init__(self,numero, proprietaire, solde, dateDouverture) :
        self._numero = numero
        self._proprietaire = proprietaire
        self._solde = solde
        self._dateDouverture = dateDouverture
        Compte.numeroDeCompte += 1


    def __str__(self) -> str:
        return f"le numero de compte :{self._numero}\nle solde de compte :{self._solde}\nla date d'ouverture:{self._dateDouverture}"