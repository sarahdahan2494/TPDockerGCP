# coding: utf-8
# TP ef-else consonne voyelle

caractere=str(input("Veuillez saisir une lettre : "))
caractere2=str.lower(caractere)          # Transforme le caractère en minuscule si c'est une majuscule afin de pouvoir tester toutes les saisies utilisateur
if (caractere2=='a' or caractere2=='e' or caractere2=='i' or caractere2=='o' or caractere2=='u' or caractere2=='y') :
# On peut aussi tester les différentes voyelles comme suit : (if caractere2 in "a,e,i,o,u,y":)
# Une autre manière serait de stocker les différentes voyelles dans une liste : liste=["a","e","i","o","u","y"] et de tester avec la condition : (if caractere2 in liste:)
    print("C'est une voyelle")
else :
    print("C'est une consonne")

# chaine=str(input("Veuillez saisir une chaîne de caractère : "))
# chaine2=str.lower(chaine)
# print("La chaîne en minuscule est : ",chaine2)