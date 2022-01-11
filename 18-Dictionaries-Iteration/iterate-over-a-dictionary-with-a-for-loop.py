chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Ribs": 7.99,
    "Fried Rice": 1.99
}

for food in chinese_food:
    print(f"The food is {food} and its price is ${chinese_food[food]}")

print()

pounds_to_kilograms = {
    5: 2.26796,
    10: 4.53592,
    25: 11.3398
}

for pound in pounds_to_kilograms:
    print(f"{pound} pounds is {pounds_to_kilograms[pound]} kilograms.")