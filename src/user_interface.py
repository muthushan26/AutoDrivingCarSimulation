from src.car import Car
from src.field import Field
from src.car import Car

class UserInterface:
    """
    Handles all user interactions for the auto driving car simulation.
    """

    def get_field_dimensions(self):
        """
        Prompts the user to enter field dimensions and validates the input.

        :return: A tuple containing the width and height of the field as positive integers
        """
        print("\nPlease enter the width and height of the simulation field in x y format:")
        while True:
            try:
                width, height = map(int, input().split())
                if width > 0 and height > 0:
                    return Field(width, height)
                else:
                    print("Dimensions must be positive integers. Please try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

    def get_menu_choice(self):
        """
        Displays the main menu and prompts the user to make a choice.

        :return: A string '1' or '2' representing the user's choice
        """
        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        while True:
            choice = input()
            if choice in ['1', '2']:
                return choice
            print("Invalid choice. Please enter 1 or 2.")

    def add_car(self):
        """
        Prompts the user to enter details for a new car and creates a Car object.

        :return: A Car object with the user-specified attributes, or None if input is invalid
        """
        print("Please enter the name of the car:")
        name = input().strip()
        
        while True:
            print(f"Please enter initial position of car {name} in x y Direction format:")
            try:
                x, y, direction = input().split()
                x, y = int(x), int(y)
                if direction not in ['N', 'S', 'E', 'W']:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter two integers and a direction (N, S, E, W) separated by spaces.")
        
        print(f"Please enter the commands for car {name}:")
        commands = input().strip().upper()
        
        # Validate commands
        if not all(cmd in 'FLR' for cmd in commands):
            print("Invalid commands. Only F, L, and R are allowed. Please try again.")
            return None

        return Car(name, x, y, direction, commands)

    def display_cars(self, cars):
        """
        Displays the list of cars currently in the simulation.

        :param cars: A list of Car objects
        """
        print("\nYour current list of cars are:")
        for car in cars:
            print(f"- {car}, {car.commands}")

    def display_results(self, results):
        """
        Displays the results of the simulation.

        :param results: A list of strings representing the simulation results
        """
        print("\nAfter simulation, the result is:")
        for result in results:
            print(f"- {result}")

    def start_over(self):
        """
        Prompts the user to choose between starting over or exiting the program.

        :return: True if the user wants to start over, False if they want to exit
        """
        print("\nPlease choose from the following options:")
        print("[1] Start over")
        print("[2] Exit")
        while True:
            choice = input()
            if choice == '1':
                return True
            elif choice == '2':
                return False
            print("Invalid choice. Please enter 1 or 2.")
