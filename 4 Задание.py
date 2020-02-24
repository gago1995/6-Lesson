class Car:
    is_poliice = bool
    def __init__(self, speed, color, name, is_poliice):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_poliice = bool (is_poliice)
        self.current_speed = 0
    def go (self):
        self.current_speed = self.speed
        print(f'Машина {self.name} поехала со скоростью {self.speed}')
    def stop (self):
         self.current_speed = 0
         print(f'Машина  {self.name} остановилась')
    def turn(self):
        direction = input('В какую сторону поехала машина?')
        print(f'Машина  {self.name} поехала {direction}')
    def show_speed (self):
        print(self.current_speed)
class TownCar (Car):
    def __init__(self, speed, color, name, is_poliice):
        super().__init__(speed, color, name, is_poliice)
    def show_speed(self):
        if self.current_speed > 60:
            print(f'Скорость {self.current_speed} превышина!')
        else:
            print(self.current_speed)
class SportCar (Car):
    def __init__(self, speed, color, name, is_poliice):
        super().__init__(speed, color, name, is_poliice)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_poliice):
        super().__init__(speed, color, name, is_poliice)
    def show_speed(self):
        if self.current_speed > 40:
            print(f'Скорость {self.current_speed} превышина!')
        else:
            print(self.current_speed)
class PoliceCar (Car):
    def __init__(self, speed, color, name, is_poliice):
        super().__init__(speed, color, name, is_poliice)
a = WorkCar (50, "Белый", 'Газель', False)
a.go()
a.show_speed()
b = PoliceCar (100, 'Чёрный', 'Форд', True)
b.go()
b.show_speed()
print(f' Цвет машины {b.name}  {b.color} ')
c = TownCar (30, "Синий", 'Спринт', 0)
print(c.is_poliice)