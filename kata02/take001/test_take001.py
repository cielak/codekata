from take001 import karate_chop


class TestBinarySearch:
    def test_finds_single_item(self):
        assert karate_chop(5, [5]) == 0

    def test_finds_middle_item(self):
        assert karate_chop(4, [1, 4, 8]) == 1
