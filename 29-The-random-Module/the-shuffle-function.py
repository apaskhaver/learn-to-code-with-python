import random
import copy

characters = ["Warrior", "Druid", "Hunter", "Rogue", "Mage"]

# all shallow copies; don't work for nested lists.
# for nested lists, do copy.deepcopy()
clone = characters[:]
clone = characters.copy()
clone = copy.copy(characters)

print(random.shuffle(clone)) # None
print(clone) # new order
print(characters) # original order