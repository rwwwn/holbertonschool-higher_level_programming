#!/usr/bin/python3
"""
Ce module illustre l'héritage multiple en Python à travers trois classes :

- 🐠 Fish : un animal aquatique qui peut nager.
- 🐦 Bird : un animal aérien qui peut voler.
- 🐟✈️ FlyingFish : un poisson qui peut aussi voler, combinant les
comportements des deux.

Chaque classe contient une ou plusieurs méthodes avec
des comportements propres.
Le but est de montrer comment Python gère l'héritage multiple
et la redéfinition de méthodes.
"""

class Fish:
    """Classe représentant un poisson."""

    def swim(self):
        """Affiche que le poisson nage."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat du poisson."""
        print("The fish lives in water")


class Bird:
    """Classe représentant un oiseau."""

    def fly(self):
        """Affiche que l'oiseau vole."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant 🐟✈️

    Hérite de Fish et Bird.
    Redéfinit les méthodes pour refléter ses capacités uniques :
    - nager comme un poisson
    - voler comme un oiseau
    - vivre entre deux mondes
    """

    def fly(self):
        """Affiche que le poisson volant plane dans les airs."""
        print("The flying fish is soaring!")

    def swim(self):
        """Affiche que le poisson volant nage."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Affiche l'habitat du poisson volant (eau et ciel)."""
        print("The flying fish lives both in water and the sky!")
