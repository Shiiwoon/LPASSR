#!/bin/bash
fichier="nom.prenom@iut-mail.fr :"

echo "Afficher extension uniquement :"
echo ${fichier##*.}

echo "Afficher provider (iut-mail.fr) : "
echo ${fichier#*@}

echo "Afficher nom.prenom : "
echo ${fichier%@*}

echo "Remplacer le provider : "
provider=$(echo ${fichier#*@})
echo ${fichier/$provider/a}
