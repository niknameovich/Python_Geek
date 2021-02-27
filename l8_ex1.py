import random

# класс генератор карточек лото
class CardGenerator:
    cardrows = 3
    cardcolumns = 9
    maxnuminrow = 5
    maxnum = 90
    columnwidth = 5

    def __init__(self):
        self.cardlist = []
        notexecutednums = range(1, CardGenerator.maxnum + 1)
        i = 0
        while i < CardGenerator.cardrows:
            previous = None
            placement = CardGenerator.generateseq(range(1, CardGenerator.cardcolumns + 1), CardGenerator.maxnuminrow)
            placement.sort()
            currentseq = CardGenerator.generateseq(notexecutednums, CardGenerator.maxnuminrow)
            currentseq.sort()
            self.cardlist.append({key: value for key, value in zip(placement, currentseq)})
            notexecutednums = set(notexecutednums) - set(currentseq)
            i += 1

    def __str__(self):
        i = 0
        j = 0
        result = '_' * CardGenerator.cardcolumns * CardGenerator.columnwidth + '\n'
        while i < CardGenerator.cardrows:
            while j < CardGenerator.cardcolumns:
                result += (str(self.cardlist[i][j + 1]).rjust(len(str(CardGenerator.maxnum)), ' ')
                           if self.cardlist[i].keys().__contains__((j + 1))
                           else ' ').ljust(CardGenerator.columnwidth, ' ')
                j += 1
            result += '\n'
            i += 1
            j = 0
        result += '_' * CardGenerator.cardcolumns * 5 + '\n'
        return result

# метод проверки текущего номера в розыгрыше
    def checknum(self, num):
        result = -1
        for row in self.cardlist:
            for key, value in row.items():
                if value == num:
                    return key
        return result

# статический метод генерации последовательностей заданной размерности
    @staticmethod
    def generateseq(columns, count):
        return random.sample(columns, count)

# класс игрока, имеющий атрибут со ссылкой на карточку лотто
class Player:

    def __init__(self, name):
        self.name = name
        self.lotocard = CardGenerator()


# метод для взаимодействия с пользователем для принятия решения по текущему номеру
    def makedecision(self, num, auto=True):
        i = 0
        if not auto:
            if input(f'Зачеркнуть номер {num} в карточке игрока {self.name} : y/n?') == 'y':
                yesno = True
            else:
                yesno = False
        else:
            yesno = True
        fkey = self.lotocard.checknum(num)
        try:
            if (fkey != -1) & yesno:
                while i < len(self.lotocard.cardlist):
                    if self.lotocard.cardlist[i].keys().__contains__(fkey):
                        if self.lotocard.cardlist[i][fkey] == num:
                            self.lotocard.cardlist[i][fkey] = '-'
                            break
                    i += 1
            elif (fkey == -1) & (not yesno):
                pass
            else:
                if not auto:
                    raise NotImplementedError
        except NotImplementedError:
            print(f'player {self.name} is loose')
            raise NotImplementedError
        finally:
            print(f'{self.name} \n {self.lotocard}')


lotobag = list(range(1, CardGenerator.maxnum+1))
p1 = Player('user')
p2 = Player('PC')
print(f'{p1.name} \n {p1.lotocard} \n {p2.name} \n {p2.lotocard} \n Начало игры')
while True:
    try:
        currentnum = random.sample(lotobag, 1).pop()
        p1.makedecision(currentnum, False)
        p2.makedecision(currentnum)
        lotobag.remove(currentnum)
    except NotImplementedError:
        break
