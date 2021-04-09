"""
Generates permutations.
"""

from typing import Sequence, List, Iterator


def permutations(max_val: int) -> Iterator[Sequence[int]]:
    """
    Generate permutations of 0 to (max_val - 1)
    """
    # developer assertion.
    assert max_val > 0  # nosec

    available: List[List[int]] = []
    current: List[int] = []
    # Initialize the data
    next_list: List[int] = []
    for i in range(max_val):
        next_list.append(i)
    available.append(next_list)

    while len(available) > 0:
        next_list = available.pop()
        if not next_list:
            if current:
                current.pop()
            continue
        current.append(next_list[0])
        if len(current) >= max_val:
            yield list(current)
        available.append(next_list[1:])
        next_list = []
        for i in range(max_val):
            if i not in current:
                next_list.append(i)
        available.append(next_list)
