from abc import ABCMeta, abstractmethod
from typing import Union
from math import pi


class Figure(metaclass=ABCMeta):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def _validate_figure(self):
        pass


class Circle(Figure):
    def __init__(self, radius: Union[int, float]) -> None:
        self.radius = radius
        self._validate_figure()

    def calculate_area(self) -> float:
        area = pi * self.radius**2
        return float(f"{area:.3f}")

    def _validate_figure(self) -> None:
        if self.radius <= 0:
            raise ValueError('Radius must be positive')


class Triangle(Figure):
    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> None:
        self.a = a
        self.b = b
        self.c = c
        self._validate_figure()

    def calculate_area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return float(f"{area:.3f}")

    def _validate_figure(self) -> None:
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Sides must be positive')
        max_side = max(self.a, self.b, self.c)
        if max_side >= sum((self.a, self.b, self.c)) - max_side:
            raise ValueError('Not a triangle')

    def is_right_triangle(self) -> bool:
        leg_1, leg_2, hypotenuse = sorted((self.a, self.b, self.c))
        return leg_1**2 + leg_2**2 == hypotenuse**2


def calculate_area(*args) -> float:
    if len(args) == 1:
        return Circle(*args).calculate_area()
    elif len(args) == 3:
        return Triangle(*args).calculate_area()
    else:
        raise ValueError('Undefined type of figure. Maybe invalid number of arguments')

