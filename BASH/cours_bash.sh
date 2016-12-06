#Pour délimiter un nom de variable, on peut utiliser {} !
#ex : prix="20"
echo "${prix}0 Euro"

# read :
# p : texte d'invite
# s : ne pas afficher saisie user
# n : nb caractères max
# t : limiter le temps de saisie

# Paramètres de position :
# set // Peu utilisé
# Ex : set val1 val2 val3
# set -- pour vider
# Évidemment on ne peut pas utiliser '='

## Test de chaines : 
# Toujours mettre des guillemets, sinon ça fait n'improte quoi quand la chaine est vide :
if [ "$str1" == "$str2"  ]; then
fi

## Nota :
Il existe une variable IFS permettant de définir le délimiteur par défaut

