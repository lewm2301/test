#----------------------------------------------------------------------
# Auteure : Marie-Claire Lewandowski
# But : Déterminer si un chiffre saisi par l'utilisateur
# est pair ou impair.
#----------------------------------------------------------------------

def pairOuImpair():
    number=int(input("Donnez-moi un nombre entier : "))

    if(number % 2 == 0):
        print(number, "est un nombre PAIR.")
    else:
        print(number, "est un nombre IMPAIR.")

#pairOuImpair()

#----------------------------------------------------------------------
# Auteure : Marie-Claire Lewandowski
# But : Calcul du nombre naturel e
#----------------------------------------------------------------------

def calculNbENaturel():

    # On demande à l'utilisateur la valeur de n
    n = int(input("Quelle est la valeur de n?"))

    # Initialisation des variables
    fact=1
    e=1
    denom=0

    for i in range(1, n+1):
        # Calcul des valeurs factoriel
        fact=fact*i
        # Addition des valeurs factorielles
        denom=denom+fact
        # On place les valeurs factorielles comme dénominateur, ce qui nous donne une fraction
        fraction=1/fact
        # Addition des fractions à chaque tour de boucle
        e=e+fraction

    # On imprime la valeur de e
    print("La valeur de 'e' est de :", e)

#calculNbENaturel()

#----------------------------------------------------------------------
# Auteure : Marie-Claire Lewandowski
# But : Vérification si une année est bisextile ou non
#----------------------------------------------------------------------

def bisextile():
    year=int(input("Donnez-moi une année : "))

    if(year % 4 == 0 or year % 400 == 0):
        response=True
        print(response,":", year, "est une année bisextile.")
    else:
        response=False
        print(response,":", year, "N'est PAS une année bisextile.")

#bisextile()

#----------------------------------------------------------------------
# Auteure : Marie-Claire Lewandowski
# But : Vérifier si un mot est un pallindrome
#----------------------------------------------------------------------

def pallindrome():

    mot=input("Donnez-moi mot: ")
    longueurMot=len(mot)
    compteur=0

    # La boucle part de 0 à la moitié de la longueur du mot
    for i in range(0, int(longueurMot/2)):
        # On compare les lettres en partant de l'extême gauche
        # et de l'extrême droite (décommenter la ligne suivante pour voir).
        #print(mot[i], mot[-i-1])
        if mot[i] == mot[-i-1]:
            compteur=compteur+1

    if (int(longueurMot/2) != int(compteur)):
        print("Il NE s'agit PAS d'un pallindrome.")

    else:
        print("Il s'agit BIEN d'un pallindrome.")

#pallindrome()