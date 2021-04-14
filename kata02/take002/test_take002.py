import pytest

from take002 import karate_chop


class TestBinarySearch:
    def test_finds_single_item(self):
        assert karate_chop(5, [5]) == 0

    def test_finds_first_of_two(self):
        assert karate_chop(1, [1, 2]) == 0

    @pytest.mark.xfail
    def test_finds_second_of_two(self):
        assert karate_chop(1, [-2, 1]) == 1

    @pytest.mark.xfail
    def test_finds_first_of_three(self):
        assert karate_chop(1, [1, 2, 3]) == 0

    @pytest.mark.xfail
    def test_finds_middle_of_three(self):
        assert karate_chop(4, [1, 4, 8]) == 1

    @pytest.mark.xfail
    def test_finds_third_of_three(self):
        assert karate_chop(6, [2, 4, 6]) == 2

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        "item_to_find, item_position",
        ((12, 0), (24, 1), (35, 2), (43, 3), (55, 4), (63, 5), (77, 6), (80, 7)),
    )
    def test_finds_one_of_eight(self, item_to_find, item_position):
        assert (
            karate_chop(item_to_find, [12, 24, 35, 43, 55, 63, 77, 80]) == item_position
        )

    @pytest.mark.skip(reason="big range crashes")
    @pytest.mark.parametrize("item", (0, 1, 50000000, 100000000))
    def test_finds_in_big_range(self, item):
        assert karate_chop(item, list(range(100000001))) == item
