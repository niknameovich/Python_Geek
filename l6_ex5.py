class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.__class__.__name__}')
        print(f'{self.title} is drawing')


class Pen(Stationery):
    pass


class Pencil(Stationery):
    pass

class Handle(Stationery):
    pass


mynewpen = Pen('pen15')
mynewpencil = Pencil('pencil01')
mynewhandle = Handle('hndle54/51')

mystationery = [mynewpencil,mynewpen,mynewhandle]
for stat in mystationery:
    stat.draw()