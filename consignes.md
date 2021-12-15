## 7
**Ecrire le prog ex7.py qui defini la function is_credit_card_number_valid à unparametre num (array int) est le num à 16 chiffre d'une carte bancaire.La fonction return vrai si le num est valid sinon faux**  

1- prenez l'ensemble des 16 chiffres

2- doublez un chiffre sur 2 en partant de l'avant dernier jusqu'au début

3- additionnez ces chiffres à ceux que vous n'avez pas doublés

4- si un chiffre est supérieur à 9, additionnez chaque unité (10 = 1 + 0)

5- si la somme obtenue est divisible par 10, alors le num de carte est valid  

**autorisés:**  
def, for, if, in, return  
-, +, %, --, >  
range  

**attendu:**
(4, 4, 1, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 3) = vrai
(4, 4, 1, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 4) = faux


## 8
**Ecrire le programme ex8.py qui defini la fonction erastosthenes à un parametre max. Elle retourne un tableau de bool prime_numbers avec prime_numbers[n] qui vaut vrai si n est premier est faux sinon (pour n compris entre 0 et max). Un nombre premier est entier qui as pour diviseur un et lui méme. Par exmeple, 0 n'est pas premier car il a plus de 2 diviseurs, 1 ne l'est pas car il n'en as qu'un seul. Implémenterl'algo d'Eratostene**

**Algorithme d'erastosthenes**
Function erastosthenes(max)

    For index1 From 0 To max Do
        prime_numbers[index1] :- True
    EndFor

    prime_numbers[0] :- False
    prime_numbers[1] :- False

    For index1 From 2 To max Do
        If prime_numbers[index1] Then
            For index2 From index1 * index1 To max withStep index1
                prime_numbers[index2] :- False
            EndFor
        EndIf
    EndFor
    Return prime_numbers
EndFunction

**autorisés:**  
def, else, for, if, in, return  
-, +, *  
range  

**attendu:**
erastosthenes(10)
[false, false, true, true, false, true, false, true, false, false, false] 

## 9
definir quadratic_equation à 3 param a, b, c. a est le premier coeff d'un equation du second degrés. 
b est le deuxieme coef de cette equation. 
c le troisieme. 
Rappel sur le calcul des solutions d'une équation du second degrés:

*une équation ax**2 + bx + c = 0, avec discriminant DELTA = b**2 - 4ac, 
à 0 solution si DELTA < 0, 
à 1 solution si DELTA = 0 qui est (-b/2a) 
et 2 solution si DELTA > 0 qui sont (-b - RACINEde DELTA / 2a) et (-b + RACINEdeDELTA / 2a)*

**autorisés:**  
def, if, import, return  
=, +, -, *, /, ++, ==?--?, >
math.sqrt

**attendu:**
test1 = (quadratic_equation(1, 1, -2) == [-2.0, 1.0])
test2 = (quadratic_equation(4, 4, 1) == [-0.5])
test3 = (quadratic_equation(1, 1, 1) == [])

[false, false, true, true, false, true, false, true, false, false, false] 