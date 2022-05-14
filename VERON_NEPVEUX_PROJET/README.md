# Projet Supply Chain VERON NEPVEUX
## Résolution problème de flux maximal sur un graphe orienté et lesté

Ce module permet de résoudre des problèmes de flux maximal sur des graphes orientés et 
permet une résolution libre mais répond aussi aux questions plus bas.

## Description 

Ce module contient une librairie `veron_nepveux_projet` avec interaction en ligne de commande. 

Toutes les commandes sont accessibles à partir de :

```sh
python -m veron_nepveux_projet --help
```

### Exemple 

Pour donner un exemple du format des données dans le cas d'une étude libre, il convient d'exécuter la commande suivante :

```sh
python -m veron_nepveux_projet exemple modele.json
```

Le nom du fichier dépend de l'utilisateur.
Le fichier généré est modifiable et permet à l'utilisateur d'importer ses propres données.

### Résolution

Si l'utilisateur veut utiliser ses propres données, il lui suffit d'exécuter la commande suivante :

```sh
python -m veron_nepveux_projet resolution donnees.json
```

Cette commande permet de ressortir la solution du problèmes ainsi que la valeur du flux maximal.

### Itération

Similairement à la commande précédente, celle-ci permet à l'utilisateur d'itérer plusieurs valeurs de contraintes sur l'un des ses sommets via :

```sh
python -m veron_nepveux_projet iteration donnees.json a 5
```

Les arguments correspondent au nom du fichier, au sommet à itérer, et à la valeur max de la contrainte.

## Questions

Pour répondre aux différentes questions, il faut utiliser là encore des lignes de commandes.

### Question 1

La première question était de résoudre le graphe suivant et d'en calculer le flux maximal : 

![reseau](reseau.svg)

Pour la réponse, il faut exécuter la commande :

```sh
python -m veron_nepveux_projet question1
```

### Question 2

La seconde question consistait à ajouter des contraintes dans les villes elles-mêmes, telles que :

| villes | a   | b   | c   | d   | e   | f   | g   |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| débits | 6   | 7   | 8   | 6   | 6   | 5   | 9   |

Pour résoudre ce problème, nous avons décidé d'utiliser des arrêtes tampons.

Pour la réponse, il faut exécuter la commande :

```sh
python -m veron_nepveux_projet question2
```

### Question 3

La troisième question consister à itérer la valeur de la contrainte sur la ville **d** et de vérifier l'utilité d'une bretelle de détournement.

La réponse peut être obtenu via : 

```sh
python -m veron_nepveux_projet question3
```