def contains(values, target):
    found = False
    for value in values:
        print(value)
        
        if value == target:
            found = True
            break
    return found

print(contains([1,2,3,4,5], 3))
print(contains([1,2,3,4,5], -2))