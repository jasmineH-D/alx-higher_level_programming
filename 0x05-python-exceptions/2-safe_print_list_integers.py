#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    w_p = 0
    for i in range(x):
        try:
             print("{:d}".format(my_list[i]), end="")
             w_p += 1
        except (ValueError, TypeError):
            pass
    print()
    return w_p
