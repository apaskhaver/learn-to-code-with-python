if 3:
    print("Will print, truthy")

if -1:
    print("Also will print, truthy")

if 0:
    print("Won't print, falsy")

if "hello":
    print("lalala")

if "":
    print("Will this print?") # No

print(bool(1))
print(bool(0))
print(bool(""))
print(bool(" "))
print(bool("aaifhwi"))
print(bool(12.201))
print(bool(0.0))