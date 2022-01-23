# If a class defines neither a __bool__ nor a __len__ magic method,
# the object will be considered truthy.

class NoBoolOrLen():
    def __init__(self):
        pass

nbol = NoBoolOrLen()

if nbol:
    print("truthy") # truthy
    