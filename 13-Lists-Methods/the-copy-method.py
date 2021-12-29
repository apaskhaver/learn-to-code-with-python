units = ["meter", "kilogram", "second", "ampere", "kelvin", "candela", "mole"]

more_units = units.copy()

units.remove("kelvin")

print(units)
print(more_units)

even_more_units = units[:]
print(even_more_units)