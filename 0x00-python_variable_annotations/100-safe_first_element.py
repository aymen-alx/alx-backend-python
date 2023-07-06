#!/usr/bin/env python3
"""  """
from typing import Mapping, Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first itemof lst
    """
    if lst:
        return lst[0]
    else:
        return None
