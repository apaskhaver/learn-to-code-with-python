class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra stupid mistake.")
except StupidMistake as e:
    print(f"Caught the error. {e}")

# except won't work b/c sibling classes
# try:
#     raise StupidMistake("Extra stupid mistake.")
# except SillyMistake as e:
#     print(f"Caught the error. {e}")

# will work b/c Mistake is parent of StupidMistake
# all sibling classes to StupidMistake will be caught
# by the use of the parent in the except
try:
    raise StupidMistake("Extra stupid mistake.")
except Mistake as e:
    print(f"Caught the error. {e}")

try:
    raise SillyMistake("Super silly mistake.")
except Mistake as e:
    print(f"Caught the error. {e}")