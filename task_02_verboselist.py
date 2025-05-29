#!/usr/bin/python3
"""
verbose_list.py - Module contenant une classe personnalisée `VerboseList`
qui hérite de la classe `list`.

Cette classe redéfinit certaines méthodes de la liste standard pour afficher
des messages à chaque modification de la liste.
Cela permet de suivre visuellement les opérations effectuées sur la liste,
ce qui peut être utile pour le débogage
ou pour des fins pédagogiques.

Classes:
    VerboseList - Liste avec retours verbaux pour append, extend, remove, pop
"""

from abc import ABC, abstractmethod


class VerboseList(list):
    """
    Classe qui hérite de `list` et redéfinit certaines méthodes
    avec des impressions explicites.

    Méthodes redéfinies :
        - append(object) : ajoute un élément à la liste et affiche un message.
        - extend(iterable) : ajoute plusieurs éléments à la liste et
                            affiche un message avec le nombre d’éléments.
        - remove(value) : supprime un élément et affiche un message.
        - pop(index=-1) : supprime et retourne un élément,
                            affiche un message avec l’élément retiré.
    """

    def append(self, object):
        """
        Ajoute un élément à la fin de la liste et
        affiche un message de confirmation.

        Args:
            object: L'objet à ajouter à la liste.
        """
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        """
        Ajoute tous les éléments d’un itérable à la fin de la liste
        et affiche combien d’éléments ont été ajoutés.

        Args:
            iterable: Un objet itérable contenant les éléments à ajouter.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        """
        Supprime la première occurrence de `value` dans la liste et
        affiche un message.

        Args:
            value: L’élément à retirer de la liste.
        """
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        """
        Supprime et retourne l’élément à l’index spécifié
        (dernier par défaut), en affichant un message.

        Args:
            index: L’index de l’élément à retirer. Par défaut,
            le dernier élément.

        Returns:
            L’élément retiré de la liste.
        """
        if index == -1:
            index = len(self) - 1
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
