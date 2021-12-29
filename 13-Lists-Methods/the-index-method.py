pizzas = [
    "Mushroom",
    "Pepperoni",
    "Sausage",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage",
]

print(pizzas.index("Barbecue Chicken"))
print(pizzas.index("Pepperoni"))
print(pizzas.index("Sausage"))

if "Olive" in pizzas:
    print(pizzas.index("Olive"))

print(pizzas.index("Pepperoni", 2))
print(pizzas.index("Sausage", 3))