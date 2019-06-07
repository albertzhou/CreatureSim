import numpy as np


class Point:

    xCoord = None
    yCoord = None

    def __init__(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord

    # p2 - p1, returns the vector between the two points
    @staticmethod
    def normalized_vector(p2, p1):

        diff_vector = [p2.xCoord - p1.xCoord, p2.yCoord - p1.yCoord]
        length = np.linalg.norm([diff_vector[0], diff_vector[1]])

        return diff_vector/length