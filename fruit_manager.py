import json

def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, 'r', encoding='utf-8') as fichier:
        inventaire = json.load(fichier)
    return inventaire

def ecrire_inventaire(inventaire,path="inventaire.json"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)
        
def ouvrir_tresorerie(path="data/tresorerie.txt"):
    with open(path, 'r', encoding='utf-8') as fichier:
        tresorerie = json.load(fichier)
    return tresorerie

def ecrire_tresorerie(tresorerie,path="data/tresorerie.txt"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)
        
def ouvrir_prix(path="data/prix.json"):
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
    
    