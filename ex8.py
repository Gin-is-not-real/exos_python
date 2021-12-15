attendu = [False, False, True, True, False, True, False, True, False, False, False] 

# fonction
def erastosthenes(max):
    prime_numbers = []
    
    # pour chaque nmbre de 0 à max on passe tout a True:
    for i in range(0, max + 1):
        prime_numbers.append(True)
    # on sait que 0 et 1 sont False    
    prime_numbers[0] = False
    prime_numbers[1] = False
    # on boucle donc à partir de l'index 2
    for i in range(2, max + 1):
        if prime_numbers[i]:
            r1 = i*i
            for j in range(r1, max + 1, i):
                prime_numbers[j] = False
    return prime_numbers
    
# function's call and print result
print(erastosthenes(10))

# test ?
print(erastosthenes(10) == attendu)