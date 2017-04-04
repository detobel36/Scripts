# Script
Voici quelques petits scripts pouvant être utile.

- [findWorld](#findwordsh)
- [compilerASM](#compilerasm)
- [compilerASM2](#compilerasm2)


## findWord.sh
Permet de retrouver un mot dans un dossier.

#### Utilisation
```BASH
./findWord.sh 
Ce script vous permet de trouver un mot dans tous les fichiers d'un dossier

Dossier/fichier à analyser [./Script]: 
Quel mot voulez-vous trouver: test
/home/remy/Bureau/Script/server.sh
43.         echo "Test de connexion au serveur $i"
/home/remy/Bureau/Script/test.sh
39.         echo "Test de connexion au serveur $i"
```

## compilerASM.py
Permet de compiler un fichier de code asm afin de l'exécuter.        
Pour être utilisé, ce script à besoin du fichier IO.cpp mis à disposition par l'ULB à ses étudiants
sur l'université virtuel.

#### Utilisation
```BASH
python3 compilerASM.py <nom du fichier>
```
Il faut mettre le nom du fichier sans l'extention (`.asm`).


## compilerASM2.py
Même utilité que `compilerASM.py` mais avec une interface graphique Tkinter pour sélectionner le bon
fichier.

#### Utilisation
```BASH
python3 compilerASM2.py
```

