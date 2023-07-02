#!/usr/bin/python3
"""Defining text printing function"""


def text_indentation(text):
    index = 0
    if type(text) != str:
        raise TypeError("text must be a string")

    while index < len(text) and text[index] == ' ':
        index++

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index++
            while index < len(text) and text[index] == ' ':
                index++
            continue
        index++
