#!/usr/bin/python3

def safe_print_division(a, b):
    resultt = 0
    try:
        resultt = a / b
    except ZeroDivisionError:
        resultt = None
    finally:
        print("Inside result: {}".format(resultt))
    return resultt
