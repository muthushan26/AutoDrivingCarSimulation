from src.car import Car
from src.field import Field

class Simulation:
    """
    Manages the core logic of the Auto Driving Car Simulation.
    """

    def __init__(self, field):
        """
        Initialize the simulation with a given field.

        :param field: A Field object representing the simulation area
        """
        self.field = field
        self.cars = []

    def add_car(self, car):
        """
        Add a car to the simulation.

        :param car: A Car object to be added to the simulation
        """
        self.cars.append(car)

    def run(self):
        """
        Execute the simulation for all cars.

        This method processes all commands for each car, checks for collisions,
        and ensures cars stay within the field boundaries.

        :return: A list of strings representing the final states or collision results of all cars
        """

        if not self.cars:
            return []

        results = []
        max_steps = max(len(car.commands) for car in self.cars)
        
        for step in range(max_steps):
            positions = {}
            for car in self.cars:
                if car.is_collided() or step >= len(car.commands):
                    continue
                
                command = car.commands[step]
                car.execute_command(command, self.field.width, self.field.height)
                
                position = car.get_position()
                if position in positions:
                    other_car = positions[position]
                    car.set_collided()
                    other_car.set_collided()
                    results.append(f"{car.name}, collides with {other_car.name} at {position} at step {step + 1}")
                    results.append(f"{other_car.name}, collides with {car.name} at {position} at step {step + 1}")
                else:
                    positions[position] = car
        
        # Add final positions of non-collided cars to results
        for car in self.cars:
            if not car.is_collided():
                results.append(str(car))
        
        return results
