class Store():
    def __init__(self):
        self.owner = "Boris"

    def exclaim(self):
        return "Lots of stuff to buy! Come inside!"

class CoffeeShop(Store):
    pass

starbucks = CoffeeShop()

print(starbucks.owner)
print(starbucks.exclaim())