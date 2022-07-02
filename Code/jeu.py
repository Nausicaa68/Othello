from affichage import *
from Saisies import *
from validite_coup import *


R = "\033[31m"
Vert = "\033[32m"
Bleu = "\033[34m"

print("Bonjour, bienvenue dans le jeu du Black & White\n\t1 - Commencer\n\t2 - Règles\n\t3 - Quitter")
cond = True
while cond:
    choix = input("Votre choix : ")
    try:
        choix = int(choix)
        if 0<choix<4:
            cond = False
        else:
            print("Erreur ! Le choix rentré n'est pas correct.")
    except ValueError:
        print("Erreur ! Le choix rentré n'est pas correct.")

if choix == 2:
    regles() #on affiche les règles puis...
    choix = 1 #... retour à la normale -> il nous faut donc éxécuter le code comme si le choix fut 1
if choix == 3:
    continuer = False
    print("Au revoir !\n")
if choix == 1:
    continuer = True
    
    taille = -1
    while taille>14 or taille<6:
        taille = input("Veuillez entrer la taille de votre plateau de jeu (min: 6 ; max:14) : ")
        try:
            taille = int(taille)
        except:
            taille = -1

    print("")
    plateau_sans_pions = creation_plateau(taille)
    plateau = placement_premiers_pions(plateau_sans_pions)
    afficher_plateau(plateau)

tour = 0

while continuer:
     
                          
        
    if tour%2 == 0:   #alternance entre les 2 joueurs
        joueur = "O "
    else:
        joueur = "X "
        
    nbr_pions = nbr_pions_2camps(plateau)
    liste_coups = liste_coups_valides(plateau,joueur)
    passer_tour = passer_son_tour(joueur,liste_coups)     #test si le joueur doit passer son tour
        
    a_place_unpion = True
        
    choix = menu(passer_tour,tour,joueur,nbr_pions)
        
    if choix == "A":
        continuer = sortie()
        a_place_unpion = False
            
    elif choix == "PT":
        tour = tour+1
        a_place_unpion = False
            
    elif choix == "L":
        affichage_liste_coups_valides = afficher_liste_coups_valides(liste_coups)
        print(affichage_liste_coups_valides)
            
        if passer_tour == False:
            choix2 = "ini"
            while choix2 != "P" and choix2 != "p":
                choix2 = input("Appuyez sur P pour placer votre pion: ")
                if choix2 == "P" or choix2 == "p":
                    if joueur == "O ":
                        print(Vert,"C'est au joueur",joueur,"de jouer. ", end="")
                        newpion = input("Où voulez-vous jouer ? (abandonner : A) : ")
                    elif joueur == "X ":
                        print(R,"C'est au joueur",joueur,"de jouer. ", end="")
                        newpion = input("Où voulez-vous jouer ? (abandonner : A) : ")
        else:
            a_place_unpion = False
                    
                    
    elif choix == "P":
        if joueur == "O ":
            print(Vert,"C'est au joueur",joueur,"de jouer. ", end="")
            newpion = input("Où voulez-vous jouer ? (abandonner : A) : ")
        elif joueur == "X ":
            print(R,"C'est au joueur",joueur,"de jouer. ", end="")
            newpion = input("Où voulez-vous jouer ? (abandonner : A) : ")
                    
        
    if a_place_unpion == True:
        if newpion == "A" or newpion == "a":  #abandon
            continuer = sortie()
            newpion = newpion.upper()
    
        if continuer == True and newpion != "A":
            continuer = verif_saisie(newpion)                 #verification du format de la saisie
            if continuer == False:
                print("Erreur ! La saisie est fausse, recommencez...")
                continuer = True
            else:
                new_pion = conversion_coordonnees(newpion)
            
                coup_valide = validite_coup(new_pion,taille,joueur,plateau)                      #attention vérifier la validité du coup avant de le placer
            
                if coup_valide == True:
                    plateau = placer_un_pion(plateau, new_pion, joueur)

                    afficher_plateau(plateau)
                    tour += 1
                    
                    
                    
                    joueurO = "O "
                    joueurX = "X "
                    liste_coupsO = liste_coups_valides(plateau,joueurO)
                    liste_coupsX = liste_coups_valides(plateau,joueurX)
                    nbr_pions = nbr_pions_2camps(plateau)
                    fin = reperer_fin_partie(liste_coupsO,liste_coupsX,taille,nbr_pions)
                    if fin == True:
                        declarer_vainqueur(nbr_pions)
                        continuer = False
                else:
                    print(Bleu," COUP NON VALIDE ! ")        # tour n'est pas incrémenté pour permettre une nouvelle saisie au même joueur
                    

