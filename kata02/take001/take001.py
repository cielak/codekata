from typing import List


def karate_chop(what: int, where: List[int]) -> int:
    cutting_position = int((len(where) - 1) / 2)
    value_at_cut = where[cutting_position]
    if value_at_cut == what:
        return cutting_position
