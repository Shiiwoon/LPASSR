#!/usr/bin/env python3

user = open("user_input.txt", 'w')
phrase = ""
while phrase != "EOF":
	phrase = str(input())
	if phrase != "EOF" :  # Ne pas ecrire dans le fichier si on est a EOF
		user.write(phrase + '\n')
	else :
		print("\n\nFichier enregistré !\n-----------------------------------------------------")
		user.close()
		user = open("user_input.txt", 'r')
		print("Contenu du fichier : ")
		for line in user:
			print(line)
		
 
