import unittest
from src.car import Car

class TestCar(unittest.TestCase):

    def test_car_initialization(self):
        car = Car("A", 1, 2, "N", "FFRFF")
        self.assertEqual(car.name, "A")
        self.assertEqual(car.x, 1)
        self.assertEqual(car.y, 2)
        self.assertEqual(car.direction, "N")
        self.assertEqual(car.commands, "FFRFF")
        self.assertFalse(car.collided)

    def test_car_movement(self):
        car = Car("B", 5, 5, "N", "")
        car.move(10, 10)
        self.assertEqual((car.x, car.y), (5, 6))
        
        car.direction = "E"
        car.move(10, 10)
        self.assertEqual((car.x, car.y), (6, 6))
        
        car.direction = "S"
        car.move(10, 10)
        self.assertEqual((car.x, car.y), (6, 5))
        
        car.direction = "W"
        car.move(10, 10)
        self.assertEqual((car.x, car.y), (5, 5))

    def test_car_rotation(self):
        car = Car("C", 0, 0, "N", "")
        car.rotate("R")
        self.assertEqual(car.direction, "E")
        car.rotate("R")
        self.assertEqual(car.direction, "S")
        car.rotate("L")
        self.assertEqual(car.direction, "E")

    def test_car_boundary_movement(self):
        car = Car("D", 0, 0, "S", "")
        car.move(10, 10)
        self.assertEqual((car.x, car.y), (0, 0))
        
        car.direction = "W"
        car.move(10, 10)
        self.assertEqual((car.x, car.y), (0, 0))

    def test_execute_single_command(self):
        car = Car("E", 1, 1, "N", "")
        car.execute_command("F", 10, 10)
        self.assertEqual((car.x, car.y), (1, 2))
        car.execute_command("R", 10, 10)
        self.assertEqual(car.direction, "E")

    def test_execute_command_sequence(self):
        car = Car("F", 1, 1, "N", "FFRFF")
        for cmd in car.commands:
            car.execute_command(cmd, 10, 10)
        self.assertEqual((car.x, car.y), (3, 3))
        self.assertEqual(car.direction, "E")

    def test_collision_status(self):
        car = Car("G", 1, 1, "N", "")
        self.assertFalse(car.is_collided())
        car.set_collided()
        self.assertTrue(car.is_collided())

    def test_car_string_representation(self):
        car = Car("H", 3, 4, "W", "")
        self.assertEqual(str(car), "H, (3,4) W")

if __name__ == '__main__':
    unittest.main()
