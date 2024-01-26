#!/usr/bin/env python3
"""
Helper function for pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for a given pagination.
    """
    return ((page_size * (page - 1)), page_size * page)
