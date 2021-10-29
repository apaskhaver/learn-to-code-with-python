print("This will \nbegin on a new \nline")
print("\tOnce upon a time...")
print("\"To be or not to be,\" said Hamlet")
print("\'To thine own self be true,\' said Polonius")
print("Let's print a backslash: \\") # prints \

file_name = "C:\news\travel" # will print with newline and tab; we don't want that
print(file_name)
file_name = r"C:\news\travel" # creates a raw String which is just interpreted as the characters
print(file_name)

some_random_number = 10
some_obscure_calculation = 28
some_additional_statistic_fetched_from_somewhere = 31

final = some_random_number + \
        some_obscure_calculation + \
        some_additional_statistic_fetched_from_somewhere

print(some_random_number,
      some_obscure_calculation, 
      some_additional_statistic_fetched_from_somewhere)