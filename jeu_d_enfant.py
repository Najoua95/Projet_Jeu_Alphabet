#version 1
import random
import string
import time

# Fonction pour poser des questions intro à l'enfant
int(input('Quel âge as tu ?'))
#input('Souhaites tu t\'entrainer avec les lettres ou les chiffres ?')
input("Ensemble, nous allons apprendre l'alphabet")

#if reponse = lettres
#if reponse = chiffres


# Fonction lettre aléatoire de l'ordi
#def lettre_ordi() :
string.ascii_letters
print('La lettre tirée au sort est : ')
time.sleep(2)
x = random.choice(string.ascii_letters)
print(x)

input('Quelle est la lettre suivante ?')

a = (ord(lettre) - ord('a')) + 1

while True :
    if 'x' == 'a' :
        print('Bravo !')
        break
    else :
        print('Ce n\'est pas la bonne réponse. Essayes encore !')

# Fonction contrôle des exceptions
def lettre_suivante():
    while True :
        try :
            lettre_joueur = input('Quelle est la lettre suivante ? ')
            break
        except ValueError :
            print('Tu dois taper une lettre')
    return lettre_joueur

