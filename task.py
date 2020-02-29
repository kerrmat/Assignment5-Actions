import math


def firstrun():
    return "success"


def computearea(radius):
    return math.pow(radius, 2) * math.pi


def getelements(input):
    return [input[0], input[len(input)-1]]


def daysbetween(date1, date2):
    difference = date1 - date2
    return abs(difference.days)
