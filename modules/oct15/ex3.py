from random import randint

from modules.module import Module


class Child(Module):
    name = "Наибольшие элементы массива"
    info = "Напишите программу для поиска k " \
           "самых больших элементов в заданном " \
           "массиве. Элементы в массиве могут " \
           "располагаться в любом порядке."

    def run(self, **kwargs):
        mas = input("mas (r for random) > ")
        if mas == 'r':
            mas = []
            for a in range(100):
                mas.append(randint(-1000, 1000))
        else:
            mas = list(map(lambda x: int(x), mas.split(" ")))


        mas.sort(reverse=True)
        print(mas[:(int(input("k > ")))])


if __name__ == '__main__':
    Child().run()
