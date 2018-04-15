# Score categories
# Change the values as you see fit
YACHT = "Yacht"
ONES = "Ones"
TWOS = "Twos"
THREES = "Threes"
FOURS = "Fours"
FIVES = "Fives"
SIXES = "Sixes"
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Four of a Kind"
LITTLE_STRAIGHT = "Little Straight"
BIG_STRAIGHT = "Big Straight"
CHOICE = "Choice"


def score(dice, category):
    if category == YACHT:
        return check_yacht(dice)
    elif category == ONES:
        return check_digit(dice, 1)
    elif category == TWOS:
        return check_digit(dice, 2)
    elif category == THREES:
        return check_digit(dice, 3)
    elif category == FOURS:
        return check_digit(dice, 4)
    elif category == FIVES:
        return check_digit(dice, 5)
    elif category == SIXES:
        return check_digit(dice, 6)
    elif category == FULL_HOUSE:
        return check_full_house(dice)
    elif category == FOUR_OF_A_KIND:
        return check_four_kind(dice)
    elif category == LITTLE_STRAIGHT:
        return check_little_straight(dice)
    elif category == BIG_STRAIGHT:
        return check_big_straight(dice)
    elif category == CHOICE:
        return check_choice(dice)
    
    return 0

def check_yacht(dice):
    digit = dice[0]

    for die in dice:
        if die != digit:
            return 0
    
    return 50

def check_digit(dice, digit):
    total = 0

    for die in dice:
        if die == digit:
            total += 1

    return total * digit

def check_full_house(dice):
    digit_one = dice[0]
    digit_two = 0
    one_count = 0
    two_count = 0

    for die in dice:
        if die == digit_one:
            one_count += 1
        elif die == digit_two:
            two_count += 1
        elif digit_two == 0:
            digit_two = die
            two_count += 1
        else:
            return 0
    
    if (one_count == 3 and two_count == 2) or (one_count == 2 and two_count == 3):
        return one_count * digit_one + two_count * digit_two

    return 0

def check_four_kind(dice):
    val_counts = { 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    
    for die in dice:
        val_counts[die] += 1
        if val_counts[die] == 4:
            return die * 4
    
    return 0

def check_little_straight(dice):
    val_counts = { 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for die in dice:
        val_counts[die] += 1
    
    if val_counts[1] == 1 and val_counts[2] == 1 and \
        val_counts[3] == 1 and val_counts[4] == 1 and \
        val_counts[5] == 1 and val_counts[6] == 0:
        return 30
    
    return 0

def check_big_straight(dice):
    val_counts = { 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for die in dice:
        val_counts[die] += 1
    
    if val_counts[1] == 0 and val_counts[2] == 1 and \
        val_counts[3] == 1 and val_counts[4] == 1 and \
        val_counts[5] == 1 and val_counts[6] == 1:
        return 30
    
    return 0

def check_choice(dice):
    vals_sum = 0

    for die in dice:
        vals_sum += die
    
    return vals_sum