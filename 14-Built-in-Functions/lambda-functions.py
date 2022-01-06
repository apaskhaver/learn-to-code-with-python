metals = ["gold", "silver", "platinum", "palladium"]
print(list(filter(lambda metal: len(metal) > 5, metals)))
# will print ["silver", "platinum", "palladium"]

print(list(filter(lambda word: "p" in word, metals)))

print(list(map(lambda word: word.count("l"), metals)))
print(list(map(lambda word: word.replace("s", "$"), metals)))