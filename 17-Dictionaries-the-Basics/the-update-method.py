employee_salaries = {
    "Guido": 100000,
    "James": 500000,
    "Brandon": 900000
}

extra_employee_salaries = {
    "Yukihiro": 1000000,
    "Guido": 33333
}

employee_salaries.update(extra_employee_salaries)
print(employee_salaries)
print(extra_employee_salaries)

print()

even_more_employee_salaries = {
    "Ana": 400000,
    "Jerry": 300000
}

extra_employee_salaries.update(even_more_employee_salaries)
print(extra_employee_salaries)
print(even_more_employee_salaries)