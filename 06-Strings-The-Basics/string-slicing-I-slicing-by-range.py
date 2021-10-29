address = "Attractive Street, Beverly Hills, CA 90210"
print(address[0:3])
print(address[0:4])
print(address[0:17])
print(address[19:32])
print(address[-100:100])

print("\n")

print(address[34:-6])
print(address[-8:-6])
print(address[-8:36])

print("\n")

print(address[3: ])
print(address[15: ])
print(address[-10: ])

print("\n")

print(address[ :5])
print(address[ :-14])

print("\n")

print(address[ : ])

print(len(address))
print(address[43:44]) # prints a blank b/c out of String's indexes, but won't run an error