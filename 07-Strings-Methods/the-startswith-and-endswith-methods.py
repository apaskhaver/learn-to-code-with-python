salutation = "Kermit the frog"

print(salutation.startswith("K"))
print(salutation.startswith("Kermit"))
print(salutation.startswith("M"))
print(salutation.startswith("Mermit"))
print(salutation.startswith("frog")) # doesn't start with frog even if the String contains it

print()

print(salutation.endswith("g"))
print(salutation.endswith("frog"))
print(salutation.endswith("the"))