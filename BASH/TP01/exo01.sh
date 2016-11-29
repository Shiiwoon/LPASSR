#!/bin/bash
stRepertoire="/bin"
stProgramme="/bin/bash"

# 5 plus gros fichiers de chaque variable :
echo -n "Les 5 fichiers les plus gros dans $stRepertoire sont : "
# a : fichiers caches, h : human readable (size : Ko, Mo...), S : sort by size
# head -6 : une ligne en plus pour le "total x" en première ligne
ls -ahS $stRepertoire | head -6 | tr '\n' ' '

# 5 fichiers les plus anciens :
echo -en "\n\nLes 5 fichiers les plus anciens dans $stRepertoire sont : "
ls -tU $stRepertoire | head -6 | tr '\n' ' '

# size of $stProgramme :
echo -en "\n\nLa taille du fichier $stProgramme est : "
du -h $stProgramme | awk '{print $1}'

# Date de modification :
echo -en "\nLa date de modification du fichier $stProgramme est : "
ls -l --time-style=long-iso $stProgramme | awk '{print $6}'
