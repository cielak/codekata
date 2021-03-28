from take001 import karate_chop


class TestBinarySearch:
    def test_finds_single_item(self):
        assert karate_chop(5, [5]) == 0
