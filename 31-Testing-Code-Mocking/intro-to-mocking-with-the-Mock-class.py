from unittest.mock import Mock

# not a real Pizza object, but has attributes
pizza = Mock()
print(pizza)
print(type(pizza))

pizza.size = "large"
pizza.price = 19.99
pizza.toppings = ["pepperoni", "mushroom", "sausage"]

# can also do
pizza.configure_mock(
    size = "large",
    price = 19.99,
    toppings = ["pepperoni", "mushroom", "sausage"]
)
# the above is an actual method

print(pizza.size)
print(pizza.price)
print(pizza.toppings)

# if an attribute "does not exist" on the Mock object,
# it doesn't run an error. It supplies new Mock objects
# that take the place of the attributes. 
# Any attribute you can dream of will exist on pizza.
print(pizza.anything)
print(pizza.nonsense)
print(pizza.anything) # only dynamically created the first time
print(pizza.anything.we.want) # nested structure of mock objects dynamically created

# invoking any method at all on a mock object returns another mock object
print(pizza.cover_with_cheese())
print(pizza.cover_with_cheese())