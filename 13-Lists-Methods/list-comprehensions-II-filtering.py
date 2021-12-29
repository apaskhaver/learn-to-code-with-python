print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])

print([number / 2 for number in range(20)])

donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]
# filters list to only return donuts with "Cream" in them
print([donut for donut in donuts if "Cream" in donut])
# prints ["Boston Cream", "Vanilla Cream", "Chocolate Cream"]

# prints length of the string of each creamy donut
print([len(donut) for donut in donuts if "Cream" in donut])

# prints out the names of the creamy donuts minus the "Cream"
print([donut.split(" ")[0] for donut in donuts if "Cream" in donut])
# splits creamy donuts by space to have
# [["Boston", "Cream"], ["Vanilla", "Cream"], ["Chocolate", "Cream"]]
# Notice nested lists, because .split() returns a list. However,
# we take the first element of each of these lists, which is the
# name of the donut, without the cream, thus returning all the names
# in one unlayered list, since we indexed into the nested list.
# ["Boston", "Vanilla", "Chocolate"]