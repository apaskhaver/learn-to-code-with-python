filename = "my_first_file.txt"

with open(filename, "w") as file_object:
    file_object.write("Hello!\n")
    file_object.write("I'm a file.\n")