class Worker:

    def __init__(self, name, surname, position, _wage, _bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": _wage, "bonus": _bonus}


class Position(Worker):

    def __init__(self, name, surname, position, _wage, _bonus):
        super().__init__(name, surname, position, _wage, _bonus)

    def get_full_name(self):
        return f'Сотрудник фирмы (должность {self.position}) {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход в этом месяце {sum(self._income.values())}'


employee = Position('Yulya', 'Ofitserova', 'teacher', 20, 30)
print(employee.get_full_name())
print(employee.get_total_income())
