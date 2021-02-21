class Worker:
    incomekeys = ('wage', 'bonus')

    def __init__(self, name, surname, position, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def __setattr__(self, key, value):
        if key == '_income':
            if type(value) == dict:
                    super().__setattr__(key, value)
            else:
                print('Wrong type of income detected')
        else:
            super().__setattr__(key, value)


class Position(Worker):

    def get_full_name(self):
        return f'{self.surname, self.name, self.position}'

    def get_total_income(self):
        total = 0
        for key in super().incomekeys:
            total += self._income[key]
        return total

    def __str__(self):
        return f'{self.get_full_name()} , total income = {self.get_total_income()}'


mynewposition = Position('Vasya', 'Pupkin', 'head of r&d', {Worker.incomekeys[0]: 100, Worker.incomekeys[1]: 50})
print(mynewposition)
