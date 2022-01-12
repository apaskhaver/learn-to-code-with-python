agents = {"Mulder", "Scully", "Doggett", "Reyes"}

agents.remove("Doggett")
print(agents)

# agents.remove("Skinner") # runs an error, Skinner not in the set

agents.discard("Reyes")
agents.discard("Skinner") # no error, even though Skinner's not in the set
print(agents)