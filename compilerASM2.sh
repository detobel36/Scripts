#!/bin/bash
# -*- coding:Utf8 -*-
 
###########################################
# Programme Bash type                     #
# Bruxelles, 2015                         #
###########################################
 
##################################
#   =>  Projet: compile.sh  <=   #
##################################
 
echo "Compilation de fichier assembleur: "
if [ -a IO.cpp ]
then
    echo "Quel est le nom du fichier que vous voulez compiler (sans le .asm)"
    read -p "" -e input
    if [ -a $input.asm ]
    then
        nasm -f elf $input.asm
        if [ -a $input.o ]
        then
            g++ IO.cpp $input.o -m32 -o executable
 
            if [ -a executable ]
            then
                ./executable
            else
                echo "La commande 'g++ IO.cpp" $input".o -m32 -o executable' n'a pas fonctionnnée"
            fi
        else
            echo "La commande 'nasm -f elf" $input".asm' n'a pas fonctionnée "
        fi
 
    else
        echo "Le fichier que vous avez spécifié n'existe pas"
    fi
 
else
    echo "Le fichier IO.cpp est introuvable.  Téléchargez le sur l'uv"
    echo "Lien: http://bit.ly/1MTjYnx"
fi
 
echo "Appuyer la touche <Entrée> pour fermer..."
read touche
echo "Fin de la compilation"
