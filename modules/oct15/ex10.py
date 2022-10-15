from modules.module import Module


class Child(Module):
    name = "Квадрат, Куб и дальше"
    info = "Напишите, которая считывает число " \
           "и отображает квадрат, куб и четвертую степень."
    def run(self, **kwargs):
        a = float(input("a > "))
        print(a, a*a, a*a*a, a*a*a*a)


if __name__ == '__main__':
    Child().run()
