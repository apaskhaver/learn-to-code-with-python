print("ABC", "CDE", "FGH")
print("ABC", "CDE", "FGH", sep=" ")

print("ABC", "CDE", "FGH", sep="!")
print("ABC", "CDE", "FGH", "!")

print("ABC", "CDE", "FGH", sep="--*--")

print("Hello")
print("Hello", end="\n")
print("Hello", "Goodbye", end="!!!!")
# note that the end of the previous statement does not have a newline,
# hence this statement comes directly following the previous one.
print("A", "B", "C", sep="**", end="#\n")
print("A", "B", "C", sep="#", end="**")