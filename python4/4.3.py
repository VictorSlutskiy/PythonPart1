class Stationary:
    title = "название"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationary):
    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationary):
    def draw(self):
        print("Отрисовка маркером")


stationary = Stationary()
stationary.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
