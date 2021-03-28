class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.color} {self.name} went')

    def stop(self):
        print(f'The {self.color} {self.name} stopped')

    def turn(self, direction):
        print(f'The {self.color} {self.name} turned to the {direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} speed {self.speed} km per hour')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости ай-яй-яй')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости ай-яй-яй')


class PoliceCar(Car):
    pass


town_car_1 = TownCar(70, 'Yellow', 'Toyota Camry')
work_car_1 = WorkCar(41, 'Blue', 'XT3')
police_car_1 = PoliceCar(90, 'White', 'Chevrolet Bel Air', is_police=True)
sport_car_1 = SportCar(140, 'Red', 'Ferrari F40')

print(sport_car_1.color)
print(sport_car_1.name)
print(sport_car_1.speed)
print(sport_car_1.is_police)

police_car_1.go()
police_car_1.turn('left')
police_car_1.stop()
police_car_1.show_speed()
town_car_1.show_speed()
work_car_1.show_speed()
