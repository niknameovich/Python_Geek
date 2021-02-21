from math import ceil


class ROAD:

    def __init__(self, length: float, width: float):
        self._length = abs(length)
        self._width = abs(width)
        self.weight = 0

    def __str__(self):
        return f'length={self._length} m, width={self._width} m, totalweight={self.weight} t'

    def calcweght(self, weightpermeter: float, thickness: float):
        return ceil(self._length * self._width * weightpermeter * thickness)


mynewroad = ROAD(100.75, 10.12)
mynewroad.weight = mynewroad.calcweght(10, 15.7)
print(mynewroad)
