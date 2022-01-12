creator = "Alex"
PI = 3.14159
calculator = "meta"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def area(radius):
    return PI * radius * radius

print(__name__)

if __name__ == "__main__":
    # does something only if file is run as a script
    print("This will only run when module is executed as a script")
    print(subtract(3, 5))

_year = 2022