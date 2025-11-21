import time

def timer(func, *args, **kwargs):
    """
    Exécute func(*args, **kwargs), renvoie le résultat de func et la durée.
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    
    duree = end - start

    return (result, duree)
