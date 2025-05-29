#!/usr/bin/python3
"""
counted_iterator.py - Module contenant la classe CountedIterator.

Ce module définit un itérateur personnalisé qui encapsule un autre itérateur
tout en comptant combien d’éléments ont été consommés à l’aide de la
méthode `__next__()`.

Classes:
    CountedIterator -- Itérateur qui compte le nombre d’éléments itérés
"""


class CountedIterator:
    """
    Classe qui encapsule un itérateur et compte le nombre d’éléments parcourus.

    Attributs :
        iteratorobject (iterator) : l'objet itérable à encapsuler.
        counter (int) : compteur du nombre d’éléments consommés.

    Méthodes :
        __init__(iteratorobject) : initialise l’itérateur et le compteur.
        get_count() : retourne le nombre d’éléments déjà parcourus.
        __next__() : retourne le prochain élément et incrémente le compteur.
    """

    def __init__(self, iteratorobject):
        """
        Initialise un CountedIterator avec un objet itérable.

        Args:
            iteratorobject: Un objet itérable à parcourir.
        """
        self.iteratorobject = iter(iteratorobject)
        self.counter = 0

    def get_count(self):
        """
        Retourne le nombre d’éléments consommés via `__next__`.

        Returns:
            int: Le nombre d’éléments itérés jusqu’à présent.
        """
        return self.counter

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: self
        """
        return self

    def __next__(self):
        """
        Retourne le prochain élément de l’itérateur et incrémente le compteur.

        Returns:
            Tout élément issu de l’itérateur encapsulé.

        Raises:
            StopIteration: Lorsque l’itérateur d’origine est épuisé.
        """
        item = next(self.iteratorobject)
        self.counter += 1
        return item
