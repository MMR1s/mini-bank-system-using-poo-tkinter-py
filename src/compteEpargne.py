from .compte import Compte

class CompteEpargne(Compte):
    def __init__(self, numero, proprietaire, solde, dateDouverture,interet):
        super().__init__(numero, proprietaire, solde, dateDouverture)
        self._interet = interet

    def __str__(self) -> str:
        return super().__str__()+f"\nl'interet :{self._interet}"