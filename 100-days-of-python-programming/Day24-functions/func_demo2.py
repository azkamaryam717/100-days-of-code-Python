def is_even(number):
    if type(number) == int:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")