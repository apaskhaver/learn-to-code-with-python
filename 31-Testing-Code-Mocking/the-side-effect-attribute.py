from subprocess import call
from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10)

call_me_maybe = Mock()
print(call_me_maybe.side_effect)
# None b/c no side_effect defined

call_me_maybe.side_effect = generate_number
print(call_me_maybe.side_effect())
print(call_me_maybe())
# random number b/c side_effect assigned to generate_number function
# and was called with (). If you didn't use parens, just returns
# the function

# can also use constructor
call_me_maybe = Mock(side_effect = generate_number)
print(call_me_maybe())

call_me_maybe.return_value = 10
print(call_me_maybe()) 
# side_effect wins out when both it and return_value are defined

print()
print()

three_item_list = Mock()

# setting the invented pop attribute to a method through side_effect
three_item_list.pop.side_effect = [3, 2, 1, IndexError("Popping from empty list")]
print(three_item_list.pop()) # 3
print(three_item_list.pop()) # 2
print(three_item_list.pop()) # 1
# print(three_item_list.pop()) # IndexError w/ error method

print()
print()

mock = Mock(side_effect = NameError("Some error message"))
# print(mock()) # error

mock.side_effect = None
print(mock())
# prints default new Mock object