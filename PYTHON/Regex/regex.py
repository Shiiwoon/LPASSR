import re

def afficheTitre(titre):
	print('*' * len(titre)
	print(titre)
	print('*' * len(titre)

def afficheLignes(regex, lignes):
	for l in lignes:
		if re.search(regex, l):
			print l
"""
	Regex utiles :
		\d : un chiffre
		\D : tout sauf un chiffre
		\s : espace, tab, \n
		\S : tout sauf ...
		\w : mot -> suite de caractères délimités par espace, tab ou \n
	Wildcards :
		- . : n'importe quel caractère
		- ^ : commence par
		- $ : finit par
		- ? : au plus une fois
		- + : au moins une fois
		- * : 0, 1 ou plusieurs fois
"""

words = [ ".pouet",\
		  "...a...",\
		  "Pouet",\
		  "Ah",\
		  "Wesh",\
		  "Test",\
		  "P234",\
		  "1T3",\
		  "[pouet]",\
		  "[pouet",\
		  "pouet]",
		  "ZeaaaaaaaaaaaTaa",\
		  "abracadabra",\
		  "abracadabraa",\
		  "!pouet",\
		  "!@",\
		  "a 0423af a",\
		  "0434af", "04PO"]

for w in words:
	print("---------------------------------------")
	"""if re.search('ue', w):
		print(w)
	if re.search('^W', w):
		print(w)
	if re.search('h$', w):
		print(w)
	if re.search('s.$', w):
		print(w)
	if re.search('s.$|^P', w):
		print(w)
	if re.search('P[ou]u', w):
		print(w)
	if re.search('^[A-Z][0-9]', w):
		print(w)
	if re.search('\d\D\d', w):
		print(w)
	if re.search('o[^i]', w):
		print(w)
	if re.search('o[^i]', w):
		print(w)
	#if re.search('^([^a]*a){5}[^a]*$', w):
	# contient uniquement chiffre ou majuscules
	match = re.search('[^A-Z0-9]', w)
	if not match:
		print(w)
	
	# 1.a : contient des chiffres ou des majuscules
	if re.search('[A-Z0-9]', w):
		print(w)

	# 1.b : contient des points
	if re.search('\.', w):
		print(w)

	# 1.c : contient "..."
	if re.search('(\.){3}', w):
		print(w)
	if re.search('\.\.\.', w):
		print(w)

	# 1.d des nombres hexadécimaux qui ne soient pas collés à d'autres caractères de la ligne
	if re.search('\s[a-f0-9]', w, re.IGNORECASE):
		print(w)
	# 1.e : un mot d'au moins 12 caractères alphanumériques
	if re.search('[a-z0-9]{12}', w, re.IGNORECASE):#pk ok ?
		print(w)
		"""
	# 1.f : exactement 5 lettres 'a'
	if re.search('^([^a]*a){5}[^a]*$', w):
		print(w)
		"""
	# 1.g : '[' ou ']'
	if re.search('\[|\]', w):
		print(w)
		"""
