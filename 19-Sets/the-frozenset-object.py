mr_freeze = frozenset([1, 2, 3, 2])
print(mr_freeze)

# mr_freeze.add(4) # error, can't mutate

regular_set = {1, 2, 3}

# print({regular_set: "Arbitrary value"}) # error, cannot use mutable set as dict key

print({mr_freeze: "Generic value"}) # works, immutable key