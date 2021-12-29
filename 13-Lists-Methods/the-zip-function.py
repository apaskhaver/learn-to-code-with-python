breakfasts = ["eggs", "cereal", "banana"]
lunches = ["sushi", "chicken teriyaki", "soup"]
dinners = ["steak", "meatballs", "pasta"]

print(zip(breakfasts, lunches, dinners))
print(list(zip(breakfasts, lunches, dinners)))

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My breakfast today was {breakfast}, my lunch was {lunch}, and my dinner was {dinner}.")