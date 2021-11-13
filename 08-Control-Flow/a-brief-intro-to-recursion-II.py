def reverse(str):
    new_string = ""
    index = len(str) - 1

    while index >= 0:
        new_string += str[index]
        index -= 1
    
    return new_string

print(reverse("straw"))

print()

def reverse_recursive(str):
    if len(str) <= 1:
        return str

    return str[-1] + reverse(str[0: -1])

print(reverse_recursive("straw"))
print(reverse_recursive("racecar"))
print(reverse_recursive("General Washington"))