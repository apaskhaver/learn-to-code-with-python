candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Reeses Pieces", "Mars Bars", "Snickers"}

print(candy_bars.symmetric_difference(sweet_things))
print(candy_bars ^ candy_bars) # everything in common so empty set
print(sweet_things ^ candy_bars)