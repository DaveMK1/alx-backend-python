#!/usr/bin/env python3
'''Contains a function that sums a list of floats
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))
