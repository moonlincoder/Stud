from modules.module import Module


class Child(Module):
    info = "Напишите програмиу для преобразования температуры из градуса Фаренгейта в градус Цельсия."
    def run(self, **kwargs):
        cels = float(input("celsius > "))
        print(f"fahrenheit: {cels * (9/5) + 32}")


if __name__ == '__main__':
    Child().run()
