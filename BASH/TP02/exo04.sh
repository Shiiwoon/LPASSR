#!/bin/bash

## Pour alléger la fonction tri, on fai un fonction qui échange les éléments à côté
function swap {
	tmp=${tableau[$1]}
	tableau[$1]=${tableau[$2]}
	tableau[$2]=$tmp
}

## Trie le tableau selon l'algorithme de tri par sélection
function tri {
	len_tab=${#tableau[@]}
	for ((i=0 ; i < len_tab ; i++)); do
		min=$i
		for ((j = i+1 ; j < len_tab ; j++)); do
			if [ ${tableau[j]} -lt ${tableau[min]} ]; then
				min=$j
			fi
		done
		swap $i $min
	done
}

## Programme principal
echo -n "Saisir un tableau d'entier : "
read -a tableau
tri $tableau
echo "tableau : ${tableau[*]}"
echo "Note minimale : ${tableau[0]}"
echo "Note maximale : ${tableau[-1]}"
