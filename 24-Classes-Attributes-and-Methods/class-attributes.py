class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"New number of counter objects created: {cls.count}")
        # can do cls.count b/c the Counter class is represented by cls

        return two_counters
    
print(Counter.count) # 0
c1 = Counter()
print(Counter.count) # 1

# assigning each element in the list to a var
c2, c3 = Counter.create_two()
print(Counter.count) # 3

print()

# each instance of the class has access to count variable
# reference the same obj in memory.
print(c1.count) # 3
print(c2.count) # 3
print(c3.count) # 3