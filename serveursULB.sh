#!/bin/bash


echo "Connexion à un serveur de l'ULB: "
echo ""
echo ""
echo " UUUUUUUU     UUUUUUUU     LLLLLLLLLLL                  BBBBBBBBBBBBBBBBB   "
echo " U::::::U     U::::::U     L:::::::::L                  B::::::::::::::::B  "
echo " U::::::U     U::::::U     L:::::::::L                  B::::::BBBBBB:::::B "
echo " UU:::::U     U:::::UU     LL:::::::LL                  BB:::::B     B:::::B"
echo "  U:::::U     U:::::U        L:::::L                      B::::B     B:::::B"
echo "  U:::::D     D:::::U        L:::::L                      B::::B     B:::::B"
echo "  U:::::D     D:::::U        L:::::L                      B::::BBBBBB:::::B "
echo "  U:::::D     D:::::U        L:::::L                      B:::::::::::::BB  "
echo "  U:::::D     D:::::U        L:::::L                      B::::BBBBBB:::::B "
echo "  U:::::D     D:::::U        L:::::L                      B::::B     B:::::B"
echo "  U:::::D     D:::::U        L:::::L                      B::::B     B:::::B"
echo "  U::::::U   U::::::U        L:::::L         LLLLLL       B::::B     B:::::B"
echo "  U:::::::UUU:::::::U      LL:::::::LLLLLLLLL:::::L     BB:::::BBBBBB::::::B"
echo "   UU:::::::::::::UU       L::::::::::::::::::::::L     B:::::::::::::::::B "
echo "     UU:::::::::UU         L::::::::::::::::::::::L     B::::::::::::::::B  "
echo "       UUUUUUUUU           LLLLLLLLLLLLLLLLLLLLLLLL     BBBBBBBBBBBBBBBBB   "
echo ""
echo "Attention, le programme ne s'arrete pas encore tout seul si aucun serveur n'a été trouvé"
echo ""
echo "Quel est votre NetID ?"
read netid

serveur="romeo" # Or roxan

# Initialisation
i="0"

# Recherche du meilleur serveur
while [ true ]; do
    i=$((i+1))
    status=$(ssh -o BatchMode=yes -o ConnectTimeout=3 $serveur$i.ulb.ac.be echo ok 2>&1)

    if [[ $status == ok ]] || [[ $status == "Permission denied"* ]] ; then
        echo "Connexion réussie pour le serveur $i"
        break;

    #if ping -c1 -w 3 $serveur$i.ulb.ac.be > /dev/null; then
    #    echo "Connexion réussie pour le serveur $i"
    #    break;


    # elif $i > 2; then
    #     break;
    else
        echo "Test de connexion au serveur $i"
    fi
done

ssh -X $netid@$serveur$i.ulb.ac.be
echo "Appuyer la touche <Entrée> pour fermer..."
read touche
echo "Fin de la connexion"
