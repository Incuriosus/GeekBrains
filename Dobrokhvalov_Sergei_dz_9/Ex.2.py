class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def calc_mass(self, density, thickness):
        return self._length*self._width*density*thickness


road_1 = Road(20, 5000)
print(f'{int(road_1.calc_mass(25, 5)/1000)} т.')
