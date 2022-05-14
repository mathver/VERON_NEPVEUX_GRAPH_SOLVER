"""Description.

Tests automatiques de la librairie de resolution.
"""
import pytest
from veron_nepveux_projet.lib_resolution import Solution, resout, contrainte_iterable
from veron_nepveux_projet.lib_probleme import Probleme


def test_init():
    essai = Solution(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4),
            ("S", "C", 1),
            ("A", "P", 2),
            ("A", "B", 3),
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        source="S",
        puit="P",
    )
    assert isinstance(essai, Solution)


def test_init_puit_source():
    with pytest.raises(ValueError):
        Solution(sommets=["A", "B"], arretes=[("A", "B", 1)], source="C", puit="B")
    with pytest.raises(ValueError):
        Solution(sommets=["A", "B"], arretes=[("A", "B", 1)], source="A", puit="D")


def test_repr():
    essai = Solution(sommets=["A", "B"], arretes=[("A", "B", 1)], source="A", puit="B")
    assert (
        repr(essai)
        == """Solution(sommets=['A', 'B'], arretes=[('A', 'B', 1.0)], source='A', puit='B')"""
    )


def test_egalite():
    essai1 = Solution(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4.0),
            ("S", "C", 1.0),
            ("A", "P", 2),
            ("A", "B", 3),
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        source="S",
        puit="P",
    )
    essai2 = Solution(
        sommets=["A", "B", "C", "D", "S", "P"],
        arretes=[
            ("S", "A", 4),
            ("A", "P", 2),
            ("S", "C", 1),
            ("A", "B", 3),
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        source="S",
        puit="P",
    )
    assert essai1 == essai2


def test_resoud_non_contraint():
    entree = Probleme(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4),
            ("S", "C", 1),
            ("A", "P", 2),
            ("A", "B", 3),
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        capacite_sommet=[
            ("A", None),
            ("B", None),
            ("C", None),
            ("D", None),
            ("P", None),
            ("S", None),
        ],
        source="S",
        puit="P",
    )

    attendu = Solution(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4),
            ("S", "C", 1),
            ("A", "P", 2),
            ("A", "B", 2),
            ("B", "P", 2),
            ("C", "B", 0),
            ("C", "D", 1),
            ("D", "P", 1),
        ],
        source="S",
        puit="P",
    )
    assert resout(entree) == attendu


def test_resout_contraint():
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

    attendu = Solution(
        sommets=[
            "c",
            "b",
            "t1",
            "t3",
            "g",
            "a",
            "e",
            "E",
            "t0",
            "t6",
            "S",
            "t2",
            "f",
            "t4",
            "t5",
            "d",
        ],
        arretes=[
            ("t5", "f", 4.0),
            ("b", "t2", 6.0),
            ("t0", "a", 5.0),
            ("E", "t1", 7.0),
            ("f", "S", 4.0),
            ("b", "t3", 1.0),
            ("E", "t0", 5.0),
            ("E", "t4", 4.0),
            ("d", "t6", 0.0),
            ("g", "S", 6.0),
            ("t6", "g", 6.0),
            ("b", "t4", 0.0),
            ("d", "t5", 0.0),
            ("c", "t6", 6.0),
            ("t1", "b", 7.0),
            ("t3", "d", 6.0),
            ("t2", "c", 6.0),
            ("d", "S", 6.0),
            ("a", "t2", 0.0),
            ("e", "t5", 4.0),
            ("a", "t3", 5.0),
            ("t4", "e", 4.0),
        ],
        source="E",
        puit="S",
    )
    assert resout(essai) == attendu


def test_flux_max():
    attendu = 18.0
    solution = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )
    flux_max = solution.flux_maximal()

    assert flux_max == attendu


def test__eq__general():
    attendu = [1, 2]
    solution = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )

    assert solution.__eq__(attendu) is False


def test__eq__source():
    attendu = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="a",
        puit="S",
    )
    solution = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )

    assert solution.__eq__(attendu) is False


def test__eq__puit():
    attendu = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="c",
    )
    solution = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )

    assert solution.__eq__(attendu) is False


def test__eq__sommets():
    attendu = Solution(
        sommets=["a", "b", "y", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )
    solution = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )

    assert solution.__eq__(attendu) is False


def test__eq__arretes():
    attendu = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "g", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )
    solution = Solution(
        sommets=["a", "b", "c", "d", "e", "f", "g", "E", "S"],
        arretes=[
            ("a", "c", 0.0),
            ("a", "d", 5.0),
            ("b", "c", 7.0),
            ("b", "d", 2.0),
            ("b", "e", 0.0),
            ("c", "g", 7.0),
            ("d", "g", 2.0),
            ("d", "S", 4.0),
            ("d", "f", 1.0),
            ("e", "f", 4.0),
            ("f", "S", 5.0),
            ("g", "S", 9.0),
            ("E", "a", 5.0),
            ("E", "b", 9.0),
            ("E", "e", 4.0),
        ],
        source="E",
        puit="S",
    )

    assert solution.__eq__(attendu) is False


def test_contrainte_iterable():
    entree = Probleme(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4),
            ("S", "C", 1),
            ("A", "P", 2),
            ("A", "B", 3),
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        capacite_sommet=[
            ("A", 1),
            ("B", 2),
            ("C", 2),
            ("D", 1),
            ("P", None),
            ("S", None),
        ],
        source="S",
        puit="P",
    )
    attendu = [1.0, 2.0, 3.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    assert attendu == contrainte_iterable(entree, "A", 10)
