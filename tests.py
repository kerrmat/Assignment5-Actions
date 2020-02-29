import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        radius = 2
        expected = math.pi * math.pow(radius, 2)
        self.assertEqual(expected, task.computearea(radius))

    def test4(self):
        radius = 2
        expected = 6
        self.assertNotEqual(expected, task.computearea(radius))

    def test5(self):
        input = [1,2,3,4,5]
        expected = [1,5]
        self.assertEqual(expected, task.getelements(input))

    def test6(self):
        input = [1,2,3,4,5]
        expected = [1,4]
        self.assertNotEqual(expected, task.getelements(input))


if __name__ == '__main__':
    unittest.main()
