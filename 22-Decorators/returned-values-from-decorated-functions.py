def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you. I'll execute your function.")
        result = fn(*args, **kwargs)
        print("I executed it. Have a nice day.")

        return result
    
    return inner

@be_nice
def complex_business_sum(a, b):
    return a + b

print(complex_business_sum(a = 3, b = 5))