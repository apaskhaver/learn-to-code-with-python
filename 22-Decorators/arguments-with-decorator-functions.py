def be_nice(fn):
    def inner(*args, **kwargs):
        # converts any arguments into a tuple, args, and a 
        # dictionary, kwargs

        print("Nice to meet you. I'll execute your function.")
        # args and kwargs above are destructured into
        # values. "Inverse" of what happened above.
        fn(*args, **kwargs)
        print("I executed it. Have a nice day.")
    
    return inner

@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Something complex for {position} {stakeholder}.")

# all below work
complex_business_logic("Alex", "Manager")
complex_business_logic("Alex", position = "Manager")
complex_business_logic(stakeholder = "Alex", position = "Manager")