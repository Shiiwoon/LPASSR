# Mail

## Blabla de base
Moyen de communication asynchrone
A la base : login@machine, puis login@domaine
On peut maintenant utiliser de l'UTF-8 dans les noms d'utilisateurs / machine dans les mails.
Encore beaucoup utilisé dans les entreprises
Aujourd'hui considéré comme étant un outil de travail collaboratif.

Mais pb :
	- Impossible d'indentifier clairement un correspondant
	- Intégrité des messages -> pas moyen de savoir s'il a été modifié avant d'être reçu.
	- Messages peuvent être interceptés sans qu'on en ait connaissance
	- Confidentialité ?
	- Infection : quelqu'un se fait passer pour quelqu'un d'autre, du coup on ne se méfie pas.


## Syntaxe
Pour interpréter adresse : part de la fin, cherche le premier @ et en déduit que c'est le nom de domaine, le reste est le nom
de l'utilisateur. En théorie, on pourrait avoir des '@' dans le nom d'utilisateur.

On peut utiliser des parenthèses pour faire un commentaire.
On peut aussi demander de passer par les serveurs qu'on a choisit.
On peut envoyer des mails chiffrés : passe toujours par Telnet, mais on peut chiffrer Telnet

MIME : contenu multimédia

## Fonctionnement
SMTP : port 25 de base, 465 pour SSMTP
ESMTPS : extented SMTP chiffré


POP3 : default port 110 non chiffré. Il prend le serveur de messagerie et le supprime du serveur de messagerie. À éviter. 
IMAP4 : defaut pourt 143. Les serveurs restent sur le serveur : on peut utiliser plusieurs appareils pour consulter les mails.
Il ne consulte que les entêtes avant de dl le message, contrairement à IMAP. Il faut demander explicitement à dl la pièce
jointe pour qu'il le fasse. On peut aussi créer des dossiers sur le serveur de messagerie.

MUA [Mail User Agent]: logiciel depuis lequel on écrit le mail, parle en SMTP
MTA [Mail Transfert Agent] : lie MUA avec SMTP
MDA [Mail Delivery Agent] : Distribue les mails
MAA [Mail Access Agent] : va chercher les mails sur le stockage
SMTP : serveur de mail qui envoie le message
POP/IMAP : serveur qui récupère le message

SMTP envoie tout en clair, mais on peut ruser. On peut protéger les pièces jointes par mot de passe par exemple, ou tout
simplement utiliser un chiffrement asymétrique. 

## Logiciels
MTA:
	Ceux qu'il faut pas utiliser :
		Sendmail, Qmail
	Les autres :
		Exim, Postfix
	
MDA:
	Ils sont intégrés auw logiciels de messagerie le plus souvent
	Mais il y en a des indépendants : procmail; mailfilter, maildrop, deliver...
	Peuvent intégrer des filtres comme Spamassassin

MAA :
	Cyrus, Dovecot : les plus répendus
	Courrier-impa, uw_imap

MUA : 
	Clients lourds : Evolution, Thunderbird/Icedove, Kmail, Claws, Mail, mutt : command line -> très sécurisé
	Clients légers : Roundclub, Horde, MiniG, SquirrelMail

Filtres à merdes :
	Spamassassin : rechercher des choses dans le contenu du mail. Il peut aussi focntionner par apprentissage via des filtres
	Baysiens.

	Clamv : s'occuper de check les pièces jointes

	amavis : permet de retarder l'arrivée des messages, faire des filtres, les démons de spamassassin et clamv. On peut aussi
	faire des zones de quarantaine

## Messageries instantannées

Jabber
clients : Pidgin, Kopete, Empathy

serveurs : Ejabberd(Erlang) -> standart, openfire(java)-> complet,  prosody(LUA)-> Léger
