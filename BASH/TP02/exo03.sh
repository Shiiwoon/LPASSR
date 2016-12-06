#!/bin/bash
# Idée : compter le nombre de fichiers et dossiers
# d'un répertoire donné en paramètre

function list_sub {
# In : nom de répertoire, nb_fichiers, nb_dossiers
# 
# Compte le nombre de fichiers et dossiers dans le répertoire
# Si elle trouve des répertoires, se lance récursivement
# pour compter les sous-répertoires

echo $1
for e in $(ls $1); do
	elem=$(ls $1/$e)
	if [ -f $elem ]; then
		echo "$elem : fichier"
	elif [ -d $elem ]; then
		echo "$elem : répertoire"
	fi
	echo $elem
done
}

# Vérifier si on a un seul paramètre et si le dossier existe
if [ "$#" -ne 1 ] || [ ! -d $1 ]; then
	exit 1
fi

list_sub $1
