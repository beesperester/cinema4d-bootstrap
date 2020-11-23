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


class Monad(object):

    def __or__(self, func):
        return self.map(func)


class Either(Monad):

    def map(self, value):
        raise NotImplementedError("Map is not implemented")


class Right(Either):
    """
    This class defines the Right side of an Either Monad
    """

    def __init__(self, value):
        self.value = value

    def map(self, func):
        return func(self.value)


class Left(Either):
    """
    This class defines the Left side of an Either Monad
    """

    def __init__(self, value):
        self.value = value

    def map(self, func):
        return Left(self.value)
