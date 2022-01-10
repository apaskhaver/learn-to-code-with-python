flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["Denver"])
# print(flight_prices["Seattle"])
# print(flight_prices["chicago"])

gym_membership_packages = {
    29: ["machines"],
    49: ["machines", "vitamin supplements"],
    79: ["machines", "vitamin supplements", "sauna"]
}

print(gym_membership_packages[29])
print(gym_membership_packages[49])
print(gym_membership_packages[79])

print(gym_membership_packages.get(29, ["basic dumbbells"]))
print(gym_membership_packages.get(100, ["basic dumbbells"]))
print(gym_membership_packages.get(100))