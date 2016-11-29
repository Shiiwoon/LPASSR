#!/bin/bash

# Déclaration variables base
isVerbose=false
extension=".save"
arr=()

# Boucler dans les paramètres entrés par l'utilisateur
while [[ $# -gt 0 ]]
do
	case $1 in
	"--verbose"  |  "-v"  )
		isVerbose=true
		;;
	"--extension" | "-e")
		extension=$2	
		shift
		;;
	*)
		if [ -e $1 ]; then # Ne pas ajouter à la liste si ce n'est pas un fichier
			arr+=" "
			arr+=$1 # Si c'est un fichier, ajouter à la liste avec un espace pour séparer les arguments
		else
			echo "Le fichier $1 n'existe pas dans ce répertoire."
		fi
	
	esac
	shift
done

# Parcourir la liste de fichiers et faire les sauvegardes
for file in $arr
do
	
	cp $file ./$file$extension
	if [ $isVerbose = true  ]; then
		echo "Sauvegarde de $file en $file$extension"
	fi
done
