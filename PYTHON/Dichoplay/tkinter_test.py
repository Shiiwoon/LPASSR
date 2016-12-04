#!/usr/bin/env python3
# coding: utf-8

from tkinter import *
def print_game_status():
	print("pouet")
	TextIndice.config(text="Plus petit !")

def print_rules():
	RuleWindow = Toplevel(MainWindow)
	RuleWindow.wm_title("Règles du jeu")
	RuleLabel = Label(RuleWindow, text='\
	Le but du jeu est de trouver en moins \n \
	de coups possibles le nombre choisi   \n \
	par l\'ordinateur                  ').pack()
	ValButton = Button(RuleWindow, text = 'Compris !', command = RuleWindow.destroy).pack()

def state_config_items(state):
	Rad100.config(state=state)
	Rad200.config(state=state)
	Rad300.config(state=state)
	E1.config(state=state)
	E2.config(state=state)
	E3.config(state=state)
	BeginButton.config(state=state)

def state_game_items(state):
	E4.config(state=state)
	ButTestValue.config(state=state)

def launch_game():
	state_config_items("disable")
	state_game_items("normal")
	TextTour.config(text="Tour 1 sur 12")
###################################################################################################################
# Creation de la fenetre de jeu
MainWindow = Tk()
MainWindow.wm_title("Dichoplay")
MainWindow.minsize(width=700, height=300)

# Creation d'un menu
MenuBar = Menu(MainWindow)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="Règles du jeu", command=print_rules)
MenuBar.add_cascade(label="Help", menu=FileMenu)

MainWindow.config(menu=MenuBar)
###################################################################################################################
# Pannel gauche
LeftPannel = PanedWindow(MainWindow, orient=VERTICAL)
LeftPannel.pack(side=LEFT, expand=Y, fill=BOTH, pady=5, padx=5)

# Creation des frames (contiennent le texte et l'encadrement)
ConfigFrame = LabelFrame(LeftPannel, borderwidth=2, relief=GROOVE, text="Configuration", padx=20, pady=5)
ConfigFrame.pack(side=TOP, padx=5, pady=5)

Text1 = Label(ConfigFrame, text='Choississez l\'intervalle du nombre à trouver : ')
Text1.pack()
# Definition du contenu des frames
Rad100 = Radiobutton(ConfigFrame, text = "0 - 100", variable=10 , value=100)
Rad100.select()
Rad100.pack()
Rad200 = Radiobutton(ConfigFrame, text = "0 - 200", variable=10 , value=200)
Rad200.pack()
Rad300 = Radiobutton(ConfigFrame, text = "0 - 300", variable=10 , value=300)
Rad300.pack()

Text2 = Label(ConfigFrame, text='Options facultatives').pack()

Text3 = Label(ConfigFrame, text='Nombre de coups : ').pack()
E1 = Entry(ConfigFrame, bd =3)
E1.pack()

Text4 = Label(ConfigFrame, text='Temps max en secondes : ').pack()
E2 = Entry(ConfigFrame, bd =3)
E2.pack()

Text5 = Label(ConfigFrame, text='Valeur max du random : ').pack()
E3 = Entry(ConfigFrame, bd =3)
E3.pack()

BeginButton = Button(ConfigFrame, text='Commencer a jouer', command = launch_game)
BeginButton.pack()


###################################################################################################################
## Pannel droit

RightPannel = PanedWindow(MainWindow, orient=VERTICAL)
RightPannel.pack(side=LEFT, expand=Y, fill=BOTH, pady=5, padx=5)

GameFrame = LabelFrame(RightPannel, borderwidth=2, relief=GROOVE, text="Jeu", padx=20, pady=5)
GameFrame.pack(side=TOP, padx=5, pady=5)

TextGame = Label(GameFrame, text='Saisissez une valeur : ').pack()

E4 = Entry(GameFrame, bd=3, state="disable")
E4.pack()

ButTestValue = Button(GameFrame, text = "Soumettre", command = print_game_status, state="disable")
ButTestValue.pack()

TextIndice = Label(GameFrame, text= " ")
TextIndice.pack()

TextTour = Label(GameFrame, text = " ")
TextTour.pack()
# Button
ButQuit = Button(MainWindow, text = 'Quit', command = MainWindow.destroy, bg='#234')
ButQuit.pack(side=BOTTOM)

# Launch evnt
MainWindow.mainloop()
