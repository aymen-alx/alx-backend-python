#!/usr/bin/env python3
"""  """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Type-annotated function 'make_multiplier' that takes
    """
    def myFunc(num: float) -> float:
        return multiplier * num
    return myFunc
