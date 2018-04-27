def slices(series, length):
    if length <= 0 or length > len(series) or len(series) == 0:
        raise ValueError("bad data")

    outlist = []
    counter = 0

    while counter + length <= len(series):
        inner_count = counter
        temp_list = []
        for i in range(inner_count, inner_count + length):
            temp_list.append(int(series[i]))
        outlist.append(temp_list)
        counter += 1
    
    return outlist