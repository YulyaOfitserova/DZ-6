class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует тонко')


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} нужен, чтобы обводить')


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует ярко')


pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()
