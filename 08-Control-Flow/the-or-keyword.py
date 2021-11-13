if 5 > 8 or 7 < 11:
    print("At least one of the conditions is true. Doesn't short-circuit.")

if "cat" == "cat" or "dog" == "donkey":
    print("Short-circuits to true")

if "cat" == "cat" or "dog" == "dog":
    print("True")

if "apple" == "banana" or "orange" == "pear":
    print("Won't print, no conditions are true.")