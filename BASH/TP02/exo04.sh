#!/bin/bash

function tri {
	while [ $i < ${#$1[*]} ]; do
		echo $i
		i++
	done
}

read -p "Saisir un tableau d'entier : " tableau
echo $tableau
#tableau_trie=$(echo ${tableau[*]} | tr ' ' '\n' | sort)
#echo $tableau_trie
tri $tableau
echo "Note minimale : ${tableau[0]}"
