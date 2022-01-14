class Guitar():
    def __init__(self, wood):
        self.wood = wood

acoustic = Guitar("alder")
electric = Guitar("mahogany")

print(acoustic.wood)
print(electric.wood)

baritone = Guitar("alder")
print(baritone.wood)

print(acoustic == baritone)
print(acoustic is baritone)