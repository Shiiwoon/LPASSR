#!/bin/bash

read -p "Saisissez la borne supérieure [défaut : 100] : " borne_sup
if [[ -z $borne_sup ]]
then
	borne_sup=100
fi
echo $borne_sup

random_num=$((RANDOM%$borne_sup+1))
echo $random_num

read -p "Saisissez un nombre entre 1 et $borne_sup : " nb_entre

while [ $random_num != $nb_entre ]
do
	if [ $random_num -gt $nb_entre ]; then
		echo "Le nombre mystère est plus grand que $nb_entre"
	elif [ $random_num -lt $nb_entre  ]; then
		echo "Le nombre mystère est plus petit que $nb_entre"
	fi
	read -p "Saisissez un nombre entre 1 et $borne_sup : " nb_entre
done
echo "Bravo, le nombre mystère était $random_num !!"
