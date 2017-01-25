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
Bien comprendre comment on désigne un élément d'une liste ! Si on avait écrit list_CPU.remove(i7-6700K), on aurait obtenu cette erreur :
```python
NameError : name I7-6700K is not defined
```