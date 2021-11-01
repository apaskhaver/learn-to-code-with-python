story = "once upon a time"

print(story.capitalize())
print(story.title())
print(story.upper())
print("HELLO".lower())
print("AbCdE".swapcase())
print("BENJAMIN FRANKLIN".lower().title()) # prints "Benjamin Franklin"
print(story) # doesn't change story variable

story = story.capitalize().swapcase()
print(story)