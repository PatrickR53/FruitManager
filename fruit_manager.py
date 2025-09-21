import json
import os

DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")

def ouvrir_inventaire(path=INVENTAIRE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        inventaire_defaut = {
            "bananes" : 120,
            "mangues" : 85,
            "ananas" : 45,
            "noix de coco" : 60,
            "papayes" : 30
        }
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(inventaire_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, 'r', encoding='utf-8') as fichier:
        inventaire = json.load(fichier)
    return inventaire

def ecrire_inventaire(inventaire,path=INVENTAIRE_PATH):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)
        
def ouvrir_tresorerie(path=TRESORERIE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(1000.0, fichier)
    with open(path, 'r', encoding='utf-8') as fichier:
        tresorerie = json.load(fichier)
    return tresorerie

def ecrire_tresorerie(tresorerie,path=TRESORERIE_PATH):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)
        
def ouvrir_prix(path=PRIX_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        prix_defaut = {
            "bananes" : 2,
            "mangues" : 7,
            "ananas" : 5,
            "noix de coco" : 4,
            "papayes": 3
        }
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(prix_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, 'r', encoding='utf-8') as fichier:
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
    print(f"\n ✅ Récolté {quantite} {fruit} supplémentaire(s) !")
    
def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0) * quantite
        print(f"\n 💰 Vendu {quantite} {fruit} au prix {prix.get(fruit, 0)} $!")
        return(inventaire, tresorerie)
    else:
        print(f"\n 🚨 quantite insuffisante de {fruit} pour vendre {quantite} unité(s) !")

def vendre_tout(inventaire, tresorerie, prix):
    print("\n Vente de tout l'inventaire : \n")
    for fruit, quantite in list(inventaire.items()):
        if quantite > 0:
             revenu = quantite * prix(fruit, 0)
             tresorerie += revenu
             print(f" - {fruit.capitalize()} : vendu {quantite} unités pour {revenu:.2f}")
             inventaire[fruit] = 0
    return

if __name__ == "__main__":
    
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)
    
    recolter(inventaire, "bananes", 10)
    recolter(inventaire, "noix de coco", 10)
    
    inventaire, tresorerie = vendre(inventaire, "noix de coco", 15, tresorerie, prix)
    
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)
    
    ecrire_tresorerie(tresorerie)
    ecrire_inventaire(inventaire)
    
    