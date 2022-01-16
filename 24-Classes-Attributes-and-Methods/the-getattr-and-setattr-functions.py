stats = {
    "name": "barbecue chicken",
    "price": 19.99,
    "size": "extra-large",
    "ingredients": ["chicken", "onions", "barbecue sauce"]
}

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)

bbq = Pizza(stats)
print(bbq.size)
print(bbq.ingredients)

print()

for attr in ["price", "name", "diameter", "discounted"]:
    print(getattr(bbq, attr, "unknown"))