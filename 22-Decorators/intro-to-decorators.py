def be_nice(fn):
    def inner():
        print("Nice to meet you. I'll execute your function.")
        fn()
        print("I executed it. Have a nice day.")
    
    return inner

@be_nice
def complex_business_logic():
    print("Something complex.")

@be_nice
def nonsense():
    print("Horseradish!")

# print(type(be_nice(complex_business_logic)))
# be_nice(complex_business_logic)()

complex_business_logic()
nonsense()