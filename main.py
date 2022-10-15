from modules import module_list

if __name__ == '__main__':
    print("Выберите задание")
    for i, module in enumerate(module_list):
        print(f"{i+1}: {module.info}")
    print("\n-1: exit")
    while True:
        a = int(input(" номер задания >> "))
        print()
        if (a >= 0) and (a <= len(module_list)):
            module_list[a-1]().run()
        else:
            print("exiting")
