import unittest
from src.field import Field


class TestField(unittest.TestCase):

    def test_field_initialization(self):
        field = Field(10, 15)
        self.assertEqual(field.width, 10)
        self.assertEqual(field.height, 15)

    def test_is_within_bounds(self):
        field = Field(5, 5)
        self.assertTrue(field.is_within_bounds(0, 0))
        self.assertTrue(field.is_within_bounds(4, 4))
        self.assertFalse(field.is_within_bounds(5, 5))
        self.assertFalse(field.is_within_bounds(-1, 0))

    def test_get_dimensions(self):
        field = Field(7, 8)
        width, height = field.get_dimensions()
        self.assertEqual(width, 7)
        self.assertEqual(height, 8)

    def test_string_representation(self):
        field = Field(3, 4)
        self.assertEqual(str(field), "Field(3x4)")

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            Field(0, 5)
        with self.assertRaises(ValueError):
            Field(5, -1)
