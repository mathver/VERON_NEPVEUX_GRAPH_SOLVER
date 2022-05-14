"""Description.

Création d'une classe permettant de définir un graphe orientés
avec poids grâce aux valeurs clées du problème.
"""
from typing import Any, Iterator, Union, Optional


class Probleme:
    """
    Classe permettant de représenter un problème de type graphe
    comprenant des contraintes sur les arêtes et sur les sommets de celui-ci.

    sommets: liste des sommets présents dans le graphe, l'ordre n'importe pas
    arretes: liste de tuples de deux sommets et d'une contrainte de flux sur l'arrête
    source: sommet étant la source du graphe
    puit: sommet étant le puit du graphe
    capacite_sommet: liste des sommets et de la capacité correspondante à ce dernier

    Exemple:
    >>> essai = Probleme(
    ...   sommets=["a", "b", "c", "E", "S"],
    ...    arretes=[
    ...        ("E", "a", 5),
    ...        ("a", "b", 6),
    ...        ("b", "c", 4),
    ...        ("c", "S", 3)
    ...    ],
    ...    source="E",
    ...    puit="S",
    ...    capacite_sommet=[
    ...        ("a", 6),
    ...        ("b", 7),
    ...        ("c", 8),
    ...        ("E", None),
    ...        ("S", None),
    ...    ],
    ... )

    >>> essai
    ... Probleme(sommets=['a', 'b', 'c', 'E', 'S'],
    ... capacite_sommet=[('a', 6), ('b', 2), ('c', 8), ('E', None), ('S', None)],
    ... arretes=[('E', 'a', 5.0), ('a', 'b', 6.0), ('b', 'c', 4.0), ('c', 'S', 3.0)],
    ... source='E',
    ... puit='S')
    """

    def __init__(
        self,
        sommets: list[str],
        capacite_sommet: list[tuple[str, Optional[int]]],
        arretes: list[tuple[str, str, Union[float, int]]],
        source: str,
        puit: str,
    ):
        self._sommets = sommets
        self._arretes: list[tuple[str, str, float]] = [
            (depart, arrivee, float(capacite)) for depart, arrivee, capacite in arretes
        ]
        if source not in sommets:
            raise ValueError("La source doit être un sommet.")
        self._source = source
        if puit not in sommets:
            raise ValueError("Le puit doit être un sommet.")
        self._puit = puit

        self._capacite_sommet = capacite_sommet

    def __repr__(self) -> str:
        return f"Probleme(sommets={repr(self._sommets)}, capacite_sommet={repr(self._capacite_sommet)}, arretes={repr(self._arretes)}, source={repr(self._source)}, puit={repr(self._puit)})"

    def __eq__(self, autre: Any) -> bool:
        if type(self) != type(autre):
            return False
        if self._source != autre._source:
            return False
        if self._puit != autre._puit:
            return False
        if sorted(self._sommets) != sorted(autre._sommets):
            return False
        if sorted(self._arretes) != sorted(autre._arretes):
            return False
        return True

    def __iter__(self):
        return self

    def arretes(self) -> Iterator[tuple[str, str, float]]:
        return iter(self._arretes)

    def sommets(self) -> Iterator[str]:
        return iter(self._sommets)

    def arretes_contraintes(self) -> Iterator[tuple[str, str, float]]:
        arretes_contraintes = []
        for ville, contrainte in self._capacite_sommet:
            for depart, arrivee, flux_max in self._arretes:
                if ville == depart and contrainte is not None:
                    arretes_contraintes.append(
                        (depart, arrivee, min(float(contrainte), flux_max))
                    )
                elif ville == depart and contrainte is None:
                    arretes_contraintes.append((depart, arrivee, flux_max))
        return iter(arretes_contraintes)

    def capacite_sommets(self) -> Iterator[tuple[str, Optional[int]]]:
        return iter(self._capacite_sommet)

    def puit(self) -> str:
        return self._puit

    def source(self) -> str:
        return self._source

    def sommets_internes(self) -> Iterator[str]:
        for sommet in self._sommets:
            if sommet != self._source and sommet != self._puit:
                yield sommet


def points_tampons(probleme: Probleme) -> Probleme:
    """
    Fonction prenant en entrée un objet de classe Probleme comprenant
    des capacités de sommets et permettant de transformer ces dernières en
    capacité d'arrêtes pour l'optimisation numérique et de donner en sortie un nouvel
    objet de classe Probleme utilisable.

    probleme: objet de classe problème

    Exemple :
    >>> essai = Probleme(
    ...   sommets=["a", "b", "c", "E", "S"],
    ...    arretes=[
    ...        ("E", "a", 5),
    ...        ("a", "b", 6),
    ...        ("b", "c", 4),
    ...        ("c", "S", 3)
    ...    ],
    ...    source="E",
    ...    puit="S",
    ...    capacite_sommet=[
    ...        ("a", 6),
    ...        ("b", 7),
    ...        ("c", 8),
    ...        ("E", None),
    ...        ("S", None),
    ...    ],
    ... )

    >>> points_tampon(essai)
    ... Probleme(sommets=['t0', 'S', 'c', 't1', 't2', 'b', 'E', 'a'],
    ... capacite_sommet=[('a', 6), ('b', 2), ('c', 8), ('E', None), ('S', None)],
    ... arretes=[('E', 't0', 5.0), ('t2', 'c', 8.0), ('a', 't1', 6.0), ('c', 'S', 3.0),
    ... ('t1', 'b', 2.0), ('t0', 'a', 6.0), ('b', 't2', 4.0)],
    ... source='E',
    ... puit='S')
    """
    arretes_contraintes = []
    sommets_tampons = probleme._sommets
    for sommet, contrainte in probleme._capacite_sommet:
        for depart, arrivee, capacite in probleme._arretes:
            if sommet == arrivee and contrainte is not None:
                arretes_contraintes.append(
                    (
                        depart,
                        f"t{probleme._capacite_sommet.index((sommet,contrainte))}",
                        capacite,
                    )
                )
                arretes_contraintes.append(
                    (
                        f"t{probleme._capacite_sommet.index((sommet,contrainte))}",
                        arrivee,
                        contrainte,
                    )
                )
                sommets_tampons.append(
                    f"t{probleme._capacite_sommet.index((sommet,contrainte))}"
                )
            elif contrainte is None and sommet == arrivee:
                arretes_contraintes.append((depart, arrivee, capacite))
    arretes_contraintes = set(arretes_contraintes)
    # obligation d'utiliser set() sinon bug de dédoublement : ne pas considérer l'erreur de mypy
    sommets_tampons = set(sommets_tampons)
    arretes_contraintes = list(arretes_contraintes)
    sommets_tampons = list(sommets_tampons)
    return Probleme(
        sommets=sommets_tampons,
        arretes=arretes_contraintes,
        capacite_sommet=probleme._capacite_sommet,
        source=probleme._source,
        puit=probleme._puit,
    )
