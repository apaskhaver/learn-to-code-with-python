class Teacher():
    def teach_class(self):
        print("Teaching stuff...")
    
    def grab_lunch(self):
        print("Yum, yum, yum.")

    def grade_tests(self):
        print("F, F, F!")

class CollegeProfessor(Teacher):
    def publish_book(self):
        print("Hurrah, I'm an author!")

    def grade_tests(self):
        print("A, A, A!")

t = Teacher()
t.teach_class()
t.grab_lunch()
t.grade_tests()

print()

cp = CollegeProfessor()
cp.teach_class()
cp.grab_lunch()
cp.grade_tests()
cp.publish_book()