# Все принты для наглядности
import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self, green_time, rounds):
        for _ in range(rounds):
            self.__color = 'Red'
            print('Горит красный')
            time.sleep(7)
            self.__color = 'Yellow'
            print('Горит желтый')
            time.sleep(2)
            self.__color = 'Green'
            print('Горит зеленый')
            time.sleep(green_time)
            print('---')
        self.__color = None


light = TrafficLight()
light.running(5, 2)
