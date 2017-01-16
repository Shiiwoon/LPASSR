#!/usr/bin/env python3
# coding: utf-8

####################################################################################################################
## Auteurs : Jorane Congio; Fabrice Edgard
## Date : 14/12/2016
## Titre : Ex3 Fichiers
## Consigne : Demander à l'utilisateur  d'entrer un chemin vers un répertoire, un mot et un rapport
## puis écrire dans le rapport tous les mots commençants par le mot donné à partir du dossier entré par l'utilisateur
## Bonus : Compatibilité Linux / Windows / MacOS + Parcours des sous répertoires
####################################################################################################################


import os
import os
from os.path import join
import datetime


def find_string_in_files(word, path, rapport):
	# Entrée : le mot à chercher, le chemin du dossier et le rapport

	# On utilise un boucle for pour parcourir l'arborescence -> os.walk
	for root, dirs, files in os.walk(path):
		print("searching", root)
		# try pour éviter les UnicodeDecodeError et PermissionError rencontrées
		try:
			# On parcourt tous les fichiers
			for fi in files:
				current_path = root + os.sep + fi
				current_file = open(current_path, 'r')

				# On définit une liste qui contiendra les éventuelles lignes trouvées
				list_contenu = []

				line_count = 1 # Pour savoir à quelle ligne du fichier on est
				# On lit chaque ligne du fichier pour savoir si elle commence par ce qu'on cherche
				for ligne in current_file:
					# Si la ligne est ok, on la met dans la liste
					if ligne.startswith(word):
						list_contenu.append("ligne " + str(line_count) + " : " + ligne)
					line_count += 1
				current_file.close()

				# Si la liste n'est pas vide, on l'écrit dans le rapport
				if list_contenu :
					rapport.write(current_path + "\n")
					for l in list_contenu:
						rapport.write(l)
					rapport.write("\n")
					del list_contenu[:]
		except:
			print("Il y a un problème dans ce fichier : ", current_path)
			pass

# Programme principal
if __name__ == '__main__':
	# Variables utilisees dans le programme
	today = datetime.date.today().strftime('%d-%m-%Y')

	# On demande a l'utilisateur le chemin du dossier, le mot a chercher et le nom du rapport
	directory_path = str(input("Chemin du dossier : "))
	directory_name = os.path.basename(directory_path)

	word = str(input("Chercher les lignes commençant par : "))
	rapport_name = str(input("Nom du rapport : "))
	rapport = open(rapport_name, 'w')
	
	# On ecrit dans le rapport les infos
	rapport.write("----------------------------------------------------------------------\n")
	rapport.write("Date : " + today + "\n")
	rapport.write("Dossier : " + directory_path + "\n")
	rapport.write("----------------------------------------------------------------------\n\n")
	
	# On appelle la fonction qui va parcourir toute l'arborescence à partir du dossier donné par l'utilisateur
	find_string_in_files(word, directory_path, rapport)
