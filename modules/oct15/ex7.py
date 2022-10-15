import random

from modules.module import Module


class Child(Module):
    name = "Четные и нечетные в массиве"
    info = "Напишите для разбиения заданного " \
           "массива целых чисел на четное число " \
           "первым и нечетное число вторым."

    def run(self, **kwargs):
        mas = input("mas > ")
        if mas == 'r':
            even = []
            for a in range(100):
                even.append(random.randint(-1000, 1000))
        else:
            even = list(map(lambda x: int(x), mas.split(" ")))

        odd = []
        for a in even:
            if a % 2 == 0:
                odd.append(a)
                even.remove(a)

        print(f"odd: {odd} \n even: {even}")


if __name__ == '__main__':
    Child().run()
