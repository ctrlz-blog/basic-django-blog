import unittest

from blog import utils


class TestResizeImage(unittest.TestCase):
    def test_get_new_image_dimensions(self):

        original = (400, 200)
        new_width = 200
        expected = (200, 100)

        actual = utils.get_new_image_dimensions(original, new_width)

        self.assertEqual(expected, actual)

    def test_original_dimensions_returned(self):
        """Tests that the original dimensions are returned if the
        original dimensions are smaller than the new width (we don't
        want to enlarge images)"""

        original = (400, 200)
        expected = original
        actual = utils.get_new_image_dimensions(original, 500)

        self.assertEqual(expected, actual)
