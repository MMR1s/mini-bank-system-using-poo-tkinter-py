from .compte import Compte

class CompteCourant(Compte):
    def __init__(self, numero, proprietaire, solde, dateDouverture,MontantDecouvertAutorise):
        super().__init__(numero, proprietaire, solde, dateDouverture)
        self._MontantDecouvertAutorise = MontantDecouvertAutorise

    def __str__(self) -> str:
        return super().__str__()+f'\nle montant Decouvert Autorise {self._MontantDecouvertAutorise}'