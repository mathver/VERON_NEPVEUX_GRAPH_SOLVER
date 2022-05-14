"""Description.

Encode une fonction permettant de passer d'un objet de type Probleme
aux tableaux numpy attendus par scipy.optimize.linprog
"""
import numpy as np
from typing import Any
from dataclasses import dataclass
from .lib_probleme import Probleme


@dataclass
class Tableaux:
    """
    Classe permettant de transformer un objet de classe Probleme en tableau au format numpy.array
    l: np.ndarray
    u: np.ndarray
    Aeq: np.ndarray
    beq: np.ndarray
    c: np.ndarray
    """

    l: np.ndarray
    u: np.ndarray
    Aeq: np.ndarray
    beq: np.ndarray
    c: np.ndarray

    def __post_init__(self):
        if self.l.shape != self.u.shape or self.l.shape != self.c.shape:
            raise ValueError("Incompatibilité de dimensions pour l,u ou c.")
        if self.Aeq.ndim != 2:
            raise ValueError("Aeq doit être de dimension 2.")
        lignes, colonnes = self.Aeq.shape
        if self.l.shape != (colonnes,):
            raise ValueError(
                "Aeq n'a pas le bon nombre de colonnes par rapport à l, u et c."
            )
        if self.beq.shape != (lignes,):
            raise ValueError("Aeq n'a pas le bon nombre de lignes par rapport à beq.")

    def __eq__(self, autre: Any):
        if type(self) != type(autre):
            return False
        if (self.l != autre.l).any():
            return False
        if (self.u != autre.u).any():
            return False
        if (self.Aeq != autre.Aeq).any():
            return False
        if (self.beq != autre.beq).any():
            return False
        if (self.c != autre.c).any():
            return False
        return True


def decision_matrice(depart, arrivee, courant) -> int:
    """
    Fonction retournant un valeur selon la valeur du départ et de l'arrivée
    d'une arrête selon un sommet.

    depart: point de départ d'une arrête
    arrivee: point d'arrivéee d'une arrête
    courant: sommet que l'on veut savoir appartenir à l'arrête

    Exemple :
    >>> decision_matrice("a", "b", "a")
    ... -1

    >>> decision_matrice("a", "b", "b")
    ... 1

    >>> decision_matrice("a", "b", "c")
    ... 0
    """
    if depart == courant:
        return -1
    if arrivee == courant:
        return 1
    return 0


def convertit(probleme: Probleme) -> Tableaux:
    """
    Fonction permettant de convertir un objet de classe Probleme
    en objet de classe Tableaux pris en compte par numpy.

    probleme: objet de classe Probleme

    Exemple :

    >>> essai = Probleme(
    ...    sommets=["a", "b", "c", "E", "S"],
    ...    arretes=[
    ...        ("E", "a", 5),
    ...        ("a", "b", 6),
    ...        ("b", "c", 4),
    ...        ("c", "S", 3)
    ...        ],
    ...    source="E",
    ...    puit="S",
    ...    capacite_sommet=[
    ...        ("a", 6),
    ...        ("b", 2),
    ...        ("c", 8),
    ...        ("E", None),
    ...        ("S", None),
    ...        ]
    ...    )

    >>> convertit(essai)
    ... Tableaux(l=array([0, 0, 0, 0]), u=array([5., 6., 4., 3.]), Aeq=array([
    ...   [ 1, -1,  0,  0],
    ...   [ 0,  1, -1,  0],
    ...   [ 0,  0,  1, -1],
    ...   [ 0,  0,  0,  0],
    ...   [ 0,  0,  0,  0],
    ...   [ 0,  0,  0,  0]]),
    ...   beq=array([0, 0, 0, 0, 0, 0]),
    ...   c=array([-1,  0,  0,  0]))
    """
    return Tableaux(
        l=np.array([0 for _ in probleme.arretes()]),
        u=np.array([capacite for (_, _, capacite) in probleme.arretes()]),
        c=np.array(
            [
                -1 if depart == probleme._source else 0
                for (depart, _, capacite) in probleme.arretes()
            ]
        ),
        beq=np.array([0 for sommet in probleme.sommets_internes()]),
        Aeq=np.array(
            [
                [
                    decision_matrice(depart, arrivee, sommet)
                    for depart, arrivee, capacite in probleme.arretes()
                ]
                for sommet in probleme.sommets_internes()
            ]
        ),
    )
