"""Description.

Module contenant les fonctionnalités de résolution d'un problème de flot maximal.
"""
from .lib_probleme import Probleme, points_tampons
from .lib_conversion import convertit
from typing import Any, Union
from scipy.optimize import linprog


class Solution:
    """
    Classe permettant de récupérer un objet lisible et interprétable
     suite à la résolution du problème sous forme de tableau numpy.
    Cette classe est très similaire à la classe Probleme.
    Cette classe découle de la résolution d'un objet de classe Probleme par la fonction resout().

    sommets: liste des sommets présents dans le graphe, l'ordre n'importe pas
    arretes: liste de tuples de deux sommets et d'une contrainte de flux sur l'arrête
    source: sommet étant la source du graphe
    puit: sommet étant le puit du graphe

    Exemple :
    >>> Solution(
    ...     sommets=['a', 'E', 'c', 't0', 'b', 't2', 'S', 't1'],
    ...     arretes=[
    ...         ('t1', 'b', 2.0),
    ...         ('a', 't1', 2.0),
    ...         ('t0', 'a', 2.0),
    ...         ('E', 't0', 2.0),
    ...         ('t2', 'c', 2.0),
    ...         ('b', 't2', 2.0),
    ...         ('c', 'S', 2.0)],
    ...     source='E',
    ...     puit='S')
    """

    def __init__(
        self,
        sommets: list[str],
        arretes: list[tuple[str, str, Union[float, int]]],
        source: str,
        puit: str,
    ):
        self._sommets = sommets
        self._arretes: list[tuple[str, str, float]] = [
            (depart, arrivee, float(flot)) for depart, arrivee, flot in arretes
        ]
        if source not in sommets:
            raise ValueError("La source doit être un sommet.")
        self._source = source
        if puit not in sommets:
            raise ValueError("Le puit doit être un sommet.")
        self._puit = puit

    def __repr__(self) -> str:
        return f"Solution(sommets={repr(self._sommets)}, arretes={repr(self._arretes)}, source={repr(self._source)}, puit={repr(self._puit)})"

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

    def flux_maximal(self):
        """
            Fonction permettant de donner la valeur du flux maximal d'un graphe.

            Exemple :
        >>> essai = Solution(
        ...     sommets=['a', 'E', 'c', 't0', 'b', 't2', 'S', 't1'],
        ...     arretes=[
        ...         ('t1', 'b', 2.0),
        ...         ('a', 't1', 2.0),
        ...         ('t0', 'a', 2.0),
        ...         ('E', 't0', 2.0),
        ...         ('t2', 'c', 2.0),
        ...         ('b', 't2', 2.0),
        ...         ('c', 'S', 2.0)],
        ...     source='E',
        ...     puit='S')

        >>> essai.flux_maximal()
        ... 2.0
        """
        flux_max = 0
        for depart, arrivee, capacite in self._arretes:
            if arrivee == self._puit:
                flux_max += capacite
        return flux_max


def resout(probleme: Probleme) -> Solution:
    """
    Fonction permettant la résolution d'un problème de flux maximal avec contrainte
    sur arrêtes et sommets.

    Cette fonction transforme un objet de classe Probleme en tableau interprétable
    par numpy puis donne en sortie un objet de classe Solution.

    probleme: un objet de classe Probleme

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

    >>> resout(essai)
    ... Solution(
    ...     sommets=['a', 'E', 'c', 't0', 'b', 't2', 'S', 't1'],
    ...     arretes=[
    ...         ('t1', 'b', 2.0),
    ...         ('a', 't1', 2.0),
    ...         ('t0', 'a', 2.0),
    ...         ('E', 't0', 2.0),
    ...         ('t2', 'c', 2.0),
    ...         ('b', 't2', 2.0),
    ...         ('c', 'S', 2.0)],
    ...     source='E',
    ...     puit='S'
    ... )
    """
    probleme = points_tampons(probleme)
    donnees_numeriques = convertit(probleme)
    resultat_numerique = linprog(
        c=donnees_numeriques.c,
        A_eq=donnees_numeriques.Aeq,
        b_eq=donnees_numeriques.beq,
        bounds=[(l, u) for l, u in zip(donnees_numeriques.l, donnees_numeriques.u)],
        method="simplex",
    )
    if not resultat_numerique.success:
        raise ValueError("Pas de solution")
    return Solution(
        sommets=list(probleme.sommets()),
        arretes=[
            (depart, arrivee, flot)
            for ((depart, arrivee, _), flot) in zip(
                probleme.arretes(), resultat_numerique.x
            )
        ],
        source=probleme.source(),
        puit=probleme.puit(),
    )


def contrainte_iterable(probleme: Probleme, sommet: str, max: int):
    """
    Fonction permettant d'étudier par itération le flux passant par un sommet selon
    l'évolution de la valeur de la contrainte de celui-ci.
    Elle transforme ainsi un objet de classe Probleme en liste de valeur correspondant
    à la valeur du flux maximal du graphe selon la valeur
    de la contrainte sur le sommet choisi.

    probleme: un objet de classe Probleme
    sommet: sommet sur lequel on veut étudier l'impact de la valeur de sa contrainte
    max: valeur maximale de la contrainte que l'on veut itérer, commence à 0

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

    >>> contrainte_iterable(essai, "b", 5)
    ... [('a', 6), ('b', 0), ('c', 8), ('E', None), ('S', None)]
    ... [('a', 6), ('b', 1), ('c', 8), ('E', None), ('S', None)]
    ... [('a', 6), ('b', 2), ('c', 8), ('E', None), ('S', None)]
    ... [('a', 6), ('b', 3), ('c', 8), ('E', None), ('S', None)]
    ... [('a', 6), ('b', 4), ('c', 8), ('E', None), ('S', None)]
    ... [('a', 6), ('b', 5), ('c', 8), ('E', None), ('S', None)]
    ... [0.0, 1.0, 2.0, 3.0, 3.0, 3.0]
    """
    sommet = str(sommet)
    list_cap = []
    list_caps = []
    list = []
    mod = ()
    for i in range(0, max + 1):
        for cap in probleme.capacite_sommets():
            if cap[0] != sommet:
                list_cap.append(cap)
            elif cap[0] == sommet:
                mod = (cap[0], i)
                list_cap.append(mod)  # Erreur mypy à ne pas considérer
        graph = Probleme(
            sommets=probleme._sommets,
            capacite_sommet=list_cap,
            arretes=probleme._arretes,
            puit=probleme._puit,
            source=probleme._source,
        )
        sol = resout(graph)
        list.append(sol.flux_maximal())
        list_caps.append(list_cap)
        list_cap = []
    return list, list_caps
