# # name, adjective, noun
# mad_libs = "{} laughed at the {} {}."
# # prints Bobby laughed at the green alien
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Jennifer", "silly", "tomato"))
# print(mad_libs.format("Jennifer", "silly", "tomato", "bunnies"))

# mad_libs = "{0} laughed at the {1} {2}."
# # prints Bobby laughed at the green alien
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Jennifer", "silly", "tomato", "bunnies"))

# mad_libs = "{2} laughed at the {1} {0}."
# # prints tomato laughed at the silly Jennifer
# print(mad_libs.format("Jennifer", "silly", "tomato"))

# mad_libs = "{name} laughed at the {adjective} {noun}."
# # prints tomato laughed at the silly Jennifer
# print(mad_libs.format(name = "Jennifer", adjective = "silly", noun = "tomato"))
# # order doesn't matter now
# print(mad_libs.format(adjective = "silly", name = "Jennifer", noun = "tomato"))

madlibs = "{name} laughed at the {adjective} {noun}"
name = input("Please enter a name: ")
adjective = input("Please enter an adjective: ")
noun = input("Please enter a noun: ")
# Python makes the distinction between keywords and variable names
print(madlibs.format(name = name, adjective = adjective, noun = noun))