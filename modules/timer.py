import time

def timer(func, *args, **kwargs):
    """
    Exécute func(*args, **kwargs), renvoie la durée et le résultat de func.
    """
    
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    
    duree = end - start

    return (duree, result)
