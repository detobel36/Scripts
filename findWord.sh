#!/bin/bash

echo -e "\e[37mCe script vous permet de trouver un mot dans tous les fichiers d'un dossier"

echo -e "\e[97m"
currentfile=$PWD
read -p "Dossier/fichier à analyser [$currentfile]: " filename

if [ "$filename" == "" ] ; then
    filename=$currentfile
fi


if [[ -d $filename ]] ; then
    read -p "Quel mot voulez-vous trouver: " word

    # filename=$(echo $filename | sed 's/ /\\ /g')

    fichier=""

    grep -nri "$word" `"${filename}"/*` | while read -r line ; do
        IFS=':' read -r -a array <<< "$line"

        newFichier=${array[0]}
        if [ "$fichier" != "$newFichier" ] ; then
            fichier=$newFichier
            echo -e "\e[36m$fichier"
        fi

        echo -e "\e[31m${array[1]}\e[37m. \e[93m${array[2]}"
    done
else
    echo "Ce dossier/fichier n'existe pas"
fi