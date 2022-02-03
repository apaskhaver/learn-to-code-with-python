def divide_five_by_a_number(n):
    calculation = 0
    try:
        calculation = 5 / n
    # except ZeroDivisionError:
    #     return "You can't divide by 0."
    # except TypeError as e:
    #     return f"No dividing by invalid objects. {e}"
    except (ZeroDivisionError, TypeError) as e: 
        # assigns whichever error it was to e
        return f"Something went wrong. The error was {e}"

    return calculation

print(divide_five_by_a_number(0))
print(divide_five_by_a_number(10))
print(divide_five_by_a_number("Nonsense"))