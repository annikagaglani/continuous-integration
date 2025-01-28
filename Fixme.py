#!/usr/bin/python3

def factorial(n):
    '''
    Returns the product of all numbers from 1 to n.

    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(40)
    815915283247897734345611269596115894272000000000
    >>> factorial(400)
    640345228466238952623479703195030058507025830260029594586844459428023971691
    '''
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def triangular(n):
    '''
    Returns the nth triangular number.

    The nth triangular number is the sum of all numbers from 1 to n.
    It is like the factorial, but uses addition instead of multiplication.

    >>> triangular(1)
    1
    >>> triangular(2)
    3
    >>> triangular(3)
    6
    >>> triangular(4)
    10
    >>> triangular(40)
    820
    >>> triangular(400)
    80200
    '''
    result = 1
    for i in range(2, n + 1):
        result += i
    return result
