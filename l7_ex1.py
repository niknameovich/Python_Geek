class Matrix:

    def __init__(self, currrent_matrix: list):
        self.current = list()
        if len(currrent_matrix) > 0:
            for mrow in currrent_matrix:
                self.current.append(list(map(int, mrow)))

    def __str__(self):
        result = ''
        for row in self.current:
            for el in [f'{x} ' for x in row]:
                result += el
            result += '\n'
        return result

    def __add__(self, other):
        result = Matrix('')
        try:
            if len(self.current) == len(other.current):
                for tosum, summable in zip(self.current, other.current):
                    if len(tosum) == len(summable):
                        result.current.append(list(map(lambda x, y: x + y, tosum, summable)))
                    else:
                        raise NotImplementedError
            else:
                raise NotImplementedError
        except NotImplementedError:
            print('Wrong summable matrix')
        return result


mynewmatrix = Matrix([['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3']])
print(mynewmatrix)
nm = mynewmatrix + Matrix([['9', '9', '9'], ['10', '10', '10'], ['0', '0', '0']])
print(nm)
