import json
import os
import datetime

DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")


def enregistrer_tresorerie_historique(
    tresorerie, fichier="data/tresorerie_history.json"
):
    historique = []
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            try:
                historique = json.load(f)
            except:
                historique = []
    historique.append(
        {"timestamp": datetime.datetime.now().isoformat(), "tresorerie": tresorerie}
    )
    with open(fichier, "w") as f:
        json.dump(historique, f)


def lire_tresorerie_historique(fichier="data/tresorerie_history.json"):
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []


def ouvrir_inventaire(path=INVENTAIRE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        inventaire_defaut = {
            "bananes": 120,
            "mangues": 85,
            "ananas": 45,
            "noix de coco": 60,
            "papayes": 30,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(inventaire_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(inventaire, path=INVENTAIRE_PATH):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ouvrir_tresorerie(path=TRESORERIE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(1000.0, fichier)
    with open(path, "r", encoding="utf-8") as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_tresorerie(tresorerie, path=TRESORERIE_PATH):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)


def ouvrir_prix(path=PRIX_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        prix_defaut = {
            "bananes": 2,
            "mangues": 7,
            "ananas": 5,
            "noix de coco": 4,
            "papayes": 3,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(prix_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, "r", encoding="utf-8") as fichier:
        prix = json.load(fichier)
    return prix


def afficher_tresorerie(tresorerie):
    print(f"\n 💰 Trésorerie actuelle : {tresorerie:.2f} $")


def afficher_inventaire(inventaire):
    print("\n inventaire actuel de la plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")
    print("\n Fin de l'inventaire")


def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    message = {'status': 'succes', 'text': f"\nRécolté {quantite} {fruit} supplémentaires !"}
    print(f"\n ✅ Récolté {quantite} {fruit} supplémentaire(s) !")
    return(inventaire, message)


def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0) * quantite
        enregistrer_tresorerie_historique(tresorerie)
        print(f"\n 💰 Vendu {quantite} {fruit} au prix {prix.get(fruit, 0)} $!")
        message = {'status': 'succes', 'text': f"\nVendu {quantite} {fruit} !"}
        return (inventaire, tresorerie, message)
    else:
        print(
            f"\n 🚨 quantite insuffisante de {fruit} pour vendre {quantite} unité(s) !"
        )
        message = {'status': 'error', 'text': f"\nPas assez de {fruit} pour en vendre {quantite}."}
        return (inventaire, tresorerie, message)


def vendre_tout(inventaire, tresorerie, prix):
    print("\n Vente de tout l'inventaire : \n")
    for fruit, quantite in list(inventaire.items()):
        if quantite > 0:
            revenu = quantite * prix(fruit, 0)
            tresorerie += revenu
            print(
                f" - {fruit.capitalize()} : vendu {quantite} unités pour {revenu:.2f}"
            )
            inventaire[fruit] = 0
    enregistrer_tresorerie_historique(tresorerie)
    return inventaire, tresorerie


def valeur_stock(inventaire, prix):
    valeur = {}
    valeur_stock = 0.0
    for fruit in inventaire:
        quantite = inventaire[fruit]
        prix_unitaire = prix.get(fruit, 0)
        valeur[fruit] = quantite * prix_unitaire
        valeur_stock += valeur[fruit]
    return valeur, valeur_stock


def dollar_to_euro(tresorerie):
    taux_de_change = 0.86
    tresorerie_euro = tresorerie * taux_de_change
    return tresorerie_euro


if __name__ == "__main__":

    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()

    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)

    inventaire = recolter(inventaire, "bananes", 10)
    inventaire = recolter(inventaire, "noix de coco", 10)

    inventaire, tresorerie = vendre(inventaire, "noix de coco", 15, tresorerie, prix)

    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)

    ecrire_tresorerie(tresorerie)
    ecrire_inventaire(inventaire)
