#!/usr/bin/python3
"""
    Classe abstraite représentant une forme géométrique.
    Classe représentant un cercle.
    Classe représentant un rectangle.
    """


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.

    Cette classe définit l'interface commune
    que toutes les formes doivent implémenter.
    """

    @abstractmethod
    def area(self):
        """
        Calcule la surface de la forme.
        Doit être implémentée par les sous-classes.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calcule le périmètre de la forme.
        Doit être implémentée par les sous-classes.
        """
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.

    Attributs :
        radius (float) : le rayon du cercle.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.

        Paramètre :
            radius (float) : le rayon du cercle.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Retourne la surface du cercle.
        Formule : π x r²
        """
        return pi * (self.radius * self.radius)

    def perimeter(self):
        """
        Retourne le périmètre (circonférence) du cercle.
        Formule : 2 x π x r
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle.

    Attributs :
        width (float) : la largeur du rectangle.
        height (float) : la hauteur du rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Paramètres :
            width (float) : la largeur du rectangle.
            height (float) : la hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Retourne la surface du rectangle.
        Formule : largeur x hauteur
        """
        return self.width * self.height

    def perimeter(self):
        """
        Retourne le périmètre du rectangle.
        Formule : 2 x (largeur + hauteur)
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Affiche les informations d'une forme (surface et périmètre).

    Paramètre :
        shape (Shape) : une instance d'une sous-classe de Shape
        (comme Circle ou Rectangle).
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
