from modules.module import Module


class Child(Module):
    info = "Напишите программу для умножения двух заданных целых чисел без использования оператора умножения(*)."

    def run(self, **kwargs):
        a = int(input("a > "))
        b = int(input("b > "))

        x = 0
        for i in range(b):
            x += a
        print(f"sum: {a}*{b} = {x}")

        x = a / (1/b)
        print(f"div: {a}*{b} = {x}")




if __name__ == '__main__':
    Child().run()
