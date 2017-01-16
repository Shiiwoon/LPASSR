# TP SSL

#### Générer un certificat autosigné :
```bash
# On génère la clé privée
openssl genrsa -out priv_key.pem 2048

# Puis on l'utilise pour créer notre certificat autosigné
openssl req -new -x509 -days 365 -key priv_key.pem -out ca_cert.pem
```

#### Installer le certificat dans Firefox : 
* Options > Advanced > Certificates: View Certificates > Import...

#### Générer une demande de certificat sur le serveur Web

```bash

```

#### Signer la demande de certificat sur le serveur
 ```bash

```

#### Mise en place de HTTPS

Installer Apache :
```bash
# apt-get install apache2
```

Accéder au site web en interne :
* modifier /etc/hosts
* ajouter une entrée IP_SERVER_WEB NOM_DOMAINE
 
(Le nom de domaine a été renseigné au moment de la création du certificat)

Activer le module SSL/TLS de Apache :
```bash
# a2enmod ssl
# service apache2 force-reload
```

#### Faire communiquer les VM tout en ayant internet
Les mettre en réseau NAT tout en vérifiant qu'elles aient des adresses MAC différentes. Si tout se passe bien, elles devraient obtenir des IP différentes dans le même réseau et pouvoir se ping entre elles. Sinon, good luck  ;)