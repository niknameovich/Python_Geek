from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, longtitude: int):
        self.__color = ''
        self.mode = {'red': longtitude, 'yellow': longtitude // 3, 'green': longtitude * 2}

    def running(self):
        for key, time in cycle(self.mode.items()):
            self.__color = key
            print(f'{self.__color=} wait time = {time}')
            sleep(time)


mynewtraffic = TrafficLight(7)
mynewtraffic.running()
