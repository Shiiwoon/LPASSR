#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------------------------------
#Auteurs : Jacob Fortunat, Smigly Léveillé
#Date : 27/11/2016
#Titre : TP1 v4 : Le dicho-play
#Jeu avec interface graphique qui consiste à faire deviner un nombre défini au hasard dans un intervalle choisis et 
#avec un degrè de diffulté pouvant être une limite de d'essais possible, une limite de temps ou les deux à la fois
#-----------------------------------------
from tkinter import *
from threading import Timer
from random import randrange

Fenetre = Tk()#fenetre du jeu
jeu_en_cours = BooleanVar(False)
mode_limite_coup = BooleanVar(False)#savoir quand une partie présente une limite de coup
mode_limite_temps = BooleanVar(False)#savoir quand une partie présente une limite de temps
nbsecret_limite = IntVar()#variable affilié aux radiobutton de selection de l'intervalle du nombre pris au hasard
nbsecret = IntVar()#nombre mystère pris au hasard
essais_restant = IntVar()
saisie_proposition = IntVar()#proposition soumise
limite_coup = IntVar()
limite_temps = IntVar()
temps_restant = IntVar()
nb_min_soumis = IntVar()#aide l'utilisateur en déduisant l'intervalle où se situe le nombre mystère grâce aux proposotion
nb_max_soumis = IntVar()


def countdown(): #fonction de compte à rebours 
	temps_restant.set(temps_restant.get() - 1)#décrémentation du temps restant
	label_text_temps_restant.config(text=str(temps_restant.get()) + " seconde(s)") #affichage du temps restant
	try :
		if saisie_proposition.get() == nbsecret.get():#si proposition exacte
				label_result.config(text="Bravo ! chiffre mystère = " + str(nbsecret.get()))
				jeu_en_cours.set(False)
				parameter_unlock()
		elif temps_restant.get() < 1: 
			label_text_temps_restant.config(text = "Fin du jeu")
			label_result.config(text="Echec, chiffre mystère = " + str(nbsecret.get()))
			jeu_en_cours.set(False)
			parameter_unlock()#le jeu est fini, on débloque la configuration des paramètres pour permettre le lancement d'une nouvelle partie
		else:
			chrono = Timer(1.0,countdown)#countdown va être appelé en boucle temps qu'il reste du temps
			chrono.start()
	except:
			chrono = Timer(1.0,countdown)#countdown va être appelé en boucle temps qu'il reste du temps
			chrono.start()
	if mode_limite_coup:#si en plus de la limite de temps, la limite de coups est actif, le chrono doit s'arrêter quand le nombre de coups est épuisé
		if(essais_restant.get() < 0):
			chrono.cancel()#arrêt du chrono	
	

def submitgame(event): #evenement de lancement d'une partie
	if not(jeu_en_cours.get()) :#on ne lance pas de partie si un jeu est en cours
		jeu_en_cours.set(True)
		nbsecret.set(randrange(0, nbsecret_limite.get()))
		nb_min_soumis.set(0)
		nb_max_soumis.set(nbsecret_limite.get())
		label_intervalle.config(text="Entre 0 et " + str(nbsecret_limite.get()))#intervalle où se situe le nombre secret
		label_result.config(text="--------------")#vidé le champ résultat modifié par la précédente partie
		
		try:#mis en place pour éviter un problème lorsque l'on ne met rien dans les entrès coups et temps
			if  limite_temps.get() > 0 : #si une limite de temps a été instauré
				temps_restant.set(limite_temps.get())
				mode_limite_temps.set(True)
				label_text_temps_restant.config(text=str(temps_restant.get()) + " seconde(s)")
				chrono = Timer(1.0,countdown) #le chrono qui attends une sec et appelle la fonction countdown
				chrono.start()
			else :
				label_text_temps_restant.config(text="Pas de limite de temps")
				mode_limite_temps.set(False)
				
			
			if  limite_coup.get() > 0 :#si une limite de coup a été instauré
				essais_restant.set(limite_coup.get())
				mode_limite_coup.set(True)
				label_text_coups_restant.config(text = str(essais_restant.get()) + " coup(s) restant(s)")
			else:
				label_text_coups_restant.config(text="Pas de limite de coups")
				mode_limite_coup.set(False)
			parameter_lock()
		except:
			label_text_temps_restant.config(text="Maintenant jouerez sans rien !")
			label_text_coups_restant.config(text="Vous avez voulu faire le malin")
			SaisieProposition.config(state="normal")
			ButtonPropose.config(state="normal")
		
def parameter_unlock(): #débloque les paramètres pour permettre la création d'une nouvelle partie
		#déblocage des paramètres
		SaisieCoup.config(state="normal")
		SaisieTemps.config(state="normal")
		Rad100.config(state="normal")
		Rad500.config(state="normal")
		Rad1000.config(state="normal")
		ButtonStart.config(state="normal")
		#blocage de la section proposition
		SaisieProposition.config(state="disabled")
		ButtonPropose.config(state="disabled")

def parameter_lock():#bloque les paramètres pour empêcher la création d'une nouvelle partie pendant le jeu
		#blogage des paramètres	
		SaisieCoup.config(state="disabled")
		SaisieTemps.config(state="disabled")
		Rad100.config(state="disabled")
		Rad500.config(state="disabled")
		Rad1000.config(state="disabled")
		ButtonStart.config(state="disabled")
		#déblocage de la section proposition
		SaisieProposition.config(state="normal")
		ButtonPropose.config(state="normal")		

