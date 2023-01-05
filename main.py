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
            func.other()
        elif option == "5":
            print("Program został zakończony")
            break
        else:
            print("Podaj właściwą opcję \n")


