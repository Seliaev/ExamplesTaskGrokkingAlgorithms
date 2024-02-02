import unittest

from Chapter_4.devide_and_rule import DevideAndRule


class TestChapterThreeDAR(unittest.TestCase):
    def setUp(self):
        self.size_field_x = 1680
        self.size_field_y = 640
        self.object_dar = DevideAndRule(field=(self.size_field_x, self.size_field_y))

    def test_find_size_square(self):
        self.assertEqual(self.object_dar.get_max_sq(), 80)



if __name__ == '__main__':
    unittest.main()
