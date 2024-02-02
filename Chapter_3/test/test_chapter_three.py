import unittest

from Chapter_3.main import BoxWithKey


class TestChapterThree(unittest.TestCase):
    def setUp(self):
        self.check_boxes = BoxWithKey()
        while self.check_boxes.get_secret_space() == (None, None):
            self.check_boxes = BoxWithKey()

    def test_not_none(self):
        self.assertIsNotNone(self.check_boxes.get_secret_space())

    def test_find_key(self):
        self.check_boxes.look_for_key(self.check_boxes.get_boxes())
        self.assertTupleEqual(self.check_boxes.get_secret_space(), self.check_boxes.get_find_space())


if __name__ == '__main__':
    unittest.main()
