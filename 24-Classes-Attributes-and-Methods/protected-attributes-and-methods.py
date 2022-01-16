class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware
    
    def update_firmware(self):
        print("Reaching out to the server for the next version.")
        self._firmware += 1

iPhone = SmartPhone()
# print(iPhone._company) # protected, shouldn't be directly accessed
# print(iPhone._firmware)

print(iPhone.get_os_version())
iPhone.update_firmware()
print(iPhone.get_os_version())