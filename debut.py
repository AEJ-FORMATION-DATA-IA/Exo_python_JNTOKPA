#initialisations et operations
a = 15
b = 4
c = a + b  #somme
d = a * b  #produit
e = a ** b  #exposant
f = a / b   #division flottante
g = a // b  #division entiere
h = a % b   #modulo

print(f"Le resultat de {a} + {b} est {c}")
print("le resultat de {} * {} est {}".format(a,b,d))
print("le resultat de {} exposant {} est {}".format(a,b,e))
print("le resultat de {} / {} est {}".format(a,b,f))
print("le resultat de la division entiere de {} par {} est {}".format(a,b,g))
print("le resultat de {} modulo {} est {}".format(a,b,h))

#--------------les listes------------------#

#creation et affichage de liste1 contenant les caracteres a, b, c et d
liste1 = ["a", "b", "c", "d"]
print("la liste 1 contient {}".format(liste1))

#creation et affichage de liste2 contenant les valeurs de a, b, c et d
liste2 = [a, b, c, d]
print("la liste 2 contient {}".format(liste2))

#creation et affichage de liste3 contenant liste1 et liste2
liste3 = [liste1, liste2]
print("la liste 3 contient {}".format(liste3))

#ajouter e et f a liste1
liste1.extend(["e", "f"])
print("la liste 1 apres ajout de e et f {}".format(liste1))

#supprimer b de la liste 1
liste1.remove("b")
print("la liste 1 apres suppression de b {}".format(liste1))

#remplacer a par g dans la liste 1
index_a = liste1.index("a")
liste1[index_a] = "g"
print("la liste 1 apres remplacement de a par g {}".format(liste1))

#---------------les tuples------------------------#

#creation et affiichage de tuple
mon_tuple = (a, b, c)
print("le tuple contient {}".format(mon_tuple))

#ajouter d dans tuple
mon_tuple = list(mon_tuple)
mon_tuple.append(d)
print("le tuple apres ajout de d {}".format(mon_tuple))

#modifier a en 16
ind_a = mon_tuple.index(a)
mon_tuple[ind_a] = 16
print("le tuple apres modif de a en 16 {}".format(mon_tuple))

#supprimer b du tuple
mon_tuple.remove(b)
mon_tuple = tuple(mon_tuple)
print("le tuple apres suppression de b {}".format(mon_tuple))

#------------les dictionnaires--------------------#

#creation de dictionnaire
mon_dict = {"addition" : c, "multiplication" : d, "puissance" : e, "division_flottante" : f, "division_entiere" : g}
print("mon dictionnaire {}".format(mon_dict))

#ajouter h au dictionnaire
mon_dict["modulo"] = h
print("le dictionnaire apres ajout de h contient {}".format(mon_dict))

#suppression de h du dictionnaire
del mon_dict["modulo"]
print("le dictionnaire apres suppression de h contient {}".format(mon_dict))

#afficher la liste des cles du dictionnaire
print(list(mon_dict.keys()))

#affichage des valeurs du dictionnaire
print(list(mon_dict.values()))

#affichage des cle-valeur du dictionnaire
print("le dictionnaire contient {}".format(mon_dict))