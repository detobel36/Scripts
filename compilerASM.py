# -*- coding:Utf8 -*-
 
###########################################
# Programme Python type                   #
# Bruxelles, 2015                         #
###########################################
 
##################################
#   =>  Projet: compile.py  <=   #
##################################
 
# Utilisation: python3 compile.py <nom>
# Il ne faut pas mettre le .asm
 
import os
import os.path
import sys
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfilename, askopenfilename

argument = sys.argv;
 
# Calcules des espacements pour un bel affichage
def calcule_espace(string, nbrReference):
    return string + " "*(nbrReference-len(string) -1) + "|"
 
# Si aucun fichier n'a été spécifié
if(len(argument) == 1):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" \
          "| Vous devez rentrer le nom du programme de cette manière: |\n" \
          "| >> python3 compile.py <nom>                              |\n" \
          "| Et ce, sans le .asm                                      |\n" \
          "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
 
# Si l'utilisateur à spécifié l'extention
elif(".asm" in argument[1] or ".cpp" in argument[1]):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" \
          "| Vous ne devez pas rentrer l'extention du programme.    |\n" \
          "| Voici comment utiliser le programme:                   |\n" \
          "| >> python3 compile.py <nom>                            |\n" \
          "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
 
# Si il manque le fichier IO.cpp
elif(not os.path.exists("IO.cpp")):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" \
          "| Vous avez besoin du fichier IO.cpp disponible sur l'uv |\n" \
          "| Lien: http://bit.ly/1MTjYnx                            |\n" \
          "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
 
# Si le fichier spécifié pas l'utilisateur n'existe pas
elif(not os.path.exists(argument[1]+".asm")):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" \
          "| Le fichier que vous désirez lancer n'existe pas. |\n" \
          "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
 
# Si tout est bon, on y va ->
else:
 
    # Initialisation des messages
    str_ligne     = "-=-";
    str_nom       = "| Compilation de " + argument[1] + ".asm";
    str_dossier   = "| Se trouvant dans le dossier: " + sys.path[0];
    str_nasm      = "| Lancement de la commande: nasm -f elf " + argument[1] + \
                    " .asm "
    str_g         = "| Lancement de la commande: g++ IO.cpp " + argument[1] + \
                    " .o -m32 -o exec "
    str_execusion = "| Exécution..."
    # Message d'erreur
    str_erreur_asm    = "| Une erreur c'est produite lors de l'exécution " \
                        "de la commande nasm "
    str_erreur_compil = "| Une erreur c'est produit lors de la compilation"
 
    # Calcule du nombre de caractère
    # On regarde pour tous les messages, si jamais ils sont modifiés...
    nbr_max = max(len(str_nom), len(str_dossier), len(str_nasm), \
                len(str_g), len(str_erreur_asm), len(str_erreur_compil));
 
    # Calcule de la longeur que l'on va utilisé partout
    str_ligne = (str_ligne*((nbr_max//3) + 1))
 
    nbr_caracter = len(str_ligne)
    str_nom = calcule_espace(str_nom, nbr_caracter)
    str_dossier = calcule_espace(str_dossier, nbr_caracter)
    str_nasm = calcule_espace(str_nasm, nbr_caracter)
    str_g = calcule_espace(str_g, nbr_caracter)
    str_execusion = calcule_espace(str_execusion, nbr_caracter)
    str_erreur_asm = calcule_espace(str_erreur_asm, nbr_caracter)
    str_erreur_compil = calcule_espace(str_erreur_compil, nbr_caracter)
 
 
    # Message de démarrage
    print(str(str_ligne) + "\n" + \
          str(str_nom) + "\n" + \
          str(str_dossier))
 
    ##########################
    # Première commande:
    print(str(str_nasm))
    os.system('nasm -f elf ' + argument[1] + '.asm')
 
    if(os.path.exists(argument[1] + ".o")): # Si la première commande fonctionne
 
        ##################
        # Seconde commande
        print(str(str_g))
        os.system('g++ IO.cpp ' + argument[1] + '.o -m32 -o exec')
 
        if(os.path.exists("./exec")):
            print(str(str_execusion))
            os.system('./exec')
        else:
            print(str(str_erreur_compil))
 
    else: # Si le fichier .o n'a pas été créé
        print(str(str_erreur_asm))
 
    print(str(str_ligne))