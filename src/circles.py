from math import pi


class Circles:
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    def area(self) -> float:
        """
        calculate the area of the circle
        @throws Exception if radius > 0
        """
        if self.validate():
            return pi * self.radius**2
        else:
            raise Exception("radius < 0")

    def circumference(self) -> float:
        """
        calculate the circumference of the circle
        @throws Exception if radius > 0
        """
        if self.validate():
            return 2 * pi * self.radius
        else:
            raise Exception("radius < 0")

    def validate(self) -> bool:
        return True if self.radius > 0 else False
