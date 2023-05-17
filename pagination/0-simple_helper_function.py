#!/usr/bin/env python3
"""
Function `index_range` that takes two integer arguments `page` and `page_size`
and returns a tuple containing a start index and an end index corresponding to
the range of indexes to return in a list for those particuar pagination
parameters, indexed by 1.
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that returns the start and end index for use with pagination.
    """
    return ((page - 1) * page_size + 1, page * page_size)
