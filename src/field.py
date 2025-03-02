class Field:
    """
    Represents the rectangular field for the auto driving car simulation.
    """

    def __init__(self, width, height):
        """
        Initialize the field with given dimensions.

        :param width: The width of the field (positive integer)
        :param height: The height of the field (positive integer)
        :raises ValueError: If width or height is not a positive integer
        """
        if width <= 0 or height <= 0:
            raise ValueError("Field dimensions must be positive integers")
        self.width = width
        self.height = height

    def is_within_bounds(self, x, y):
        """
        Check if the given coordinates are within the field boundaries.

        :param x: The x-coordinate to check
        :param y: The y-coordinate to check
        :return: True if the coordinates are within bounds, False otherwise
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def get_dimensions(self):
        """
        Get the dimensions of the field.

        :return: A tuple containing the width and height of the field
        """
        return self.width, self.height

    def __str__(self):
        """
        Return a string representation of the field.

        :return: A string in the format "Field(widthxheight)"
        """
        return f"Field({self.width}x{self.height})"
