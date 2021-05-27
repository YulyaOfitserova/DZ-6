from time import sleep

class TrafficLight:

    __colors = {'red': 7, 'yellow': 2, 'green': 7}

    def running(self):
        for color, sec in self.__colors.items():
            self.__color = color
            print(f'горит {self.__color} в течение {sec} сек')
            sleep(sec)


light = TrafficLight()
light.running()
