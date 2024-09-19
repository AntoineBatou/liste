import logging
from pathlib import Path
import json

from constants import CUR_DIR, DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        self.element = element
        if not isinstance(self.element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaines de caractères !!")
        if element in self:
            LOGGER.error(f"{self.element} est déjà dans la liste !")
            return False

        self.append(element)
        return True

    def supr(self, element):
        self.element = element
        if not element in self:
            LOGGER.error(f"{self.element} n'est pas dans la liste !")
            return False
        
        self.remove(element)
        return True
    
    def afficher(self):
        print(f"Ma liste de {self.nom} contient :")
        for i in self:
            print(f"- {i}")
    
    def sauvegarder(self):
        chemin = DATA_DIR / f"{self.nom}.json"
        chemin.parent.mkdir(parents=True, exist_ok=True)
        with open(chemin, "w") as f:
            json.dump(self, f)
            return True

    
if __name__ == "__main__":
    print("Hello")
    liste = Liste("Courses")
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.ajouter("Bananes")
    liste.ajouter("Petit Pois")
    liste.supr("Poires")
    liste.afficher()
    liste.sauvegarder()