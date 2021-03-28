from typing import List


def karate_chop(what: int, items: List[int]) -> int:
    cutting_position = int((len(items) - 1) / 2)
    value_at_cut = items[cutting_position]
    if value_at_cut == what:
        return cutting_position
    if value_at_cut < what:
        lower_range_boundary = cutting_position + 1
        return lower_range_boundary + karate_chop(what, items[lower_range_boundary:])
    if value_at_cut > what:
        upper_range_boundary = cutting_position
        return karate_chop(what, items[:upper_range_boundary])
