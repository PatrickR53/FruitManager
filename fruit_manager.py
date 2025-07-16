inventaire = {
    "bananes" : 120,
    "mangues" : 35,
    "ananas" : 45,
    "noix de coco" : 60,
    "papayes" : 30
}

def afficher_inventaire(inventaire):
    print("inventaire actuel de la plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")
        
def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"\n ✅ Récolté {quantite} {fruit} supplémentaire(s) !")
    
def vendre(inventaire, fruit, quantite):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        print(f"\n 💰 Vendu {quantite} {fruit} !")
    else:
        print(f"\n 🚨 quantite insuffisante de {fruit} pour vendre {quantite} unité(s) !")


if __name__ == "__main__":
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    vendre(inventaire, "noix de coco", 15)
    afficher_inventaire(inventaire)