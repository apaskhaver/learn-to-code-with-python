if 5 < 7 and "rain" == "rain":
    print("Both true")

if 5 < 7 and "rain" == "fire":
    print("Won't print b/c one condition is false")

if "rain" == "fire" and 5 < 7:
    print("Short-circuited b/c first statement is false")

if "rain" == "fire" and 5 < 3:
    print("Also short-circuited")

value = 95

if value > 90 and value < 100:
    print("Valid syntax")

if 90 < value < 100:
    print("Shortcut for above")

