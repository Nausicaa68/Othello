from affichage import *

def coup_valide(new_pion,plateau,joueur):     #fonction intermédiaire utilisée dans validite_coup afin de verifier si le coup est valide
    coup_valide = False
    col = new_pion[1]-1
    lig = new_pion[0]
    
    if joueur == "O ":
        carac1 = "X "
        carac2 = "O "
    elif joueur =="X ":
        carac1 = "O "
        carac2 = "X "
    
        
        
        
    if (col-1)<(len(plateau[lig])) and plateau[lig][col-1] == carac1:         #horizontal vers la gauche
        j = col-1
        while j<(len(plateau[lig])) and plateau[lig][j] == carac1:
            j = j-1
        if j<(len(plateau[lig])) and plateau[lig][j] == carac2:
            coup_valide = True
            for i in range(j+1,col):
                plateau[lig][i] = carac2
                    
        
    if (col+1)<(len(plateau[lig])) and plateau[lig][col+1] == carac1:   #horizontal vers la droite
        j = col+1
        while j<(len(plateau[lig])) and plateau[lig][j] == carac1:
            j = j+1
        if j<(len(plateau[lig])) and plateau[lig][j] == carac2:
            coup_valide = True
            for i in range(col+1,j):
                plateau[lig][i] = carac2
                    
        
    if (lig+1)<(len(plateau)) and plateau[lig+1][col] == carac1:  #vertical vers le bas     #len(plateau) = nbr de lignes
        j = lig+1
        while j<(len(plateau)) and plateau[j][col] == carac1:
            j = j+1
        if j<(len(plateau)) and plateau[j][col] == carac2:
                
            coup_valide = True
            for i in range(lig+1,j):
                plateau[i][col] = carac2
                    
        
    if (lig-1)<(len(plateau)) and plateau[lig-1][col] == carac1:  #vertical vers le haut
        j = lig-1
        while j<(len(plateau)) and plateau[j][col] == carac1:
            j = j-1
        if j<(len(plateau)) and plateau[j][col] == carac2:
                
            coup_valide = True
            for i in range(j+1,lig):
                plateau[i][col] = carac2
                    
        
    if (lig+1)<len(plateau) and (col-1)<len(plateau[lig]) and plateau[lig+1][col-1] == carac1:   #diagonale  en bas à gauche
        i = lig+1
        j = col-1
        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
            i = i+1
            j = j-1
        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
            coup_valide = True
            z = lig+1
            a = col-1
            while z < i and a>j:
                plateau[z][a] = carac2
                z = z+1
                a = a-1
                
        
    if (lig+1)<len(plateau) and (col+1)<len(plateau[lig]) and plateau[lig+1][col+1] == carac1:   #diagonale  en bas à droite
        i = lig+1
        j = col+1
        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
            i = i+1
            j = j+1
        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
            coup_valide = True
                
            z = lig+1
            a = col+1
            while z < i and a<j:
                plateau[z][a] = carac2
                z = z+1
                a = a+1
                    
        
    if (lig-1)<len(plateau) and (col-1)<len(plateau[lig]) and plateau[lig-1][col-1] == carac1:  #diagonale en haut à gauche
        i = lig-1
        j = col-1
        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
            i = i-1
            j = j-1
        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
            coup_valide = True
            z = lig-1
            a = col-1
            while z > i and a>j:
                plateau[z][a] = carac2
                z = z-1
                a = a-1
                        
        
    if (lig-1)<len(plateau) and (col+1)<len(plateau[lig]) and plateau[lig-1][col+1] == carac1:  #diagonale en haut à droite
        i = lig-1
        j = col+1
        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
            i = i-1
            j = j+1
        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
            coup_valide = True
            z = lig-1
            a = col+1
            while z > i and a<j:
                plateau[z][a] = carac2
                z = z-1
                a = a+1
        
    
    return coup_valide
            
    


