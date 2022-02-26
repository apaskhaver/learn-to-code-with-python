from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return BurritoBowl("Steak", "Rice", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1

lunch = BurritoBowl.steak_special()
print(lunch.protein)
print(lunch.guacamole_portions)
lunch.add_guac()
print(lunch.guacamole_portions)

# creates a mock that resembles the BurritoBowl class
# will have methods with matching implementations
# as the BurritoBowl class
class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)
print(class_mock.steak_special())
# below methods don't exist, runs error
# print(class_mock.chicken_special())
# print(class_mock.city)

print()

# creates a mock that resembles the BurritoBowl object
instance_mock = MagicMock(spec = BurritoBowl.steak_special())
print(instance_mock.protein)
print(instance_mock.rice)
print(instance_mock.guacamole_portions)
print(instance_mock.add_guac())
# print(instance_mock.add_cheese())
# can add new attributes
instance_mock.beans = True
print(instance_mock.beans)

stricter_instance_mock = MagicMock(spec_set = BurritoBowl.steak_special())
print(stricter_instance_mock.protein)
print(stricter_instance_mock.rice)
# not allowed to add to spec_set Mocks
# stricter_instance_mock.beans = True