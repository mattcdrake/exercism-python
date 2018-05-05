def sum_of_multiples(limit, multiples):
    sumtotal = 0

    for i in range(0, limit):
        for j in multiples:
            if i % j == 0:
                sumtotal += i
                break
    
    return sumtotal
