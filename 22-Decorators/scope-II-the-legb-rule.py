# x = 15

def outer():
    # x = 10

    def inner():
        # x = 5
        # return x
        return len
    
    return inner()

# print(outer())
print(outer()("Python"))