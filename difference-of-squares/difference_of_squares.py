def square_of_sum(count):
    square = 0

    for i in range(1, count + 1):
        square += i
    
    return square ** 2


def sum_of_squares(count):
    sum_squares = 0

    for i in range(1, count + 1):
        sum_squares += i**2
    
    return sum_squares


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
