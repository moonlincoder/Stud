from random import randint
from modules.module import Module


class Child(Module):
    name = "Числа больше среднего в массиве"
    info = "Напишите программу для поиска чисел, " \
           "превышающих среднее значение чисел данного массива."

    def run(self, **kwargs):

        mas = input("mas (r for random) > ")
        if mas == 'r':
            mas = []
            for a in range(100):
                mas.append(randint(-1000, 1000))
        else:
            mas = list(map(lambda x: int(x), mas.split(" ")))

        s = 0
        for a in mas:
            s += a

        print("median: ", s/len(mas))
        for m in mas:
            if m > s / len(mas):
                print(m, end=" ")
        print()


if __name__ == '__main__':
    Child().run()
