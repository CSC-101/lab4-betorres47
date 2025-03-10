import math

import data
import lab4
import unittest
from data import Point



# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)              # expected: [1, 3], actual: [1, 3]

    def test_first_element_2(self):
        input = [[9,1], [0, 1]]
        result = lab4.first_element(input)
        expected = [9, 0]
        self.assertEqual(expected, result)              # expected [9, 0], actual [9, 0]

    # Part 2

    def test_x_coordinates1(self):
        points = [Point(1, 2), Point(3, 4), Point(5, 6)]
        result = lab4.x_coordinates(points)
        expected = [1, 3, 5]
        self.assertEqual(expected, result)              # expected [1, 3, 5], actual [1, 3, 5]

    def test_x_coordinates2(self):
        points = [Point(9, 1)]
        result = lab4.x_coordinates(points)
        expected = [9]
        self.assertEqual(expected, result)              # expected [9], actual [9]

    # Part 3

    def test_are_in_positive_quadrant(self):
        points = [Point(1, 2), Point(-3, 4), Point(5, -6), Point(7, 8), Point(-2, -3)]
        assert lab4.are_in_positive_quadrant(points) == [Point(1, 2), Point(7, 8)], "Test 1 failed"

        # Test case 2: No points in the first quadrant
        points = [Point(-1, -2), Point(-3, -4), Point(0, 5), Point(6, 0)]
        assert lab4.are_in_positive_quadrant(points) == [], "Test 2 failed"
                                                        # we check a set of 2 lists with random values containing points which have negative and zero values to handle tests

    # Part 4

    def test_distance_between_points(self):
        assert lab4.distance_between_points_e(Point(0, 0), Point(3, 4)) == 5.0, "Test 2 failed"

        assert lab4.distance_between_points_e(Point(1, 1), Point(4, 5)) == 5.0, "Test 2 failed"
                                                        #  above is a different way test our expected and actual values using a simple 3-4-5 right triangle which should give 5

    # Part 5

    def test_manhattan_distance(self):
        assert lab4.distance_between_points_m(Point(0, 0), Point(3, 4)) == 7, "Test 1 failed"


        assert lab4.distance_between_points_m(Point(-1, -1), Point(2, 3)) == 7, "Test 2 failed"
                                                        # above are 2 tests to verify the manhattan distance formula is working using another 3-4-5 triangle which should give 7

    # Part 6

    def test_distance_all(self):
        points = [Point(-3, -4), Point(1, 1), Point(2, 2)]
        assert lab4.distance_all(points) == [5.0, math.sqrt(2), math.sqrt(8)], "Test 1 failed"

        points = [Point(3, 4), Point(6, 8), Point(0, 0)]
        assert lab4.distance_all(points) == [5.0, 10.0, 0.0], "Test 2 failed"
                                                        # using some common triangles (1-1-sqrt2, 3-4-5, 6-8-10, and 2-2-sqrt8) we verify the function returns the right floats




if __name__ == '__main__':
    unittest.main()
