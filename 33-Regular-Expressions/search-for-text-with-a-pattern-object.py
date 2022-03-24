import re

pattern = re.compile("flower")

print(type(pattern))

print(pattern.search("candy"))

# match = pattern.search("flower power")

match = pattern.search("a red flower in the field")
# match = pattern.search("no matches here")

print(type(match))

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())