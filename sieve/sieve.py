def sieve(limit):
    primes = []

    if limit < 2:
        return primes
    
    marked = {}

    for i in range(2, limit + 1):
        if i not in marked:
            primes.append(i)
            j = 2
            
            while i * j < limit + 1:
                marked[i * j] = True
                j += 1
    
    return primes   
