#!/usr/bin/python
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
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror


root = Tk()
root.title = "Compilation"

listbox = Listbox(root, width=40, height=20)
listbox.pack()

while(not os.path.exists("IO.cpp")):
  showerror("Fichier manquant", "Il manque le fichier IO.cpp disponible sur l'uv")


listbox.insert(END, "Choix du fichier")

nom_fichier = askopenfilename(defaultextension=".asm", title="Fichier a compiler", filetypes=[('Fichier ASM','*.asm')])

if(nom_fichier != None and nom_fichier != ""):
  nom_split = nom_fichier.split(".")
  nom_fichier = ".".join(nom_split[:-1])

  listbox.insert(END, "Fichier choisi: ", nom_fichier)
  listbox.insert(END, "    -=-")
  listbox.insert(END, "Lancement de la commande nasm")

  os.system('nasm -f elf ' + nom_fichier + '.asm')
  
  if(os.path.exists(nom_fichier + ".o")): # Si la première commande fonctionne

      ##################
      # Seconde commande
      listbox.insert(END, "Lancement de la compilation (g++)")
      os.system('g++ IO.cpp ' + nom_fichier + '.o -m32 -o exec')

      if(os.path.exists("./exec")):
          listbox.insert(END, "Lancement du programme")
          os.system('./exec')
      else:
          listbox.insert(END, "La compilation à échouée")

  else: # Si le fichier .o n'a pas été créé
      listbox.insert(END, "La commande n'a pas fonctionnée")


root.mainloop()