def submitoffer(event):#soumission d'une proposition
	if jeu_en_cours.get() and isinstance(saisie_proposition.get(), int):
		if saisie_proposition.get() == nbsecret.get():#si proposition exacte
			label_result.config(text="Bravo ! chiffre mystère = " + str(nbsecret.get()))
			jeu_en_cours.set(False)
			parameter_unlock()#fin du jeu, on dévérouille les paramètres pour permettre le lancement d'une nouvelle partie
		elif saisie_proposition.get() > nbsecret.get():#si proposition au dessus
			label_result.config(text="MOINS")
			if saisie_proposition.get() < nb_max_soumis.get():#déterminer nb_max_soumis
				nb_max_soumis.set(saisie_proposition.get())
		elif saisie_proposition.get() < nbsecret.get():
			label_result.config(text="PLUS")
			if saisie_proposition.get() > nb_min_soumis.get():#déterminer nb_min_soumis
				nb_min_soumis.set(saisie_proposition.get())
		label_intervalle.config(text="Entre " + str(nb_min_soumis.get()) + " et " + str(nb_max_soumis.get()))
		
		
		if mode_limite_coup.get(): #si limite de coups défini
			essais_restant.set(essais_restant.get() - 1)
			label_text_coups_restant.config(text = str(essais_restant.get()) + " coup(s) restant(s)")#affichage du nombre coups restants
			if(essais_restant.get() == 0):
				if saisie_proposition.get() != nbsecret.get():#nècessaire si jamais le joueur trouve le nombre secret au dernier essais
					label_result.config(text="Echec, chiffre mystère = " + str(nbsecret.get()))
				label_text_coups_restant.config(text = "Fin du jeu")
				jeu_en_cours.set(False)
				parameter_unlock()#fin du jeu, on dévérouille les paramètres pour permettre le lancement d'une nouvelle partie
		


Fenetre.title('Le dicho-play')
Fenetre.resizable(width=False, height=False)#empêcher le redimensionnement de la fenetre du jeu
Fenetre['bg']='grey' #couleur de fond

Panneau_gauche = PanedWindow(Fenetre, orient=VERTICAL)#panneau gauche où sera la frame paramètre
Panneau_gauche.pack(side=LEFT, expand=Y, fill=BOTH, pady=5, padx=5)
Panneau_droite = PanedWindow(Fenetre, orient=VERTICAL)#panneau droite où sera la frame jeu
Panneau_droite.pack(side=RIGHT, expand=Y, fill=BOTH, pady=5, padx=5)

FrameParameter = LabelFrame(Panneau_gauche,borderwidth=2,relief=GROOVE,text="Paramètres",padx=20, pady=5)#frame qui contient les éléments de paramètre
FrameParameter.pack(side=TOP,padx=5,pady=5)

FramePlay = LabelFrame(Panneau_droite,borderwidth=2,relief=GROOVE,text="Jeu",padx=20, pady=5)#frame qui contient les éléments de jeu
FramePlay.pack(side=TOP,padx=5,pady=5)

FrameGameStatus = LabelFrame(Panneau_droite,borderwidth=2,relief=GROOVE,text="Statut",padx=20, pady=5)#frame qui contient les informations sur la partie
FrameGameStatus.pack(side=TOP,padx=5,pady=5)

#bouttons radio de choix de l'intervalle

Rad100 = Radiobutton(FrameParameter ,text = "0 - 100", variable=nbsecret_limite , value= 100)
Rad100.select()
Rad100.pack(side="top")
Rad500 = Radiobutton(FrameParameter ,text = "0 - 500", variable=nbsecret_limite, value= 500)
Rad500.pack(side="top")
Rad1000 = Radiobutton(FrameParameter ,text = "0 - 1000", variable=nbsecret_limite, value= 1000)
Rad1000.pack(side="top")

SaisieCoup = Entry(FrameParameter, textvariable = limite_coup, fg ='red', bg ='white')#entrée du nombre de coups
SaisieCoup.pack(side = TOP, padx = 20, pady = 5)

label_text_coups = Label(FrameParameter, text="Nombre de coups")
label_text_coups.pack()

SaisieTemps = Entry(FrameParameter, textvariable = limite_temps, fg ='red', bg ='white')#entrée du temps limite
SaisieTemps.pack(side = TOP, padx = 20, pady = 5)

label_text_temps = Label(FrameParameter, text="Temps maximum en secondes")
label_text_temps.pack()

label_text_proposition = Label(FramePlay, text="Saisissez la valeur")
label_text_proposition.pack()

SaisieProposition = Entry(FramePlay, textvariable = saisie_proposition, state = "disabled", fg ='red', bg ='white') #entrée de la proposition
SaisieProposition.pack(side = TOP, padx = 20, pady = 5)

ButtonStart = Button(FrameParameter, text ='Démarrer le jeu',) #button lanement jeu
ButtonStart.pack(side = TOP, padx = 20, pady = 5)
ButtonStart.bind('<Button-1>', submitgame)#on bind le click sur le boutton à la fonction subitgame qui lance le jeu

ButtonPropose = Button(FramePlay, text ='Proposer',state = "disabled") #button soumission proposition. Dèsactiver de base pour empêcher les tentatives de proposition quand aucune partie n'est lancé
ButtonPropose.pack(side = TOP, padx = 5, pady = 5)
ButtonPropose.bind('<Button-1>', submitoffer)#on bind le click sur le boutton à la fonction submitoffer qui soumet la proposition

label_text_coups_restant = Label(FrameGameStatus, text="--------------")
label_text_coups_restant.pack()

label_text_temps_restant = Label(FrameGameStatus, text="--------------")
label_text_temps_restant.pack()

label_intervalle = Label(FrameGameStatus, text="--------------")
label_intervalle.pack()

label_result = Label(FrameGameStatus, text="--------------")
label_result.pack()

Fenetre.mainloop()

	




