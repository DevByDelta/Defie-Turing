"""
Problème 1 : Somme de tous les multiples de 5 ou de 7 inférieurs à 2013
Idée : A l'aide de boucle faire la somme des multiples de 5 puis de 7 inférieurs à 2013 puis enlever les doublons
Complexité :
Durée environ : 0.000124 s
"""

from modules.timer import timer

def sum_multiples(n, limit):
    s = 0
    i = 1
    while (n * i) < limit:
        s += n * i
        i += 1
    return s

def calc_sum_multiples2(n1, n2, limit):
    return sum_multiples(n1, limit) + sum_multiples(n2, limit) - sum_multiples(n1*n2, limit)

result, durre = timer(calc_sum_multiples2, 5, 7, 2013)

print(f"Fonction exécuté en {durre:.6f} s & résultat = {result}")

