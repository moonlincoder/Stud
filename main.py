from modules import bases


def safe_input(text, min, max):
    while True:
        num = int(input(text))
        if (min <= num) and (num <= max):
            return num


if __name__ == '__main__':
    base = bases[-1][1]
    print(f"Выбрана последняя база: \"{bases[-1][0]}\", для смены наберите cd ")
    while True:
        a = input(" >_  ")
        print()

        if a.isdecimal():
            a = int(a)
            if (0 <= a) and (a <= len(base)):
                base[a]().run()
        else:
            a = a.split()
            if a[0] == 'h':
                if len(a) == 1:
                    print('Доступные команды: \n'
                          ' h <n> - подробное описание модуля или эта подсказка \n'
                          ' ls - вывести список модулей текущей базы \n'
                          ' ld - вывести список баз \n'
                          ' cd - сменить базу \n'
                          '')
                else:
                    for module in a[1:]:
                        print(base[int(module)].info)
            elif a[0] == 'ls':
                for i, module in enumerate(base):
                    print(f"{i}: {module.name}")
            elif a[0] == 'ld':
                for i, base in enumerate(bases):
                    print(f"{i}: {base[0]}")
            elif a[0] == 'cd':
                if len(a) == 2:
                    index = int(a[1])
                    if 0 <= index <= (len(bases) - 1):
                        base = bases[index]
                else:
                    base = bases[safe_input(" база > ", 0, len(bases) - 1)]
                print(f"Текущая база: {base[0]}")
                base = base[1]
            else:
                print("Неизвестная команда, напишите h")
