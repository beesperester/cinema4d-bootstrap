"""
This module provides methods for working with pipes
"""

from functools import reduce


class Pipe(object):
    """
    This class defines a pipe like list of actions that are executed
    in order
    """

    def __init__(self, items):
        self.items = items

    def __call__(self, value):
        def reducer(a, b):
            return a.map(b)

        return reduce(reducer, [value] + self.items)


class Right(object):
    """
    This class defines the Right side of a monad
    """

    def __init__(self, value):
        self.value = value

    def map(self, method):
        return method(self.value)


class Left(object):
    """
    This class defines the Left side of a monad
    """

    def __init__(self, value):
        self.value = value

    def map(self, method):
        return Left(self.value)
