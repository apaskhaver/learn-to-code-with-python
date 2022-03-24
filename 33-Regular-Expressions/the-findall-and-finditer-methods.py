import re

pattern = re.compile("flower")

sentence = "There are a lot of flowers in a flowery flower field."

print(pattern.findall(sentence))

for match in pattern.finditer(sentence):
    print(match)
    # print(match.start())
    # print(match.end())
    # print(match.span())