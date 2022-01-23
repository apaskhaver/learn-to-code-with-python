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

    def __gt__(self, other):
        return self.grades > other.grades

    def __ge__(self, other):
        return self.grades >= other.grades

    def __lt__(self, other):
        return self.grades < other.grades

    def __lt__(self, other):
        return self.grades <= other.grades
    
    def __add__(self, other):
        return self.grades + other.grades
    
    def __sub__(self, other):
        return self.grades - other.grades

bob = Student(90, 90, 90)
moe = Student(100, 90, 80)
joe = Student(40, 45, 50)

print(moe > joe)
print(joe <= bob)
print(bob + moe)
print(moe - joe)