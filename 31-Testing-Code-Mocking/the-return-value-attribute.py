from unittest.mock import Mock

mock = Mock()
print(mock)

print(mock()) # new Mock object
# return_value configures the above to return a specific value. 
# Right now same as above.
print(mock.return_value) 

print()

mock.return_value = "25"
print(mock()) # 25 

# return_value can also be set in the Mock constructor
mock = Mock(return_value = 19)
print(mock()) # 19 

print()
print()

# can also set the return_value on nested mock attributes
# (since nested mock attributes are other mock objects with
# return_value property).
# Now whenever stuntman's METHODS are called
# not just stuntman()
# those methods will have return_values we set!
stuntman = Mock()
stuntman.jump_off_building.return_value = "Oh no, my leg!"
stuntman.light_on_fire.return_value = "It burns!"

# calling the methods
print(stuntman())
print(stuntman.jump_off_building())
print(stuntman.light_on_fire())

# if we don't call the methods with (),
# we'll just get a Mock object representing the method
print(stuntman.jump_off_building)