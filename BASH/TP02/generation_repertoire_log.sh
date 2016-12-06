#!/bin/bash

# ----------------------------------------
# O'Daly John - LP
# Correction Tp 02 - Exo 02
# ----------------------------------------

# suppression et création
if [ -e log ]; then
	rm -R ./log
fi
mkdir ./log

# copie des modèles
cp modele1.log ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationA.log
cp modele2.log ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationB.log
cp modele1.log ./log/20120719_ApplicationA.log
cp modele2.log ./log/20120719_ApplicationB.log

# Génération de fichier bidon
touch ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationA.conf
echo "[WARNING] - NO" >> ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationA.conf
echo "[ERROR] - NO" >> ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationA.conf
touch ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationB.conf
echo "[WARNING] - NO" >> ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationB.conf
echo "[ERROR] - NO" >> ./log/`(date '+%Y')``(date '+%m')``(date '+%d')`_ApplicationB.conf
