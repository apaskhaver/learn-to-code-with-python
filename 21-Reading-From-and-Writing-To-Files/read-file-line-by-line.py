with open("cupcakes.txt") as file_object:
    for line in file_object:
        # print(line)

        # print includes a line break,
        # so this just removes the regular
        # line breaks in the file to format
        # everything a bit truer to the
        # actual cupcakes.txt
        print(line.rstrip())