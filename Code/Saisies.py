def verif_saisie(newpion):
    continuer = False   
    lettre = newpion[0]   #on prend la première valeur de la chaine, supposement un caractère
    if 64<ord(lettre)<91 or 96<ord(lettre)<123:  #si c'est un caractère
        piontest = newpion.replace(lettre, "")   #on enlève ce caractpour vérifier si le reste est un chiffre
        try:
            piontest = int(piontest)
            continuer = True
        except ValueError:
            continuer = False
    
    return continuer

def conversion_coordonnees(newpion):     #fonction qui convertit la saisie de l'utilisateur ex: a5  en coordonnées qui correspondent aux lignes et colonnes du plateau(notre liste 2D)
    lettre = newpion[0]
    chiffre = int(newpion.replace(lettre, ""))  #On enlève la lettre -> le 5 de "d5" ; il faut le convertir en int
    lettre = lettre.upper()    # on met la lettre en majuscule
    lettre = ord(lettre)-64    # on la convertit en un chiffre 
    new_pion = [chiffre, lettre]
    
    return new_pion

def placer_un_pion(plateau, new_pion, joueur):      #fonction qui place le pion en fonction de la saisie des coordonnées converties au préalable par la fonction conversion_coordonnées
    ligne = plateau[new_pion[0]]    # sélectionne la ligne
    ligne[new_pion[1]-1] = joueur   # sélectionne la colonne (-1 car c'est une liste -> on commence à 0)
                                    # joueur est à la fois le nom du joueur et le symbole
    return plateau

def sortie():                 #fonction qui permet au joueur d'arrêter la partie(abandonner) à tout moment 
    
    cond = True
    while cond:
        print("Voulez-vous vraiment abandonner votre partie ? 0- Oui  1-Non")
        w = input()
        try:        # vérifie que w est entier et qu'il vaut 0 ou 1 
            w=int(w)
            if w==0 or w==1:
                cond = False
            else:
                print("Erreur")
        except:
            print("Erreur")
    if w == 0:
        return False
    else:
        return True