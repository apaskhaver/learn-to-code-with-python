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
print(bbq.size) # attr exists

stats_to_delete = ["size", "diameter", "spiciness", "ingredients"]

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)

# print(bbq.size) # attr deleted, no longer exists