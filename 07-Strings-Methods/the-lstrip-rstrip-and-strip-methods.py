empty_space = "  co nt ent       "
print(len(empty_space))

print(empty_space.rstrip())
print(len(empty_space.rstrip()))

print(empty_space.lstrip())
print(len(empty_space.lstrip()))

print(empty_space.strip())
print(len(empty_space.strip()))

website = "www.python.org"
print(website.lstrip("w")) # prints .python.org
print(website.rstrip("w")) # prints www.python.org
print(website.rstrip(".org")) # prints www.python
print(website.strip("worg.")) # deletes any of these characters coming
                              # from the left or right of the string
                              # prints python