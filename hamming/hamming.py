def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError("DNA strands are of different length")
    
    distance = 0
    index = 0

    while (index < len(strand_a)):
        if strand_a[index] != strand_b[index]:
            distance += 1
        index += 1
    
    return distance
