#!/usr/bin/env python3
# coding: utf-8

#####################################################################################################################
## Auteur : Jorane Congio
## Date : 11/01/2017
## Titre : Dichoplay v4
## Consigne : afficher un dictionnaire trié par valeur

def print_sorted_dico(dico):
	# Afficher du plus grand au plus petit
	for key in sorted(dico, key=lambda k : len(dico[k]), reverse=True):
		print(key, ":", dico[key])

dico_test = {"aaaa" : "Cle." ,"a" : "Une cle super longue pour faire un test de si ça fonctionne !", "aaaaaaaaaaaaaaaaaa" : "Et une moins longue"}
dico_meubles = {"Table" : "Meuble composé d'un plateau horizontal reposant sur un ou plusieurs pieds ou supports. Servant notamment pour les repas", "Commode" : "Meuble à hauteur d'appui garni, le plus souvent, de tiroirs", \
"Fauteuil" : "Siège à dossier et à bras pour une personne", "Chaise" : "Siège à dossier, sans bras"}
dico_meubles_2 = {"Table" : "Meuble composé d'un plateur horizontal reposant sur un ou plusieurs pieds ou supports, sert notamment pour les repas", "Commode" : "Meuble à hauteur"}
dico_test_2 = {"a" : "1234", "b" : "1", "c" : "1234567"}
print_sorted_dico(dico_test)
print_sorted_dico(dico_meubles)
print_sorted_dico(dico_test_2)
print_sorted_dico(dico_meubles_2)
