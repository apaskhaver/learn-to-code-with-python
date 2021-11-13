def count_down_from(number):
    while number > 0:
        print(number)
        number -= 1

count_down_from(10)

print()

def count_down_from_recursive(number):
    if number <= 0:
        return

    print(number)

    count_down_from_recursive(number - 1)

count_down_from_recursive(10)