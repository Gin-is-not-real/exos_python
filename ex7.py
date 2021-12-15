# doit retourner true
test1 = [4, 4, 1, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 3]
# doit retourner false
test2 = [4, 4, 1, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 4] 

def is_credit_card_number_valid(num):
    is_valid = False
    somme = 0
    
    # on double à partir de l'avant dernier, soit l'index i
    for i in range(14, -1, -2):
        num[i] = num[i] * 2
        
        # si le chiffre obtenu est sup à 9, on additionne chaque unité
        if num[i] > 9:
            unites = num[i] % 10
            dizaines = (num[i] - unites)/10
            num[i] = dizaines + unites
            
        # on ajoute au chiffre non doublé (l'index [i]) le chiffre doublé
        num[i + 1] = num[i + 1] + num[i]
        
        # on ajoute le chiffre à la somme
        somme = somme + num[i + 1]
        
    # on verifie que la somme est divisible par 10
    if somme%10 == 0:
        is_valid = True
            
    return is_valid
            
# on appelle la fonction
print(is_credit_card_number_valid(test1))  
print(is_credit_card_number_valid(test2)) 
print(is_credit_card_number_valid([4,9,7,8,7,4,0,5,1,3,2,3,5,0,2,9]))