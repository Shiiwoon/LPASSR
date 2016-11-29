#!/usr/bin/env python3

# ouverture en lecture
fichier = open('list-courses.txt', 'r')

# on parcours le contenu du fichier ligne par ligne
i = 1
for ligne in fichier:
    print(i, " : ", ligne, end="")
    i += 1

# il ne faut pas oublier de fermer le fichier
fichier.close()
