#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        newlist = list()
        resultt = 0
        for i in range(0, list_length):
            try:
                resultt = my_list_1[i] / my_list_2[i]
            except TypeError:
                print("wrong type")
                resultt = 0
            except ZeroDivisionError:
                resultt = 0
                print("division by 0")
            except IndexError:
                resultt = 0
                print("out of range")
            finally:
                newlist.append(resultt)
        return newlis
