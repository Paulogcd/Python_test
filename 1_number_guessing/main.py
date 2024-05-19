import random

def erreur() :
    print("Attention : la valeur entrée n'est pas un nombre entier.\n")

def call_max():
    max = input("Entrez la valeur maximale : ")
    return max

print("Bonjour et bienvenue dans ce jeu où l'on doit trouver un nombre !")

while max is not int() : 
    max = call_max()
    # print(max)
    try: 
        max = int(max)
        # print(max)
        break
    except:
        erreur()

true_value = random.randint(0,max)
# print(true_value)

guess = float()
while guess is not true_value:
    guess = input("Quel est le nombre  ? ")
    try:
        guess = int(guess)
        if guess > true_value :
            print("C'est moins !\n")
        if guess < true_value : 
            print("C'est plus !\n")
    except:
        erreur()
        continue

print("Bravo ! Le nombre était bien : ", guess)