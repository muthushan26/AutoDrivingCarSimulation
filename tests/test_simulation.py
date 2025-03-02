import unittest
from src.simulation import Simulation
from src.field import Field
from src.car import Car

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.field = Field(10, 10)
        self.simulation = Simulation(self.field)

    def test_simulation_initialization(self):
        self.assertEqual(self.simulation.field.width, 10)
        self.assertEqual(self.simulation.field.height, 10)
        self.assertEqual(len(self.simulation.cars), 0)

    def test_add_car(self):
        car = Car("A", 1, 1, "N", "FFF")
        self.simulation.add_car(car)
        self.assertEqual(len(self.simulation.cars), 1)
        self.assertEqual(self.simulation.cars[0].name, "A")

    def test_run_simulation_single_car(self):
        car = Car("A", 1, 1, "N", "FFRFF")
        self.simulation.add_car(car)
        results = self.simulation.run()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], "A, (3,3) E")

    def test_run_simulation_multiple_cars_no_collision(self):
        car1 = Car("A", 1, 1, "N", "FFRFF")
        car2 = Car("B", 5, 5, "S", "FLFLF")
        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        results = self.simulation.run()
        self.assertEqual(len(results), 2)
        self.assertIn("A, (3,3) E", results)
        self.assertIn("B, (4,3) E", results)

    def test_run_simulation_with_collision(self):
        car1 = Car("A", 1, 1, "N", "FFFFF")
        car2 = Car("B", 1, 5, "S", "FFFFF")
        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        results = self.simulation.run()
        self.assertEqual(len(results), 2)
        self.assertIn('B, collides with A at (1, 3) at step 2', results)
        self.assertIn('A, collides with B at (1, 3) at step 2', results)



    def test_run_simulation_car_reaches_boundary(self):
        car = Car("A", 0, 0, "N", "FFFFFFFFFF")
        self.simulation.add_car(car)
        results = self.simulation.run()
        self.assertEqual(results[0], "A, (0,9) N")

    def test_run_simulation_multiple_cars_no_collision(self):
        car1 = Car("A", 1, 1, "N", "FFRFF")
        car2 = Car("B", 5, 5, "S", "FLFLF")
        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        results = self.simulation.run()
        self.assertEqual(len(results), 2)
        self.assertIn("A, (3,3) E", results)
        self.assertIn("B, (6,5) N", results)

    def test_simulation_results_format(self):
        car = Car("A", 1, 1, "N", "FFRFF")
        self.simulation.add_car(car)
        results = self.simulation.run()
        self.assertRegex(results[0], r"A, \(\d+,\d+\) [NSEW]")

    def test_run_simulation_no_cars(self):
        field = Field(10, 10)
        simulation = Simulation(field)
        results = simulation.run()
        self.assertEqual(len(results), 0, "Simulation with no cars should return an empty result list")

if __name__ == '__main__':
    unittest.main()
