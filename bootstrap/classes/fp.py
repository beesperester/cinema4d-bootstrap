"""
This module provides methods for working in functional programming style
"""

import traceback
from functools import reduce


class Monad(object):
    """
    This class defines a Monad
    """

    def __init__(self, value):
        self.value = value

    def __or__(self, func):
        return self.map(func)

    def __str__(self):
        return "{}({})".format(
            self.__class__.__name__,
            str(self.value)
        )


class Either(Monad):
    """
    This class defines an Either Monad
    """

    def map(self, value):
        raise NotImplementedError("Map is not implemented")


class Right(Either):
    """
    This class defines the Right side of an Either Monad
    """

    def map(self, func):
        return func(self.value)


class Left(Either):
    """
    This class defines the Left side of an Either Monad
    """

    def map(self, func):
        return Left(self.value)


def encase(func):
    """
    This function wraps a method that might fail and turns it into
    either Right or Left monads
    """
    def func_encased(value):
        try:
            return Right(func(value))
        except Exception as e:
            return Left(e)

    return func_encased


def pipe(items):
    """
    This function creates a pipe in which functions are applied in order
    """
    def callback(value):
        def reducer(a, b):
            return a.map(b)

        return reduce(reducer, [value] + items)

    return callback


def chain(func):
    """
    This function adds chaining capabilities to pipes
    """
    def callback(value):
        return func(Right(value))

    return callback
