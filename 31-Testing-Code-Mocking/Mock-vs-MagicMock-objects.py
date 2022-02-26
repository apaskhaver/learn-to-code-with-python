from pydoc import plain
from unittest.mock import Mock, MagicMock

plain_mock = Mock()
magic_mock = MagicMock()

# print(len(plain_mock)) # error, doesn't support __len__
print(len(magic_mock))

# print(plain_mock[3]) # error, doesn't support iteration, __getitem__
print(magic_mock[3]) # returns an item, the same item
print(magic_mock[100]) 
print(magic_mock["hello"]) 

print(magic_mock.__len__) # Mock obj
print(magic_mock.__len__())
magic_mock.__len__.return_value = 50
print(magic_mock.__len__())

if magic_mock:
    print("magic_mock is truthy by default")

# setting truthiness to false
magic_mock.__bool__.return_value = False
if magic_mock:
    print("Won't print, made false.")

magic_mock.__getitem__.return_value = 100
print(magic_mock[1])
print(magic_mock[2])
print(magic_mock[3])