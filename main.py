from functions import Functions

if __name__ == '__main__':
    func = Functions()
    while True:
        func.show()
        option = input()
        if option == "1":
            func.showTasks(False)
        elif option == "2":
            func.addTask()
        elif option == "3":
            func.delTask(func.showTasks(True))
        elif option == "4":
            while True:
                func.showOther()
                try:
                    option = int(input("Wybierz opceję(1-8):"))
                    if option>0 and option<8:
                        func.other(option)
                    else:
                        break
                except ValueError:
                    print("Wybierz prawidłową opcję")
        elif option == "5":
            print("Program został zakończony")
            break
        else:
            print("Podaj właściwą opcję \n")


