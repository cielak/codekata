from take001 import karate_chop


class TestBinarySearch:
    def test_finds_single_item(self):
        assert karate_chop(5, [5]) == 0

    def test_finds_first_of_two(self):
        assert karate_chop(1, [1, 2]) == 0

    def test_finds_second_of_two(self):
        assert karate_chop(1, [-2, 1]) == 1

    def test_finds_middle_item(self):
        assert karate_chop(4, [1, 4, 8]) == 1
