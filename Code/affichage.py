from validite_coup import *


    
def creation_plateau(taille):     #fonction qui crée le plateau vide en début de partie
    plateau = []
    ligne = []
    
    for i in range(taille):
        ligne.append(chr(i+65) + " ")   # on créer la première ligne, avec les lettres
    plateau.append(ligne + [" "])       # on rajoute un espace pour que cette ligne fasse la meme taille que les autres...
    ligne = []                          # ...c-a-d (taille+1) -> moins embêtant pour l'affichage
        
    
    for i in range(taille):
        for j in range(taille+1):
            if j == taille:
                ligne.append(str(i+1) + " ")   # j == taille -> dernière colonne du plateau, on y met le chiffre de la ligne, donc i+1
            else:                              # on le convertit en str pour qu'il soit considérer comme tel et pour y conquaténer " "
                ligne.append(". ")         
            
        plateau.append(ligne)     # on ajoute cette ligne au plateau, et on recommence
        ligne = []
    
    return plateau

def placement_premiers_pions(plateau):         #cette fonction positionne les 4 pions de départ
    taille = len(plateau)
    #on place les pions du centre (ex: pour taille = 8)
    mil1 = taille//2  #4
    mil2 = (taille//2)+1 #5
    mil3 = (taille//2)-1 #3
    
    plateau[mil1][mil1] = "X "   #4,4
    plateau[mil2][mil3] = "X "   #5,3
    plateau[mil1][mil3] = "O "   #4,3
    plateau[mil2][mil1] = "O "   #5,4
    
    return plateau

def afficher_plateau(plateau):          #cette fonction correspond à l'affichage du plateau mais se situe dans le dossier color car
                                        #c'est une variante de notre affichage de base qui lui n'attribuait pas de couleur aux pions
    N = "\033[30m"
    R = "\033[31m"
    Vert = "\033[32m"
    
    chaine = ""
    taille = len(plateau)
    
    for j in range(taille):
        chaine += N + plateau[0][j]
    print(chaine)   
    chaine = ""
    
    for i in range(1,taille):
        for j in range(taille):
            if plateau[i][j] == "X ":
                chaine += R + plateau[i][j]
            elif plateau[i][j] == "O ":
                chaine += Vert + plateau[i][j]
            else:
                chaine += N + plateau[i][j]
            
            
        print(chaine)   #on met un print dans cette fonction car elle ne sert qu'à afficher le plateau. Autant mettre le print là
        chaine = ""
    print("")
    
    
    
def regles():
    # affiche les règles du Black & White
    
    print(" ")
    print("Bienvenue dans le jeu du Black & White.") 
    print("Ce jeu se joue à deux joueurs, l’un joue avec les pions X, l’autre avec les pions O.")
    print("Dans un premier temps, un des joueurs va poser un de ses pions. Son objectif est de « capturer » un pion adverse.")
    print("Pour cela, il doit encadrer le dit-pion.")
    print(" ")
    print("Une fois encadré, le pion change. Il devient de la même forme et couleur que les pions qui l’entourent.")
    print(" ")
    print("Le joueur doit dans tous les cas poser un pion, même si cela n’est pas à son avantage.")
    print("Cas particulier, si un joueur ne peut pas poser un pion de telle sorte à en entourer un autre adverse, il passe son tour automatiquement.")
    print(" ")
    print("La partie s’arrête si un joueur n’a plus de pions de sa couleur sur le plateau, si aucun des deux joueurs ne peut jouer") 
    print("(ainsi, si les deux joueurs passent leur tour, la partie s’arrête par blocage mutuel), ou si le plateau est entièrement rempli.")
    print(" ")
    print("Le vainqueur est celui qui, à la fin d’une partie, a le plus de pions de sa couleur sur le plateau.")
    print(" ")
    
    input("Appuyer sur entrer pour continuer ...")
    print("\n")

def nbr_pions_2camps(plateau):     #fonction qui permet de connaître le score des 2 joueurs

    taille = len(plateau)
    compteur_nbX = 0
    compteur_nbO = 0
    
    for i in range(taille):
        for j in range(taille):
            if plateau[i][j] == "X ":
                compteur_nbX = compteur_nbX +1
            if plateau[i][j] == "O ":
                compteur_nbO = compteur_nbO+1
    
    return compteur_nbX , compteur_nbO

 

def afficher_liste_coups_valides(liste_coup_valides):     #fonction qui affiche et convertit la liste des coups valides pour que cela corresponde à des coordonnées pour l'utilisateur
    taille = len(liste_coup_valides)                      # exemple : on convertit les coordonées 3,5 en coup pour l'utilisateur -> F3
    liste_coups_valides_affichee = []
    
    for i in range(taille):
        liste = []
                                            
        chiffre = liste_coup_valides[i][0]        #ligne donc chiffre donc change pas
        lettre = chr(liste_coup_valides[i][1] + 97)     #colonne donc lettre
        liste.append(lettre)
        liste.append(chiffre)
        
        liste_coups_valides_affichee.append(liste)
        
    return liste_coups_valides_affichee
        

def menu(passer_tour,tour,joueur,nbr_pions):   #fonction qui affiche un menu qui propose une aide sur les touches à utiliser
    R = "\033[31m"
    Vert = "\033[32m"
    Noir = "\033[30m"
    
    print("Tour n°",tour+1)
    if joueur == "O ":
        print(Vert,"C'est au tour de",joueur)
        
        if passer_tour == True:
            print(Vert,joueur,"ne peut pas jouer")
        else:
            print(Vert,joueur,"doit jouer")
        
    
    
    elif joueur == "X ":
        print(R,"C'est au tour de",joueur)
        
        if passer_tour == True:
            print(R,joueur,"ne peut pas jouer")
        else:
            print(R,joueur,"doit jouer")
    
    
        
    
    nb_pionsX = nbr_pions[0]
    nb_pionsO = nbr_pions[1]
    
    print(Noir,"Pions :  O ",nb_pionsO)
    print("          X ",nb_pionsX)
    
    if passer_tour == True:
        choix = "ini"
        while choix != "A" and choix != "PT" and choix != "L":
            print("Commandes : ")
            print("     PT: passer son tour")
            print("     A: abandon")
            print("     L: liste des coups valides")
            choix = input("Votre choix d'action : ")
            choix = choix.upper()
        
            
    
    
    elif passer_tour == False:
        choix = "ini"
        while choix != "A" and choix != "P" and choix != "L":
            print("Commandes : ")
            print("     P: placer un pion")
            print("     A: abandon")
            print("     L: liste des coups valides")
            choix = input("Votre choix d'action : ")
            choix = choix.upper()
              
    
    return choix               
                

def reperer_fin_partie(liste_coupsO,liste_coupsX,taille_plateau,nbr_pions):   #fonction qui repère les différents cas de fin de partie
    nb_pionsX = nbr_pions[0]
    nb_pionsO = nbr_pions[1]
    
    
    if nb_pionsX+nb_pionsO == taille_plateau*taille_plateau:     
        print("Partie terminée car plateau plein")
        return True
    
    
    elif (nb_pionsX == 0 and nb_pionsO != 0) or (nb_pionsX != 0  and nb_pionsO == 0 ):
        print("Victoire par élimination")
        return True
    
    elif len(liste_coupsO)==0 and len(liste_coupsX)==0: #cas de fin de partie le moins prioritaire
        print("Partie terminée par blocage mutuel")
        return True
    
    
    else:
        return False
        

def declarer_vainqueur(nbr_pions):    #fonction qui permet de déclarer le vainqueur lorsqu'on a détecter la fin de partie
    nb_pionsX = nbr_pions[0]
    nb_pionsO = nbr_pions[1]
    
    if nb_pionsX == nb_pionsO:
        print("Il y a égalité")
        
    
    if nb_pionsX > nb_pionsO:
        print("Le joueur X gagne")
    
    if nb_pionsX < nb_pionsO:
        print("Le joueur O gagne")
    
    
    print("Pions :  O ",nb_pionsO)
    print("         X ",nb_pionsX)
    return