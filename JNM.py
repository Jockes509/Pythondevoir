import random

nbr_alea=random.randint(0,10)
nbr_tent=3

print("")
print("Hello! Bienvenue sur Jockes Game")
nom=input("Entrer votre nom svp: ")
print("")
print(nom," l'ordinateur a choisi un nombre compris entre 0 a 10, alors devine le nombre")
print("")

while nbr_tent>0:
    nbr_tent-=1
    vs=int(input("Entrer un nombre compris entre 0 a 10: "))
    
    if vs<nbr_alea:
        print("C'est plus! reessayer svp, et il vous reste ",nbr_tent,"tentatives")
        
    elif vs<nbr_alea:
        print("C'est moins! reessayer svp, et il vous reste ",nbr_tent,"tentatives")

    else: 
        break
    
if nbr_tent !=0:
    print("Felicitations",nom,"! vous avez trouve le bon nombre en ",3-nbr_tent,"essais")
else: 
        print("Malheureusement"," vous avez depasse les 3 tentatives, le nombre etait ",nbr_alea)