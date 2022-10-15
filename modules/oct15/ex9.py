from modules.module import Module


class Child(Module):
    name = "Индекс массы тела"
    info = "Напишите программу для вычисления индекса массы тела " \
           "(ИМТ). ИМТ = ВЕС / РОСТ2"

    def run(self, **kwargs):
        mass = float(input('mass > '))
        h = float(input("height > "))
        print(f"IMT: {mass / (h*h)}")


if __name__ == '__main__':
    Child().run()
