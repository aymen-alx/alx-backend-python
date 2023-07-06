#!/usr/bin/env python3
""" Doc """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return length of list
    """
    return [(i, len(i)) for i in lst]
