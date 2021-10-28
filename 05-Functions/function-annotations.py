def word_multiplier(word: str, repeats: int) -> str:
    return word * repeats
print(word_multiplier("Watson", 3)) # prints WatsonWatsonWatson
print(word_multiplier(1, 5)) # will return 6 because function annotations don't raise errors