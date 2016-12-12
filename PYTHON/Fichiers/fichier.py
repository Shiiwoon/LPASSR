#!/usr/bin/env python3
# coding: utf-8

import os
import os
from os.path import join
import datetime

# Variables utilisees dans le programme
date_jour = datetime.date.today().strftime('%d-%m-%Y')

# On demande a l'utilisateur
chemin_dossier = str(input("Chemin du dossier : "))
nom_dossier=os.path.basename(chemin_dossier)
premier_mot = str(input("Chercher les lignes commençant par : "))

nom_rapport = str(input("Nom du rapport : "))
rapport = open(nom_rapport, 'w')

rapport.write("Date : " + date_jour + "\n")
rapport.write("Dossier : " + nom_dossier + "\n")


for root, dirs, files in os.walk(chemin_dossier):
	print("searching", root)
	for fi in files:
		chemin_courant = root + "/" + fi
		fichier_courant = open(chemin_courant, 'r')
		list_contenu = []
		compteur_ligne = 1
		try:
			for ligne in fichier_courant:
				if ligne.startswith(premier_mot):
					list_contenu.append(str(compteur_ligne) + " " + ligne)
				compteur_ligne += 1
			fichier_courant.close()
			if list_contenu :
				rapport.write(fi + "\n")
				for l in list_contenu:
					rapport.write(l)
				del list_contenu[:]
		except UnicodeDecodeError:
			print("Pb encodage dans le fichier ", join(root, fi))
