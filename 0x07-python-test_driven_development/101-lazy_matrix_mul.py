#!/usr/bin/python3
"""Defining a function that does matrix mutliplication using NumPy"""
import numpy as mp


def lazy_matrix_mul(m_a, m_b):
    return (mp.matmul(m_a, m_b))
