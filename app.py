import tkinter as tk
from tkinter import ttk
from src.compte import Compte
from src.compteEpargne import CompteEpargne
from src.compteCourant import CompteCourant
import csv
from datetime import datetime

current_date = datetime.now().date()

app = tk.Tk()
app.title("Test gcb")
app.geometry("600x500")

data = []
userInfo = []
# ________________________________________________________


def ChangeTypeCompte():
    if v.get() == "courant":
        tiE.config(state=tk.DISABLED)
        mdE.config(state=tk.NORMAL)
    else:
        mdE.config(state=tk.DISABLED)
        tiE.config(state=tk.NORMAL)

def AjouterUnCompte():
    numero = Compte.numeroDeCompte
    proprietaire = ProE.get()
    soldeInitial = solE.get()
    type = v.get()
    tauxInteret = tiE.get()
    MontantDecouvert = mdE.get()
    if type == "courant":
        compteCourant = CompteCourant(
            numero, proprietaire, soldeInitial, current_date, MontantDecouvert
        )
        tauxInteret = 0
        data.append(
            [numero, proprietaire, soldeInitial, type, tauxInteret, MontantDecouvert]
        )
        print(compteCourant)
    else:
        compteEpargne = CompteEpargne(
            numero, proprietaire, soldeInitial, current_date, tauxInteret
        )
        MontantDecouvert = 0
        data.append(
            [numero, proprietaire, soldeInitial, type, tauxInteret, MontantDecouvert]
        )
        print(compteEpargne)

    fichierloading(data)

    for item in tableau.get_children():
        tableau.delete(item)

    for row in data:
        tableau.insert("", "end", values=row)


def fichierloading(data):
    with open("loadData.csv", "w") as fichier:
        ecrire = csv.writer(fichier, delimiter=";")
        for row in data:
            ecrire.writerow(row)


def fichierOpener():
    with open("loadData.csv", "r") as fichier:
        ouvrire = csv.reader(fichier, delimiter=";")
        for ligne in ouvrire:
            userInfo.append(ligne)


# ________________________________________________

NumeroL = tk.Label(app, text="Numero:")
NumeroL.grid(column=0, row=0)

NumeroE = tk.Entry(app, state=tk.DISABLED)
NumeroE.grid(column=1, row=0)

ProL = tk.Label(app, text="Proprietaire:")
ProL.grid(column=0, row=1, pady=5)

ProE = tk.Entry(app)
ProE.grid(column=1, row=1, pady=5)

solL = tk.Label(app, text="Solde Initial:")
solL.grid(column=0, row=2, pady=5)

solE = tk.Entry(app)
solE.grid(column=1, row=2, pady=5)

currency = tk.Label(app, text="Euro")
currency.grid(column=2, row=2, pady=5)

typeL = tk.Label(app, text="Type:")
typeL.grid(column=0, row=3, pady=5)

v = tk.StringVar(value="courant")
choix1 = tk.Radiobutton(variable=v, value="courant", command=ChangeTypeCompte)
choix2 = tk.Radiobutton(variable=v, value="epargne", command=ChangeTypeCompte)
choix1.config(text="Courant")
choix2.config(text="Epargne")
choix1.grid(column=1, row=3, pady=5)
choix2.grid(column=2, row=3, pady=5)

tiL = tk.Label(app, text="Taux Interet:")
tiL.grid(column=0, row=4, pady=5)

tiE = tk.Entry(app, state=tk.DISABLED)
tiE.grid(column=1, row=4, pady=5)

pc = tk.Label(app, text="%")
pc.grid(column=2, row=4, pady=5)

mdL = tk.Label(app, text="Montant Decouvert:")
mdL.grid(column=0, row=5, pady=5)

mdE = tk.Entry(app)
mdE.grid(column=1, row=5, pady=5)

button = tk.Button(app, text="Creation compte", command=AjouterUnCompte)
button.grid(column=1, row=6, pady=5)

cn = ("1", "2", "3", "4", "5", "6")
headers = (
    "Numero",
    "Proprietaire",
    "Solde Inital",
    "Type",
    "Taux Intreret",
    "M.decouvert",
)

tableau = ttk.Treeview(app, columns=cn, show="headings", height=7)
tableau.grid(column=1, columnspan=6, row=7, pady=5)

for i in range(len(cn)):
    tableau.column(cn[i], width="70", anchor="e")
    tableau.heading(cn[i], text=headers[i])

fichierOpener()

app.mainloop()
