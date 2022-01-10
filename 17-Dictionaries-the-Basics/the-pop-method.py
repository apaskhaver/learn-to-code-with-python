release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

print(release_dates.pop("Java"))
print(release_dates)

print(release_dates.pop("Go"))
print(release_dates)

if "Rust" in release_dates:
    release_dates.pop("Rust")

print(release_dates.pop("C++", 2000))

del(release_dates["Python"])
print(release_dates)

# del(release_dates["Swift"]) # runs an error, "Swift" doesn't exist in release_dates