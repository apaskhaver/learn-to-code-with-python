def length(word):
    return len(word)

print(length("Hello"))
print(length(word = "Hello"))

# print(length()) # error
# print(length(something = "Hello")) # error
# print(length(word = "Hello", something = "Goodbye")) # error

def collect_keyword_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"The key is {key}, the value is {value}")

collect_keyword_arguments(a = 2, b = 3, c = 4)
# {'a': 2, 'b': 3, 'c': 4}

def args_and_kwargs(a, b, *args, **kwargs):
    print(f"The total of your regular arguments is {a + b}") # 3
    print(f"The total of your args tuple is {sum(args)}") # 12
    print(f"The total of your kwargs dictionary is {sum(kwargs.values())}") # 27

args_and_kwargs(1, 2, 3, 4, 5, x = 8, y = 9, z = 10)