#!/bin/bash
# Idée : compter le nombre de fichiers et dossiers
# d'un répertoire donné en paramètre

set -u

function list_sub {
# In : nom de répertoire, nb_fichiers, nb_dossiers
# 
# Compte le nombre de fichiers et dossiers dans le répertoire
# Si elle trouve des répertoires, se lance récursivement
# pour compter les sous-répertoires

for elem in $(ls $1); do
	# On réutilise l'exo1
	./exo01.sh $1/$elem
	case $? in
	1)
		nb_fichiers=$((nb_fichiers + 1))
		;;
	2)
		nb_dossiers=$((nb_dossiers + 1))

		# Si on a un dossier, on relance la fonction
		list_sub $1/$elem $nb_fichiers $nb_dossiers
		;;
	esac
done
}

# Vérifier si on a un seul paramètre et si le dossier existe
if [ "$#" -ne 1 ] || [ ! -d $1 ]; then
	exit 1
fi

nb_fichiers=0
nb_dossiers=0
list_sub $1 $nb_fichiers $nb_dossiers
echo "Il y a $nb_dossiers sous-répertoires et $nb_fichiers fichiers dans le répertoire $1"
