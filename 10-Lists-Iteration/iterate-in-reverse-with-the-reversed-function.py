the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
print(the_simpsons[::-1])

for character in the_simpsons[::-1]:
    print(f"{character} is {len(character)} letters long")

print(reversed(the_simpsons))
print(type(reversed(the_simpsons)))

for character in reversed(the_simpsons):
    print(f"{character} is {len(character)} letters long")