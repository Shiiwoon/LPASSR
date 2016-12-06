#!/bin/bash

# Creation du repertoire log
./generation_repertoire_log.sh

# Generation variables programme
date_jour=$(date +%Y%m%d)
liste_fichier=$(ls log/)
nb_error_fichiers=0 # Nb error dans tt fichiers
nb_warning_fichiers=0 # Nb warning dans tt fichiers
nb_fichiers=$(ls -l log/ | grep -v '^total' | wc -l) # Nb fichiers dans log
nb_fichiers_log=0 # Nb de fichiers de log du jour

# Boucle principale
for file in $liste_fichier
do
	# Si nom du fichier commence par la date du jour et se termine par .log
	if [[ $file == $date_jour* ]] && [[ $file == *.log ]]; then
		# Incrémenter nombre fichiers log total
		nb_fichiers_log=$((nb_fichiers_log + 1))

		# Incrémenter nombre d'erreurs total
		nb_error=$(grep ERROR log/$file | wc -l)
		nb_error_fichiers=$((nb_error_fichiers + nb_error))
		
		# Incrémenter nombre de warnings total
		nb_warning=$(grep WARNING log/$file | wc -l)
		nb_warning_fichiers=$((nb_warning_fichiers + nb_warning))
	fi
done

# Affichage des resultats
echo "Nombre de fichiers de log du jour : $nb_fichiers_log"
echo "Nombre de fichiers dans le répertoire : $nb_fichiers"
echo "Nombre d'autres fichiers : $((nb_fichiers - nb_fichiers_log))"
echo "Nombre total d'erreurs : $nb_error_fichiers"
echo "Nombre total d'avertissements : $nb_warning_fichiers"
