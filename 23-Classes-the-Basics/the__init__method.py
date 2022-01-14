class Guitar():
    def __init__(self):
        print(f"A new guitar has been created. This object is {self}")

acoustic = Guitar()
print(acoustic) 
# prints the same memory location as __init__
# because it references the same object

electric = Guitar()
print(electric)