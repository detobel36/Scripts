# Script
Voici quelques petits scripts pouvant être utile.

- [findWorld (`bash`)](#findwordsh)
- [compilerASM (`python`)](#compilerasmpy)
- [compilerASM2 (`python`)](#compilerasm2py)
- [compilerASM (`bash`)](#compilerasmsh)

-------------------------------


## findWord.sh
Permet de retrouver un mot dans un dossier.

#### Utilisation
```BASH
./findWord.sh 
Ce script vous permet de trouver un mot dans tous les fichiers d'un dossier

Dossier/fichier à analyser [./Script]: <chemin du dossier à analyser>
Quel mot voulez-vous trouver: <mot recherché>
```
Par défaut le chemin du dossier à analyser sera celui dans lequelle vous vous trouvez (affiché 
entre crochet) pour le sélectionner, ne mettez aucun chemin.


-------------------------------


## compilerASM.py
Permet de compiler un fichier de code asm afin de l'exécuter.        
Pour être utilisé, ce script à besoin du fichier IO.cpp (qui doit être dans le même dossier) mis à 
disposition par l'ULB à ses étudiants sur l'université virtuel.

#### Utilisation
```BASH
python3 compilerASM.py <nom du fichier>
```
Il faut mettre le nom du fichier sans l'extention (`.asm`).


-------------------------------


## compilerASM2.py
Même utilité que `compilerASM.py` mais avec une interface graphique Tkinter pour sélectionner le bon
fichier.

#### Utilisation
```BASH
python3 compilerASM2.py
```


-------------------------------



## compilerASM.sh
Permet de compiler un fichier de code asm afin de l'exécuter.        
Pour être utilisé, ce script à besoin du fichier IO.cpp (quoi doit être dans le même dossier) mis à 
disposition par l'ULB à ses étudiants sur l'université virtuel.

#### Utilisation
```BASH
./compilerASM.sh 
Compilation de fichier assembleur: 

                                  _     _                 
     /\                          | |   | |                
    /  \   ___ ___  ___ _ __ ___ | |__ | | ___ _   _ _ __ 
   / /\ \ / __/ __|/ _ \ '_ ` _ \| '_ \| |/ _ \ | | | '__|
  / ____ \\__ \__ \  __/ | | | | | |_) | |  __/ |_| | |   
 /_/    \_\___/___/\___|_| |_| |_|_.__/|_|\___|\__,_|_|   
                                                          
                                                          
Quel est le nom du fichier que vous voulez compiler (sans le .asm)
<nom du fichier>
```
Il faut mettre le nom du fichier sans l'extention (`.asm`).


