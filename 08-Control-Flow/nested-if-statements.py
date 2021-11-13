ingredient1 = "pasta"
ingredient2 = "sausage"

if ingredient1 == "pasta":
    if ingredient2 == "meatballs":
        print("Make pasta with meatballs!")
    else:
        print("Make plain pasta")
else:
    print("No recipe recommendations")

if ingredient1 == "pasta" and ingredient2 == "meatballs":
    print("Make pasta with meatballs!")
elif ingredient1 == "pasta": # don't need to bother to check ingredient2, the only way we get here is if ingredient2 != "meatballs"
    print("Make plain pasta")
else:
    print("No recipe recommendations")