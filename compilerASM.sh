#!/bin/bash

echo "Compilation de fichier assembleur: "
echo ""
echo "                                  _     _                 "
echo "     /\\                          | |   | |                "
echo "    /  \\   ___ ___  ___ _ __ ___ | |__ | | ___ _   _ _ __ "
echo "   / /\\ \\ / __/ __|/ _ \\ '_ \` _ \\| '_ \\| |/ _ \\ | | | '__|"
echo "  / ____ \\\\__ \\__ \\  __/ | | | | | |_) | |  __/ |_| | |   "
echo " /_/    \\_\\___/___/\\___|_| |_| |_|_.__/|_|\\___|\\__,_|_|   "
echo "                                                          "
echo "                                                          "


echo "Quel est le nom du fichier que vous voulez compiler (sans le .asm)"
read -p "" -e input
nasm -f elf $input.asm
g++ IO.cpp $input.o -m32 -o executable
./executable

echo "Appuyer la touche <Entrée> pour fermer..."
read touche
echo "Fin de la compilation"