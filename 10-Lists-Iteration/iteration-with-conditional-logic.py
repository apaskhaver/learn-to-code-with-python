values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odds_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total

print(odds_sum(values))
print(odds_sum(other_values))

def greatest_numbers(numbers):
    greatest = numbers[0]

    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(greatest_numbers([1, 2, 3]))
print(greatest_numbers([-5, 2, 3, -10, 399]))
print(greatest_numbers([-5, -4, -3]))