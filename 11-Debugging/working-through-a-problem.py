# Define a function that iterates over a list of numbers,
# multiplies each number by one less than its index position
# and returns the total sum of these products

def multiply_by_one_less_than_index(numbers):
    total = 0

    for index, number in enumerate(numbers):
        total += number * (index - 1)
    return total

print(multiply_by_one_less_than_index([1, 2, 3, 4, 5]))