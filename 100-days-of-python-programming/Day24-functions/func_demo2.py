def is_even(number):
    if type(number) == int:
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Not allowed"