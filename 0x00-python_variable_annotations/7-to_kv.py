#!/usr/bin/env python3
""" Doc """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Type-annotated function 'to_kv' tat takes
    """
    return (k, v * v)
