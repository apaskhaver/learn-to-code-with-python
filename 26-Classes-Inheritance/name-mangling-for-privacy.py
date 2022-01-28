class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some_method")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()

# None of these accesses work b/c the attributes have
# been mangled to different names
# print(n.__some_attribute)
# print(n.some_attribute)
# print(sn.__some_attribute)
# print(sn.some_attribute)
# print(n.__some_method())
# print(sn.__some_method())

# name mangling changes the names to
# _NameOfClassmethod-right-after
print(n._Nonsense__some_attribute)
n._Nonsense__some_method()
print(sn._Nonsense__some_attribute)
sn._Nonsense__some_method()