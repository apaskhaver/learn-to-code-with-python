class Guitar():
    def __init__(self):
        print(f"A new guitar has been created. This object is {self}")

acoustic = Guitar()
electric = Guitar()


# BAD PRACTICE BELOW
# (Better to set attributes in the __init__ method)
acoustic.wood = "mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

print(acoustic.wood)
print(electric.nickname)

# Inconsistent design: we don't know if all guitar types have a
# .nickname or .wood, and this will lead to errors if we try to 
# access such attributes on the wrong guitar. Guitars should 
# behave similarly. Hence, set attributes in __init__.