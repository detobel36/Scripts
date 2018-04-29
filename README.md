# Script
Voici quelques petits scripts pouvant être utile.

- [findWorld (`bash`)](#findwordsh)
- [compilerASM (`python`)](#compilerasmpy)
- [compilerASM2 (`python`)](#compilerasm2py)
- [compilerASM (`bash`)](#compilerasmsh)
- [serveursULB (`bash`)](#serveursulbsh)
- [scanWifi (`bash`)](#scanwifish)
- [BonPatronLaTex (`python`)](#BonPatronLaTex)

-------------------------------


## [findWord.sh](findWord.sh)
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


## [compilerASM.py](compilerASM.py)
Permet de compiler un fichier de code asm afin de l'exécuter.        
Pour être utilisé, ce script à besoin du fichier IO.cpp (qui doit être dans le même dossier) mis à 
disposition par l'ULB à ses étudiants sur l'université virtuel.

#### Utilisation
```BASH
python3 compilerASM.py <nom du fichier>
```
Il faut mettre le nom du fichier sans l'extention (`.asm`).


-------------------------------


## [compilerASM2.py](compilerASM2.py)
Même utilité que `compilerASM.py` mais avec une interface graphique Tkinter pour sélectionner le bon
fichier.

#### Utilisation
```BASH
python3 compilerASM2.py
```


-------------------------------



## [compilerASM.sh](compilerASM.sh)
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


-------------------------------

## [serveursULB.sh](serveursULB.sh)
Script permettant de se connecter plus facilement aux serveurs de l'ULB.            
[Plus d'informations](http://padi.ulb.ac.be/v2/index.php)        

#### Utilisation:
```BASH
./serveursULB.sh 
Connexion à un serveur de l'ULB: 


 UUUUUUUU     UUUUUUUU     LLLLLLLLLLL                  BBBBBBBBBBBBBBBBB   
 U::::::U     U::::::U     L:::::::::L                  B::::::::::::::::B  
 U::::::U     U::::::U     L:::::::::L                  B::::::BBBBBB:::::B 
 UU:::::U     U:::::UU     LL:::::::LL                  BB:::::B     B:::::B
  U:::::U     U:::::U        L:::::L                      B::::B     B:::::B
  U:::::D     D:::::U        L:::::L                      B::::B     B:::::B
  U:::::D     D:::::U        L:::::L                      B::::BBBBBB:::::B 
  U:::::D     D:::::U        L:::::L                      B:::::::::::::BB  
  U:::::D     D:::::U        L:::::L                      B::::BBBBBB:::::B 
  U:::::D     D:::::U        L:::::L                      B::::B     B:::::B
  U:::::D     D:::::U        L:::::L                      B::::B     B:::::B
  U::::::U   U::::::U        L:::::L         LLLLLL       B::::B     B:::::B
  U:::::::UUU:::::::U      LL:::::::LLLLLLLLL:::::L     BB:::::BBBBBB::::::B
   UU:::::::::::::UU       L::::::::::::::::::::::L     B:::::::::::::::::B 
     UU:::::::::UU         L::::::::::::::::::::::L     B::::::::::::::::B  
       UUUUUUUUU           LLLLLLLLLLLLLLLLLLLLLLLL     BBBBBBBBBBBBBBBBB   

Attention, le programme ne s'arrete pas encore tout seul si aucun serveur n'a été trouvé

Quel est votre NetID ?
<votre netid>
Connexion réussie pour le serveur 1
test@romeo1.ulb.ac.be's password: <votre mot de passe>
```


-------------------------------

## [scanWifi.sh](scanWifi.sh)
Script permettant de scanner la liste des wifi et d'afficher leurs fréquences, le type de signal, 
le type de mot de passe ainsi que le canal utilisé.          
L'affichage est rechargé de manière régulière (configurable).  Le script affiche également le ping de
certains sites.

#### Utilisation:
```BASH
./scanWifi.sh 
Google.be: 13.3 ms | Github: 99.1 ms
==================================================================================================================================================
                                                          Liste de balayage Wi-Fi (wlo1)
==================================================================================================================================================
ACTIF  SSID                            SSID-HEX                                                      CHAN  DÉBIT    SIGNAL  BARS  SÉCURITÉ    
--------------------------------------------------------------------------------------------------------------------------------------------------
oui    VOO-******                      564F****************                                          13    54 Mo/s  49      ▂▄__  WPA1 WPA2   
non    VOO_HOMESPOT                    564F********************                                      13    54 Mo/s  45      ▂▄__              
non    PROXIMUS_FON                    5052********************                                      1     54 Mo/s  37      ▂▄__              
non    WiFi-2.4-****                   5769**********************                                    1     54 Mo/s  37      ▂▄__  WPA2        
non    PROXIMUS_AUTO_FON               5052******************************                            1     54 Mo/s  34      ▂▄__  WPA2 802.1X 
non    Olympe                          4F6C********                                                  5     54 Mo/s  22      ▂___  WPA2        
non    HP-Print-AA-Officejet Pro 8620  4850********************************************************  6     54 Mo/s  20      ▂___  WPA2        
non    WiFi-2.4-********               5769******************************                            1     54 Mo/s  19      ▂___  WPA2        
non    PROXIMUS_FON                    5052********************                                      11    54 Mo/s  19      ▂___              
```

## [BonPatronLaTex.py](BonPatronLaTex.py)
Script permettant de corriger les fautes d'orthographe d'un document LaTeX (`.tex`) en utilisant le site [http://bonpatron.com/](BonPatron.com)

### Utilisation
```
python3 BonPatronLaTex.py
python3 BonPatronLaTex.py <fichier LaTeX>
```
Si aucun paramètre n'est donné lors de l'exécution, une fenêtre tkinter sera ouverte pour permettre de choisir le fichier LaTeX.  Le nom du fichier LaTeX à corrigé peut être mis en paramètre et sera donc corrigé par le site web.            
Le résultat de cette correction sera stocké dans un fichier `result.html` placé dans le même dossier que le script python.  Ce fichier sera lancé automatiquement **ainsi** que la page web de BonPatron (pour afficher les publicités présente sur le site, qui infine le finance).
