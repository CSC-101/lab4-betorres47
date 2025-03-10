import math

import data
from data import Point

# Write your functions for each part in the space below.

# Part 1

def first_element(lst: list[list[int]]) -> list[list[int]]:
    lst = filter(lambda x: len(x) > 0, lst)             # remove any list that does is not complete

    return [x[0] for x in lst]                          # create and return list that has

# Part 2

def x_coordinates(lst: list[Point]) -> list[float]:
    return list(map(lambda point: point.x, lst))                            # create a new list with every that takes the point.x value from point to create a list

# Part 3

def are_in_positive_quadrant(lst: list[Point]) -> list[Point]:
    return list(filter(lambda point: point.x > 0 and point.y > 0, lst))     # verifies both x and y components are positive; filter negative values

# Part 4

def distance_between_points_e(p1 :Point, p2: Point) -> float:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)               # finds the Euclidian distance using Pythagorean's theorem

# Part 5

def distance_between_points_m(p1 :Point, p2: Point) -> float:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)                              # finds the Manhattan distance formula

# Part 6

def distance_from_origin(p :Point) -> float:
    return math.sqrt(p.x ** 2 + p.y ** 2)                                   # finds the Euclidian distance using Pythagorean's theorem

def distance_all(lst = list[Point]) -> list[float]:
    return list(map(distance_from_origin, lst))                             # finds distance for all points in the list and creates new list w filter

