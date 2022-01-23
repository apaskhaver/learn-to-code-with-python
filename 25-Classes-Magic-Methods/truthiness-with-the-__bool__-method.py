class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity
    
    def __bool__(self):
        return self.positivity > self.negativity
    
my_emotional_state = Emotion(50, 75)

if my_emotional_state:
    print("Won't print, more negative than positive.")

my_emotional_state.positivity = 100

if my_emotional_state:
    print("This will print because I have more positivity than negativity.")
