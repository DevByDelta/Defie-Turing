"""
Problème 1 : Somme de tous les multiples de 5 ou de 7 inférieurs à 2013
Idée : A l'aide d'une boucle for faire la somme des multiples de 5 puis de 7 inférieurs à 2013 puis enlever les doublons
Complexité : O(n) avec n = limit
Durée environ : 0.000033 s
"""

from modules.timer import timer

def sum_multiples(n, limit):
    """Calcul la somme des multiples de n inférieur à limit"""
    s = 0
    # multiple < limit signifie multiplicateur (i) =< limit div n
    for i in range(1, (limit // n) + 1):
        s += n * i
    return s

def calc_sum_multiples2(n1, n2, limit):
    return sum_multiples(n1, limit) + sum_multiples(n2, limit) - sum_multiples(n1*n2, limit)

result, durre = timer(calc_sum_multiples2, 5, 7, 2013)

print(f"Fonction exécuté en {durre:.6f} s & résultat = {result}")

