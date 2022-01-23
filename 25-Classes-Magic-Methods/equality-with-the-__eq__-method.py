class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    
    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other):
        return self.grades == other.grades

bob = Student(90, 90, 90)
moe = Student(100, 90, 80)
joe = Student(40, 45, 50)

print(bob.grades)
print(moe.grades)
print(joe.grades)

print()

print(bob == moe)
print(moe == bob)
print(bob == joe)
print(moe == joe)

print(bob != joe)