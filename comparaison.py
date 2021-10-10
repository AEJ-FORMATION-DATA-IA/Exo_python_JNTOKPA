#Comparaison de comparaison de deux entiers
print("comparer deux entiers")
nbre1 = input("Entrer un nombre entier : ")
try:
    nbre1 = int(nbre1)
except ValueError:
    print("Vous avez fait une erreur")
else:
    nbre2 = input("Entrer un nombre entier : ")
    try:
        nbre2 = int(nbre2)
    except:
        print("Vous avez fait une erreur")
    else:
        if nbre1 > nbre2 :
            print(str(nbre1) + " > " + str(nbre2))
        elif nbre1 < nbre2:
            print(str(nbre1) + " < " + str(nbre2))
        else:
            print(str(nbre1) + " = " + str(nbre2))