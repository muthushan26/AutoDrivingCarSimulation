from src.user_interface import UserInterface
from src.simulation import Simulation
from src.field import Field
from src.car import Car

def main():
    """
    Main function to run the Auto Driving Car Simulation program.
    """
    print("Welcome to Auto Driving Car Simulation!")

    ui = UserInterface()
    
    while True:
        # Get field dimensions and create the field 
        field = ui.get_field_dimensions()
        simulation = Simulation(field)

        # Add cars to the simulation
        while True:
            choice = ui.get_menu_choice()
            if choice == '1':
                car = ui.add_car()
                if car:
                    simulation.add_car(car)
                else:
                    print("Failed to add car. Please try again.")
            elif choice == '2':
                # Check if there are any cars in the simulation
                if not simulation.cars:
                    print("Error: No cars in the simulation. Please add at least one car before running the simulation.")
                    continue  # Go back to the menu to add cars
                break  # Exit the car addition loop if there are cars

        # Display current cars in the simulation
        ui.display_cars(simulation.cars)

        # Run simulation
        results = simulation.run()

        # Display simulation results
        ui.display_results(results)

        # Ask user if they want to start over or exit
        if not ui.start_over():
            break

    print("Thank you for running the simulation. Goodbye!")

if __name__ == "__main__":
    main()
