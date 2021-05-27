class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'{self.speed} текущая скорость авто'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} - слишком большая скорость для городского авто'
        else:
            return f'{self.speed} текущая скорость авто'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} - слишком большая скорость для рабочего авто'
        else:
            return f'{self.speed} текущая скорость авто'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def ispolice(self):
        if self.is_police:
            return f'{self.name} - это полицейская машина'
        else:
            return f'{self.name} - это не полицейская машина'


auto1 = TownCar(70, 'red', 'Lada', True)
auto2 = WorkCar(50, 'white', 'Vaz', True)
auto3 = SportCar(200, 'green', 'Ferrari', False)
auto4 = PoliceCar(80, 'black', 'Ford', False)
print(auto1.go())
print(auto1.show_speed())
print(auto2.show_speed())
print(auto4.ispolice())
print(auto2.turn_left())
print(auto2.stop())
print(auto3.turn_right())
