from modules.module import Module


class Child(Module):
    name = "Существует ли треугольник?"
    info = " Напишите программу, чтобы проверить," \
           " могут ли три заданные длины сторон " \
           "(целые числа) образовать треугольник или нет."

    def run(self, **kwargs):
        a = float(input("a > "))
        b = float(input("b > "))
        c = float(input("c > "))
        if (a < b+c) and (b < a+c) and (c < a+b):
            print("Треугольник существует")
        else:
            print("Нет такого треугольника")


if __name__ == '__main__':
    Child().run()
