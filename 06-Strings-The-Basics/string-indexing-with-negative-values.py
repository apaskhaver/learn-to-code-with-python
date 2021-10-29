print("cat"[-1])

topic = "programming"

print(topic[-1])
print(topic[-2])
print(topic[-5])

# not out of bounds because negative indexes start counting at -1, not 0
print(topic[-len(topic)])