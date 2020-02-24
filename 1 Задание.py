import time
class TrafficLight:
    __color = ""
    def running (self):
        print('Светофор запущен:')
        while True:
            __color = "Красный"
            print(f'Текущий цвет свтофора: {__color}')
            time.sleep(7)
            __color = "Желтый"
            print(f'Текущий цвет свтофора: {__color}')
            time.sleep(2)
            __color = "Зелёный"
            print(f'Текущий цвет свтофора: {__color}')
            time.sleep(7)
a = TrafficLight ()
a.running()