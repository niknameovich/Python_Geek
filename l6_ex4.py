class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = is_police

    def go(self):
        print(f'car {self.name, self.color} is riding')

    def stop(self):
        print(f'car {self.name, self.color} was stopped')

    def turn(self, direction):
        print(f'car {self.name, self.color} is turning to the {direction}')

    def show_speed(self):
        print(f'the car {self.name, self.color} has current speed = {self.speed}')


class TownCar(Car):
    limit = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > TownCar.limit:
            print(f'Danger! you force your speed limit {TownCar.limit}, current speed = {self.speed}')


class WorkCar(Car):
    limit = 40

    def show_speed(self):
        super().show_speed()
        if self.speed > WorkCar.limit:
            print(f'Danger! you force your speed limit {WorkCar.limit}, current speed = {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


mynewtowncar = TownCar(50, 'red', 'Cadillac', False)
mynewworkcar = WorkCar(50, 'grey', 'lada', False)
mynewsportcar = SportCar(50, 'red', 'Cadillac', False)
mynewpolicecar = PoliceCar(50, 'grey', 'lada', False)

mycars = [mynewworkcar, mynewtowncar, mynewpolicecar, mynewsportcar]
for car in mycars:
    if type(car) == TownCar:
        car.speed += 20
    print(f'{type(car)=}')
    car.show_speed()
