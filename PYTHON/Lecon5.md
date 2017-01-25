# Leçon 5

### C'est quoi ?

Une liste c'est une suite ordonnée pouvant contenir n'importe quel type de données : des entiers, des flotants, des chaines de caractères, des objets...

### Quand utilise-t-on une liste ?
On peut utiliser une liste pour
- regrouper des valeurs : liste des notes des étudiants, liste des températures sur le dernier mois, etc
- Savoir que les éléments vont être enregistrés dans l'ordre où on les a ajoutés à la liste

### Déclaration

Déclaration à l'initialisation :
```python
list_CPU = ['i7-6700K', 'Xeon-E5506', 'm3-7Y30', 'FX 8300', 'FX 4300'] # liste contenant des noms de CPU
```
Python sait que l'on a déclaré une liste car on a utilisé des crochets pour délimiter les éléments. Ici, on a une liste de chaînes de caractères.

Déclaration sans initialisation :
```python
list_CPU = list()
```

Si on ne sait pas par avance ce que va contenir la liste mais qu'on sait qu'on va l'utiliser, il faut la déclarer sans l'initialiser. Ça peut par exemple être utile pour remplir une liste par rapport à un input de l'utilisateur ou un fichier.

### Manipulations sur les listes

Ajouter un élément :
```python
list_CPU.append('Pentium G3460')
```

Retirer un élément :
```python
list_CPU.remove('i7-6700K')
```

Désigner un élément d'une liste :
Pour désigner un élément, on utilise son indice. Les indice sont numérotés à partir de 0 !
```python
>>> print(list_CPU[0])
Xeon-E5506
```
Attention : Python réattribue les indices dès qu'on fait une modification sur la liste. Ici, on a retiré le premier élément de la liste, le premier élément est donc à présent Xeon-E5506

Dans certaines fonctions propres à l'objet list, on doit utiliser la valeur pour désigner un indice. Par exemple, nous avons écrit list_CPU.remove('i7-6700K') et pas list_CPU.remove(0). Si on l'avait fait, on aurait obtenu cette erreur :
```
ValueError: list.remove(x): x not in list
```
En effet, python pense que l'on souhaite retirer la *valeur* 0, pas l'indice. Il nous indique donc qu'il n'a pas trouvé la valeur 0 dans la liste.
Si on avait écrit list_CPU.remove(i7-6700K), on aurait obtenu cette erreur :
```
NameError : name I7-6700K is not defined
```
Dans le cas présent, python essaie de trouver une *variable* qui porterait le nom i7-6700K.

Pourquoi n'a-t-on pas obtenu la même erreur dans les deux cas ? Il faut bien garder à l'esprit que les chiffres et les caractères sont très différents en programmation.

L'instruction `a = 0` a du sens : on déclare une variable a qui a pour valeur 0. En revanche, l'instruction `b = EXDE` ne veut rien dire : que repréente AEFE ? Une nom de variable ? Une chaine de caractères ? Un nombre hexadécimal ?


## Cas d'utilisation
#### Déclarer et afficher
#### Transformer un fichier en liste
#### Somme des éléments
#### Moyenne des éléments
#### Vérifier si une liste contient un élément
#### Supprimer les doublons
#### Séparer une liste

## Erreurs courantes et leur résolution
1 - Utiliser le mauvais type de délimiteur au moment de la création de la liste : `a = ('a', 'b')`, `a = ['a', 'b']` et `a = {'a', 'b'}` ont une signification très différente.
