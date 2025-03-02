class Car:
    def __init__(self, name, x, y, direction, commands):
        """
        Initialize a new Car object.

        :param name: A string representing the car's name
        :param x: An integer representing the car's initial x-coordinate
        :param y: An integer representing the car's initial y-coordinate
        :param direction: A string ('N', 'S', 'E', or 'W') representing the car's initial direction
        :param commands: A string of commands ('F', 'L', 'R') for the car to execute
        """
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.collided = False

    def move(self, field_width, field_height):
        """
        Move the car one step in its current direction, if within field boundaries.

        :param field_width: The width of the field
        :param field_height: The height of the field
        """
        if self.direction == 'N' and self.y < field_height - 1:
            self.y += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'E' and self.x < field_width - 1:
            self.x += 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def rotate(self, command):
        """
        Rotate the car based on the given command.

        :param command: 'L' for left rotation, 'R' for right rotation
        """
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        if command == 'L':
            self.direction = directions[(current_index - 1) % 4]
        elif command == 'R':
            self.direction = directions[(current_index + 1) % 4]

    def execute_command(self, command, field_width, field_height):
        """
        Execute a single command.

        :param command: 'F' for forward, 'L' for left rotation, 'R' for right rotation
        :param field_width: The width of the field
        :param field_height: The height of the field
        """
        if command == 'F':
            self.move(field_width, field_height)
        elif command in ['L', 'R']:
            self.rotate(command)

    def __str__(self):
        """
        Return a string representation of the car.

        :return: A string in the format "name, (x,y) direction"
        """
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"

    def get_position(self):
        """
        Get the current position of the car.

        :return: A tuple (x, y) representing the car's position
        """
        return (self.x, self.y)

    def set_collided(self):
        """
        Mark the car as collided.
        """
        self.collided = True

    def is_collided(self):
        """
        Check if the car has collided.

        :return: Boolean indicating whether the car has collided
        """
        return self.collided
