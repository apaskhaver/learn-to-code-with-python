from types import BuiltinFunctionType


def outer():
    bubble_tea_flavor = "black"

    def inner():
        nonlocal bubble_tea_flavor
        bubble_tea_flavor = "taro"
    
    inner() # if inner not run, outer() returns black

    return bubble_tea_flavor

print(outer()) # prints taro