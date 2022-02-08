import random

print(random.choice(["Bob", "Moe", "Curly"]))
print(random.choice((1, 2, 3)))
print(random.choice("elephant"))

# generates a 25 element list of random numbers between 0 and 50
lottery_numbers = [random.randint(1, 50) for value in range(25)]
print(lottery_numbers)
print(random.sample(lottery_numbers, 5))