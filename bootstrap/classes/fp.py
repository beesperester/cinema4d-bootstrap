"""
This module provides methods for working with pipes
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
    def func_encased(value):
        try:
            return Right(func(value))
        except Exception as e:
            return Left(e)

    return func_encased


def pipe(items):
    def callback(value):
        def reducer(a, b):
            return a.map(b)

        return reduce(reducer, [value] + items)

    return callback


def chain(func):
    def callback(value):
        return func(Right(value))

    return callback


if __name__ == "__main__":
    pipe1 = pipe([
        encase(lambda x: x + 1)
    ])

    pipe2 = pipe([
        encase(lambda x: x * 2)
    ])

    result = pipe([
        chain(pipe1),
        chain(pipe2)
    ])(Right(1))

    print(result)
