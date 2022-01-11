college_courses = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Einstein"
}

print(type(college_courses.items()))

for key, value in college_courses.items():
    print(f"The course {key} is being taught by {value}")

for _, value in college_courses.items():
    print(f"The next professor is {value}")