class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes.")

    def store(self):
        print("Putting in the freezer!")

class Dessert():
    def add_weight(self):
        print("Putting on the pounds!")

    def store(self):
        print("Putting in the refrigerator.")

class IceCream(FrozenFood, Dessert):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)
ic.store() # will run FrozenFood's store method, b/c FrozenFood class
           # is inherited first in the order the IceCream class is declared
           # FrozenFood, Dessert <-- so FrozenFood methods accessed first.
           # Unless, of course, IceCream has a store() method, in which case
           # IceCream obj would access its own method first.

# Order of accesses
print(IceCream.mro()) # '__main__.FrozenFood'>, <class '__main__.Dessert'>, <class 'object'>]
