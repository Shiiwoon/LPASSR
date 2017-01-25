# SÉCURITÉ

Ensemble de mesures qui permettent de se protéger.

-> Antivirus, chiffrement des données, tester vulnérabilité du réseau...

De quoi on doit se protéger ? Comment faire ?

Risques :
Récupérer infos persos (gmail & co)
cookies : penser faire supprimer les cookies par le navigateur automatiquement.
La plupart des logiciels contiennet des failles de sécurité. Les antivirus ont énormément de droits sur le système, donc si hack : personne même droits que l'antivirus (presque tous donc).
Phishing
Social engineering : se faire appeler par quelqu'un, mise en confiance. But : soutirer des informations sur l'entreprise
Les mises à jour qui sont buggées : toujours faire un teste sur quelques cobayes avant de déployer sur tout le parc !

IPS action préventive pour identifier les menaces. Surveille le réseau.

Trouver les infos sur les failles :
site du cert (version US) : chaque semaine, il y a un bulletin qui recense les alertes sur les logiciels.

Sécurité des locaux : très important car à partir du moment où on peut accéder physiquement à l'ordi c'est trop tard. Mot de passe BIOS : il y en a souvent des génériques permettant de bypass celui mis par l'utilisateur, dépend du numéro de série du pc portable / carte mère.

Base SAM : utilisateurs locaux avec leurs mots de passe. Normalement non accessible, il suffit de boot sur une clé linux pour y accéder. mdp : encodé en md5, système ne connait pas le mdp

# Firewall

But : filtrer tout ce qui rentre ou sort du réseau. Ne revient pas à faire des ACL sur un routeur car il faut préciser aussi le sens de retour : on doit donc faire une ACL Web -> ANY -> ANY (port) => faille de sécurité. Le firewall lui sait lire les paquets et répondre tout seul. Il sait aussi reconnaitre les fausses connexions TCP(envoi du paquet pas à la bonne étape) : table de session, donc sait toujours où en sont les connexions.

NAT : masquer une adresse, faire communiquer un réseau avec un autre, cacher un adresse réelle.

Fonctionne souvent via un couple @IP:port. Filtre basique : source | destination | port | action : ACCEPT / DENY

22 : SSH []
25 : [UTP]
53 : DNS [UDP]
80 : HTTP[TCP]
161 : SNMP [TCP]

Soit une boîte toute faite qu'on achète sans savoir comment elle est faite, soit un serveur qu'on installe soit même et qu'on configure.

Généralement 2 interfaces : interne / internet.

Deux types de firewall : transparent ou routé.
Transparant : ne fait que du filtrage. Gatheway : routeur en face. Le firewall ne fait pas de routage, n'est même pas obligé d'avoir une adresse IP. PB que deux interfaces
Par exemple on ne peut pas avoir de DMZ.

Routé : routeur est gatheway. Permet de faire plus de choses, permet d'avoir plus de deux interfaces.

Filtrage : avec ou sans état (stateless / statefull)

On peut aussi filtrer sur l'identité de la personne, pas son adresse IP.

On peut ajouter plein de trucs à un firewall :
	Inspection protocolaire : regarder le protocole en plus du port.
	Resilience réseau
	IPS/IDS
	Anti spam
	antivirus
	passerelle vpn ssl ou ipsec
	remote desktop
	QoS
	Cluster

CheckPoint : société israëlienne, firewall
défaut : conf compilée avant d'être mise sur les boitiers. Du coup obligé de passer par le soft pour faire des modifs.

Diff drop / reject : drop : rejette paquet, ne réponds pas : timeout. Reject : répondre "connexion rejetée"
