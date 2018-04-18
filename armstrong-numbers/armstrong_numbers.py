def is_armstrong(number):
    temp_num = number
    digits = len(str(number))
    sum_digs = 0

    for i in range (0, digits):
        temp_digit = temp_num % 10
        sum_digs += temp_digit ** digits
        temp_num //= 10

    return sum_digs == number
