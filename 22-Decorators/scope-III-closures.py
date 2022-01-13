def outer():
    candy = "Snickers"

    def inner():
        return candy

    return inner # returns the inner function

the_function = outer() # the_function now assigned to inner function
# All local variables declared inside outer will be garbage-collected
# But the_function has a reference to inner so we can still use it.

print(the_function()) # prints Snickers