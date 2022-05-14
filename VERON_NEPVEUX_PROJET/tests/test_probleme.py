"""Description.

Tests automatiques de la classe Probleme.
"""
import pytest
from veron_nepveux_projet.lib_probleme import Probleme


def test_init():
    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )
    assert isinstance(essai, Probleme)


def test_init_puit_source():
    with pytest.raises(ValueError):
        Probleme(
            sommets=["A", "B"],
            capacite_sommet=[("A", 5), ("B", 5)],
            arretes=[("A", "B", 1)],
            source="C",
            puit="B",
        )
    with pytest.raises(ValueError):
        Probleme(
            sommets=["A", "B"],
            capacite_sommet=[("A", 5), ("B", 5)],
            arretes=[("A", "B", 1)],
            source="A",
            puit="D",
        )


def test_repr():
    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )
    assert (
        repr(essai)
        == "Probleme(sommets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'E', 'S'], capacite_sommet=[('a', 6), ('b', 7), ('c', 8), ('d', 6), ('e', 6), ('f', 5), ('g', 9), ('E', None), ('S', None)], arretes=[('E', 'a', 5.0), ('E', 'b', 10.0), ('E', 'e', 8.0), ('a', 'c', 7.0), ('a', 'd', 10.0), ('b', 'c', 8.0), ('b', 'd', 2.0), ('b', 'e', 1.0), ('c', 'g', 7.0), ('d', 'g', 4.0), ('d', 'S', 6.0), ('d', 'f', 2.0), ('e', 'f', 4.0), ('f', 'S', 6.0), ('g', 'S', 10.0)], source='E', puit='S')"
    )


def test_egalite():
    essai1 = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )
    essai2 = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "b", 10),
            ("E", "a", 5),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )
    assert essai1 == essai2


def test_fonction_arretes():
    attendu = [
        ("E", "a", 5.0),
        ("E", "b", 10.0),
        ("E", "e", 8.0),
        ("a", "c", 7.0),
        ("a", "d", 10.0),
        ("b", "c", 8.0),
        ("b", "d", 2.0),
        ("b", "e", 1.0),
        ("c", "g", 7.0),
        ("d", "g", 4.0),
        ("d", "S", 6.0),
        ("d", "f", 2.0),
        ("e", "f", 4.0),
        ("f", "S", 6.0),
        ("g", "S", 10.0),
    ]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert list(essai.arretes()) == attendu


def test_fonction_sommets():
    attendu = ["a", "b", "c", "d", "e", "f", "g", "E", "S"]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert list(essai.sommets()) == attendu


def test_fonction_capacite_sommets():
    attendu = [
        ("a", 6),
        ("b", 7),
        ("c", 8),
        ("d", 6),
        ("e", 6),
        ("f", 5),
        ("g", 9),
        ("E", None),
        ("S", None),
    ]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert list(essai.capacite_sommets()) == attendu


def test_fonction_puit():
    attendu = ["S"]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert list(essai.puit()) == attendu


def test_fonction_source():
    attendu = ["E"]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert list(essai.source()) == attendu


def test_fonction_sommets_internes():
    attendu = ["a", "b", "c", "d", "e", "f", "g"]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert list(essai.sommets_internes()) == attendu


def test_fonction_arretes_contraintes():
    attendu = [
        ("a", "c", 6.0),
        ("a", "d", 6.0),
        ("b", "c", 7.0),
        ("b", "d", 2.0),
        ("b", "e", 1.0),
        ("c", "g", 7.0),
        ("d", "g", 4.0),
        ("d", "S", 6.0),
        ("d", "f", 2.0),
        ("e", "f", 4.0),
        ("f", "S", 5.0),
        ("g", "S", 9.0),
        ("E", "a", 5.0),
        ("E", "b", 10.0),
        ("E", "e", 8.0),
    ]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert list(essai.arretes_contraintes()) == attendu


def test_fonction__eq__type_general():
    autre = ["a", "b", "c", "d", "e", "f", "g", "E", "S"]

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert essai.__eq__(autre) is False


def test_fonction__eq__source():
    autre = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="a",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert essai.__eq__(autre) is False


def test_fonction__eq__puit():
    autre = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S", "G"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="G",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert essai.__eq__(autre) is False


def test_fonction__eq__sommets():
    autre = Probleme(
        sommets=["a", "b", "y", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert essai.__eq__(autre) is False


def test_fonction__eq__arretes():
    autre = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "z", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )

    assert essai.__eq__(autre) is False


def test__iter__():
    essai = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("E", "a", 5),
            ("E", "b", 10),
            ("E", "e", 8),
            ("a", "c", 7),
            ("a", "d", 10),
            ("b", "c", 8),
            ("b", "d", 2),
            ("b", "e", 1),
            ("c", "g", 7),
            ("d", "g", 4),
            ("d", "S", 6),
            ("d", "f", 2),
            ("e", "f", 4),
            ("f", "S", 6),
            ("g", "S", 10),
        ],
        source="E",
        puit="S",
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
    )
    attendu = Probleme(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        capacite_sommet=[
            ("a", 6),
            ("b", 7),
            ("c", 8),
            ("d", 6),
            ("e", 6),
            ("f", 5),
            ("g", 9),
            ("E", None),
            ("S", None),
        ],
        arretes=[
            ("E", "a", 5.0),
            ("E", "b", 10.0),
            ("E", "e", 8.0),
            ("a", "c", 7.0),
            ("a", "d", 10.0),
            ("b", "c", 8.0),
            ("b", "d", 2.0),
            ("b", "e", 1.0),
            ("c", "g", 7.0),
            ("d", "g", 4.0),
            ("d", "S", 6.0),
            ("d", "f", 2.0),
            ("e", "f", 4.0),
            ("f", "S", 6.0),
            ("g", "S", 10.0),
        ],
        source="E",
        puit="S",
    )
    assert essai == attendu
