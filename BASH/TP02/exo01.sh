#!/bin/bash

# On commence par vérifier si le script prend bien un seul paramètre
if [ "$#" -ne 1 ]; then
	exit 0

# On vérifie ensuite si le paramètre existe
elif [ -e $1 ]; then
	if [ -f $1 ]; then # si c'est un fichier simple
		exit 1
	elif [ -d $1 ]; then # si c'est un dossier
		exit 2
	else # Si ce n'est ni l'un ni l'autre
		exit 3
	fi
# Si le paramètre n'existe pas
else
	exit 0
fi
