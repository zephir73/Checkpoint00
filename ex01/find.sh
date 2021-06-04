#!/bin/sh

ls -d */ -1 >> es.txt ## liste les repertoires avec / en fin de ligne

awk '$1 {print "./"$1}' es.txt >> es2.txt ## ajoute ./ en debut de ligne

sed 's/.$//' es2.txt >> es3.txt ## enleve le / en fin de ligne

sed  '1i\.' es3.txt >> es4.txt ## ajoute le . en debut de fichier

cat es4.txt ## affiche le ficher

rm es*.txt ## efface les fichers temporaire
