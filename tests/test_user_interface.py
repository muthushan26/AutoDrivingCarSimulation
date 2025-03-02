import unittest
from unittest.mock import patch
from io import StringIO
from src.user_interface import UserInterface
from src.car import Car

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = UserInterface()

    @patch('builtins.input', side_effect=['5 5'])
    def test_get_field_dimensions_valid(self, mock_input):
        field = self.ui.get_field_dimensions()
        self.assertEqual(field.width,5)
        self.assertEqual(field.height,5)

    @patch('builtins.input', side_effect=['invalid', '-1 5', '5 5'])
    def test_get_field_dimensions_invalid(self, mock_input):
        field = self.ui.get_field_dimensions()
        self.assertEqual(field.width,5)
        self.assertEqual(field.height,5)

    @patch('builtins.input', side_effect=['1'])
    def test_get_menu_choice_valid(self, mock_input):
        choice = self.ui.get_menu_choice()
        self.assertEqual(choice, '1')

    @patch('builtins.input', side_effect=['3', '2'])
    def test_get_menu_choice_invalid(self, mock_input):
        choice = self.ui.get_menu_choice()
        self.assertEqual(choice, '2')

    @patch('builtins.input', side_effect=['A', '1 2 N', 'FFRFF'])
    def test_add_car_valid(self, mock_input):
        car = self.ui.add_car()
        self.assertIsInstance(car, Car)
        self.assertEqual(str(car), "A, (1,2) N")

    @patch('builtins.input', side_effect=['B', 'invalid', '1 2 X', '1 2 N', 'FFRFF'])
    def test_add_car_invalid_inputs(self, mock_input):
        car = self.ui.add_car()
        self.assertIsInstance(car, Car)
        self.assertEqual(str(car), "B, (1,2) N")

    def test_display_cars(self):
        cars = [Car("A", 1, 2, "N", "FFRFF"), Car("B", 3, 4, "S", "FLFL")]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_cars(cars)
            self.assertIn("A, (1,2) N, FFRFF", fake_out.getvalue())
            self.assertIn("B, (3,4) S, FLFL", fake_out.getvalue())

    def test_display_results(self):
        results = ["A, (3,3) E", "B collided with C at (2,2)"]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_results(results)
            self.assertIn("A, (3,3) E", fake_out.getvalue())
            self.assertIn("B collided with C at (2,2)", fake_out.getvalue())

    @patch('builtins.input', side_effect=['1'])
    def test_start_over_true(self, mock_input):
        self.assertTrue(self.ui.start_over())

    @patch('builtins.input', side_effect=['2'])
    def test_start_over_false(self, mock_input):
        self.assertFalse(self.ui.start_over())

if __name__ == '__main__':
    unittest.main()
