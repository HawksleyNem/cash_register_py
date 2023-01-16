money_list = []
result = 0
sum = int(input("Quelle somme payez-vous : "))
money = sum

if sum != 0:    #Implémentation des valeurs dans la liste
    while money != 0:
        if money >= 20:
            money_list.append(20)
            money = money - 20
        elif money >= 10 and money < 20:
            money_list.append(10)
            money = money - 10
        elif money >= 5 and money < 10:
            money_list.append(5)
            money = money - 5
        elif money >= 2 and money < 5:
            money_list.append(2)
            money = money - 2
        elif money >= 1 and money < 2:
            money_list.append(1)
            money = money - 1
    
    if money_list.count(20) >= 1:   #Comptage des billets et des pièces en fonction de leur valeur
        print(f"{money_list.count(20)} billet(s) de 20€")
    if money_list.count(10) >= 1:
        print(f"{money_list.count(10)} billet(s) de 10€")
    if money_list.count(5) >= 1:
        print(f"{money_list.count(5)} billet(s) de 5€")
    if money_list.count(2) >= 1:
        print(f"{money_list.count(2)} pièce(s) de 2€")
    if money_list.count(1) >= 1:
        print(f"{money_list.count(1)} pièce(s) de 1€")

else:   #Si la monnaie possède une valeur nulle
    print("Aucun rendu.")