# vérifie si le coup du joueur est valide
def validite_coup(new_pion,taille,joueur,plateau):   #pion dans le plateau/il ne faut rien dans la case /possibilité de jouer(prendre un pion adverse)
                                                     # new_pion a les coordonées du coup ex: d15 -> [4,15]
    cond = False
    if 0<new_pion[0]<=taille and 0<new_pion[1]<=taille:
        
        if plateau[new_pion[0]][new_pion[1]-1] == ". ":           #case vide
            
            coup_valid = coup_valide(new_pion,plateau,joueur)
            if coup_valid == True:                                             #distinguer 3 cas horizontal/vertical/diagonale
                cond = True
    
    return cond             # si cond==True  le pion respecte toutes les conditions pour être placé

def liste_coups_valides(plateau,joueur):     #fonction qui établit la liste des coups valides qui pourra ensuite être demandée par l'utilisateur
    liste_coup_valides = []
    taille = len(plateau)

    
    for c in range(1,taille):   #on n'analyse pas la première ligne car elle correspond aux lettres
        for d in range(taille):
            
            lig = c
            col = d
            
            
            if joueur == "O ":
                carac1 = "X "
                carac2 = "O "
            elif joueur =="X ":
                carac1 = "O "
                carac2 = "X "
                
                
            coup_valide = False
            while coup_valide == False:
                
                if plateau[c][d] == ". ":   #on ne peut pas jouer si on a déjà un pion sur la case
                    
                    if (col-1)<(len(plateau[lig])) and plateau[lig][col-1] == carac1:         #horizontal vers la gauche
                        j = col-1
                        while j<(len(plateau[lig])) and plateau[lig][j] == carac1:
                            j = j-1
                        if j<(len(plateau[lig])) and plateau[lig][j] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                    
        
                    if (col+1)<(len(plateau[lig])) and plateau[lig][col+1] == carac1:   #horizontal vers la droite
                        j = col+1
                        while j<(len(plateau[lig])) and plateau[lig][j] == carac1:
                            j = j+1
                        if j<(len(plateau[lig])) and plateau[lig][j] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                    
        
                    if (lig+1)<(len(plateau)) and plateau[lig+1][col] == carac1:  #vertical vers le bas     #len(plateau) = nbr de lignes
                        j = lig+1
                        while j<(len(plateau)) and plateau[j][col] == carac1:
                            j = j+1
                        if j<(len(plateau)) and plateau[j][col] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                
                    
        
                    if (lig-1)<(len(plateau)) and plateau[lig-1][col] == carac1:  #vertical vers le haut
                        j = lig-1
                        while j<(len(plateau)) and plateau[j][col] == carac1:
                            j = j-1
                        if j<(len(plateau)) and plateau[j][col] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                
        
                    if (lig+1)<len(plateau) and (col-1)<len(plateau[lig]) and plateau[lig+1][col-1] == carac1:   #diagonale  en bas à gauche
                        i = lig+1
                        j = col-1
                        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
                            i = i+1
                            j = j-1
                        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                
                
                
        
                    if (lig+1)<len(plateau) and (col+1)<len(plateau[lig]) and plateau[lig+1][col+1] == carac1:   #diagonale  en bas à droite
                        i = lig+1
                        j = col+1
                        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
                            i = i+1
                            j = j+1
                        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                    
                        
        
                    if (lig-1)<len(plateau) and (col-1)<len(plateau[lig]) and plateau[lig-1][col-1] == carac1:  #diagonale en haut à gauche
                        i = lig-1
                        j = col-1
                        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
                            i = i-1
                            j = j-1
                        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                
                        
        
                    if (lig-1)<len(plateau) and (col+1)<len(plateau[lig]) and plateau[lig-1][col+1] == carac1:  #diagonale en haut à droite
                        i = lig-1
                        j = col+1
                        while i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac1:
                            i = i-1
                            j = j+1
                        if i<len(plateau) and j<len(plateau[lig]) and plateau[i][j] == carac2:
                            coup_valide = True
                            if [c,d] not in liste_coup_valides:
                                liste_coup_valides.append([c,d])
                
                
                    coup_valide = True
                else:
                    coup_valide = True
                    
                        
    return liste_coup_valides


def passer_son_tour(joueur,liste_coups):        #fonction qui détecte si le joueur doit passer son tour
    taille=len(liste_coups)
    
    if taille != 0:
        return False
    else:
        return True   #le joueur doit passer son tour


