from modules.module import Module


class Child(Module):
    info = "Напишите программу, чтобы найти значение указанного выражения."
    def run(self, **kwargs):
        print("(101+0)/3 = ", ((101+0)/3))
        print("3.0e-6 * 10000000.1 = ", (3.0e-6 * 10000000.1))
        print("true && true = ", (True & True))
        print("false && true = ", (False & True))
        print("(false && false) || (true && true) = ", ((False & False) | (True & True)))
        print("(false || false) && (true && true) = ", ((False | False) & (True & True)))


if __name__ == '__main__':
    Child().run()
