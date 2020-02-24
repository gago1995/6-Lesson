class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calculating_mass(self):
        mass = self._length * self._width * 25
        print(f'Масса асфальта для дроги длинной: {self._length} м.'
              f' и шириной: {self._width} м. составит:{mass} кг.')
a = Road (10, 5)
a.calculating_mass()