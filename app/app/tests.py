"""
Sample tests
"""
from django.test import SimpleTestCase  # SimpleTestCase: no db integration

from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """test subtracting"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, -5)
