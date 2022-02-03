def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("One or both of the values are invalid. Both numbers must be positive.")
        
        return a + b
    except ValueError as e:
        return f"Caught the ValueError: {e}"

print(add_positive_numbers(10, 5))
print(add_positive_numbers(-2, 3))
print(add_positive_numbers(5, -8))
# Below two statements print
# Caught the ValueError: 
# One or both of the values are invalid. Both numbers must be positive.
# Notice it's our custom error message from inside the try block.
