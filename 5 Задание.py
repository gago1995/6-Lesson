class Stationery:
    def __init__(self, title ):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen (Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw (self):
        print('Запуск отрисовки ручки')
class Pencil (Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Запуск отрисовки карандаша')
class Handle (Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Запуск отрисовки маркера')
a = Stationery ('Скрепки')
a.draw()
b = Pen ('Ручка синяя')
b.draw()