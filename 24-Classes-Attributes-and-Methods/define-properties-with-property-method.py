class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12
    
    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

    # creates a property called feet for any Height object
    # feet is the name we will use to access the property
    feet = property(_get_feet, _set_feet)

h = Height(5)
print(h.feet) # 5.0, property feet calls _get_feet

h.feet = 6 # property calls _set_feet
print(h.feet) # 6.0

h.feet = -10 # validation in _set_feet means nothing changes
print(h.feet) # 6.0