### import du module pathlib et indication du chemin du fichier .JSON

from pathlib import Path
import json

liste = []

chemin = Path("/Users/marc/Documents/python/Mes projets/liste/liste.json")
if not chemin.exists():
    print("n'existe pas")
    with open(chemin, "w") as f:
        json.dump(liste, f)

else:
    with open(chemin, "r") as f:
        liste = json.load(f)

### Liste de choses à faire :

choix_utilisateur = ""

### Boucle True pour demander le choix :

while True:
    choix_utilisateur = input('''Choisissez parmi les 5 options suivantes : 
                              1: Ajouter un élément à la liste
                              2: Retirer un élément de la liste
                              3: Afficher la liste
                              4: Vider la liste
                              5: Sauvegarder & Quitter
                              ------------------
                              --> Votre choix : ''')

#### Choix 1 - Ajouter un élément :
    if choix_utilisateur == "1":
        element = input("Entrez un élément à ajouter à la liste : ")
        if element not in liste:
            liste.append(element)

        else:
            print("L'élement est déjà dans la liste")

### Choix 2  - Supprimer un élement :
    elif choix_utilisateur == "2":
        element_supr = input("Quel élément souhaitez vous supprimer ? ")
        if element_supr in liste:
            liste.remove(element_supr)
        else:
            print("L'élement n'est pas dans la liste")

### Choix 3 - Afficher la liste :
    elif choix_utilisateur == "3":
        if liste == []: 
            print("La liste est vide.")
        else:
            for index, i in enumerate(liste, start=1):
                print(index, i)
                print("-" * 50)

### Choix 4 - Vider la liste :
    if choix_utilisateur == "4":
        liste.clear()
        print("La liste a bien été vidée.")

### Choix 5 - Sauvegarder & Quitter :
    if choix_utilisateur == "5":
        with open(chemin, "w") as f:
            json.dump(liste,f)
        print("A bientôt")
        break

### - Je sauvegarde le contenu de la liste dans un fichier json :

