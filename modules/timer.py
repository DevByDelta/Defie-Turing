import time

def timer(func, *args, **kwargs):
    """
    Exécute func(*args, **kwargs), renvoie le résultat de func et la durée.
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    
    duration = end - start

    return (result, duration)


def test_rapide(func, *args, **kwargs):
    """
    Faire rapidement des test sur le temps d'exécution des fonctions.
    Affiche le message contenant la durée et le résultat
    """
    result, duration = timer(func, *args, **kwargs)
    print(f"Le programme a durée {duration:.6f} s")
    print(f"Le résultat du programme : {result}")