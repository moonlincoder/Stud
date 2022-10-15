from modules.module import Module


class Child(Module):
    info = "Напишите программу, которая принимает четыре целых числа от пользователя и выводит надпись равно, если все четыре равны, и не равно в противном случае."
    def run(self, **kwargs):
        a = []
        for i in range(4):
            a.append(int(input()))
        print(a[0] == a[1] & a[1] == a[2] & a[2] == a[3])


if __name__ == '__main__':
    Child().run()
