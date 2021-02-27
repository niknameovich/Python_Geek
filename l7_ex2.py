from abc import ABC, abstractmethod
from math import ceil


class Clothes:
    def __init__(self, catalogname):
        self.name = catalogname

    @abstractmethod
    def tissue_consump(self):
        pass


class Suit(Clothes):
    def __init__(self, catalogname, size):
        self.size = float(size)
        super().__init__(catalogname)

    @property
    def tissue_consump(self):
        return ceil(self.size / 6.5 + 0.5)


class Costume(Clothes):
    def __init__(self, catalogname, height):
        self.height = float(height)
        super().__init__(catalogname)

    @property
    def tissue_consump(self):
        return ceil(2 * self.height + 0.3)


totalconsump = 0
mynewclothes = [Costume('bergeron', 5.8), Suit('camber', 27.5)]
for mnclothe in mynewclothes:
    print(mnclothe.tissue_consump)
    totalconsump += mnclothe.tissue_consump
print(f'{totalconsump=} m2')
