"""Description.

Application ligne de commande pour la librairie de résolution de problème de flux maximal.
"""

from .lib_probleme import Probleme
from .lib_resolution import resout, contrainte_iterable
from rich import print
import typer
import jsonpickle

application = typer.Typer()


@application.command()
def question1():
    exemple1 = Probleme(
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
            ("a", None),
            ("b", None),
            ("c", None),
            ("d", None),
            ("e", None),
            ("f", None),
            ("g", None),
            ("E", None),
            ("S", None),
        ],
    )

    solution1 = resout(exemple1)
    print(
        f"\nLa solution de la question 1 sont les arrêtes suivant :\n{solution1._arretes}\n\nPour une valeur de flux maximal de {solution1.flux_maximal()}\n"
    )


@application.command()
def question2():
    exemple2 = Probleme(
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

    solution2 = resout(exemple2)
    print(
        f"\nLa solution de la question 2 sont les arrêtes suivantes :\n{solution2._arretes}\n\nCela nous donne une valeur de flux maximale de : {solution2.flux_maximal()}\n"
    )


@application.command()
def question3():
    exemple3 = Probleme(
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

    solution3 = contrainte_iterable(exemple3, "d", max=7)
    print(
        f"\nIl fallait ici itérer la valeur de la contrainte de d, on choisit comme valeur ici 7, on obtient :\n"
    )
    for i, j in zip(solution3[0], solution3[1]):
        print(
            f"La valeur de flux maximal est de {i} quand les contraintes des sommets sont :\n{j}\n"
        )
    print(f"Ils semblent donc utile de réfléchir à cette bretelle de détournement.\n")


@application.command()
def exemple(nom_fichier: str):
    exemple = Probleme(
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

    code = jsonpickle.encode(exemple)
    with open(nom_fichier, "w") as fichier:
        fichier.write(code)
    print(
        f"\nLe fichier {nom_fichier} a été enregistré dans le dossier parent avec succès\n"
    )


@application.command()
def resolution(nom_fichier: str):
    with open(nom_fichier, "r") as fichier:
        code = fichier.read()

    donnees = jsonpickle.decode(code)
    solution4 = resout(donnees)
    print(
        f"\nLa solution de votre problème sont les arrêtes :\n{solution4._arretes}\n\nPour une valeur de flux maximal de {solution4.flux_maximal()}\n"
    )


@application.command()
def iteration(nom_fichier: str, sommet: str, max: int):
    with open(nom_fichier, "r") as fichier:
        code = fichier.read()

    donnees = jsonpickle.decode(code)
    solution5 = contrainte_iterable(donnees, sommet, max)
    print(
        f"Lorsque vous itérer la valeur du sommet [red]{sommet} [/red]de 0 à {max}, on obtient :\n"
    )
    for i, j in zip(solution5[0], solution5[1]):
        print(
            f"La valeur de flux maximal est de {i} quand les contraintes des sommets sont :\n{j}\n"
        )


if __name__ == "__main__":
    application()
