class OrganicCeil:
    def __init__(self, ceilcount=0):
        self.ceilcount = ceilcount

    def __add__(self, other):
        return OrganicCeil(self.ceilcount + other.ceilcount)

    def __sub__(self, other):
        return OrganicCeil(self.ceilcount - other.ceilcount) if self.ceilcount > other.ceilcount else print \
            ('Wrong genetic operation')

    def __mul__(self, other):
        return OrganicCeil(self.ceilcount * other.ceilcount)

    def __truediv__(self, other):
        return OrganicCeil(round(self.ceilcount / other.ceilcount))

    def make_order(self, rows):
        result = '\n'.join(['*' * rows for rng in range(self.ceilcount // rows)])
        result += '\n' + '*' * (self.ceilcount % rows)
        return result


geneticexperiment = [OrganicCeil(10)]
geneticexperiment.append(geneticexperiment[-1] - OrganicCeil(4))
geneticexperiment.append(geneticexperiment[-1] / OrganicCeil(10))
geneticexperiment.append(geneticexperiment[-1] * OrganicCeil(8))

for mnceil in geneticexperiment:
    print(f'experiment {geneticexperiment.index(mnceil)}')
    print(mnceil.make_order(len(geneticexperiment)))
