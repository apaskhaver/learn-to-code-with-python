def sum_of_positive_values(values):
    total = 0

    for value in values:
        if value > 0:
            total += value

    return total

print(sum_of_positive_values([1, 2, -3, 4]))

def sum_of_positive_values2(values):
    total = 0

    for value in values:
        if value < 0:
            continue
        
        # this line is only reached if the above if statement is false
        # ergo, the value is positive
        total += value

    return total

print(sum_of_positive_values2([1, 2, -3, 4]))