from modules import bases

def safe_input(text, min, max):
    while True:
        num = int(input(text))
        if (min <= num) and (num <= max):
            return num

if __name__ == '__main__':
    print("Выберите базу: ")
    for i, base in enumerate(bases):
        print(f"{i}: {base[0]}")

    base = bases[safe_input(" база > ", 0, len(bases) - 1)][1]

    while True:
        a = input(" номер задания >> ")
        print()
        if a == 'h':
            a
        elif a.isdecimal():
            a = int(a)
            if (0 <= a) and (a <= len(base)):
                base[a]().run()
