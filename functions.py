import csv
import re
from datetime import datetime
import os


class Functions:
    keys = ["name", "date", "time", "priority", "progress", "category", "description", "createTime", "updateTime"]
    def show(self):

        options = ["Wyświetl zadanie(a)", "Dodaj zadanie", "Usuń zadanie", "Inne operacje", "Wyjśće z programu"]
        print("Wybierz opcję:")
        for idx, x in enumerate(options):
            print(f"\t{idx + 1}. {x}")

    def showTasks(self, append):
        tasks = []
        with open("LZdZ/zadania.csv", "r") as f:
            r = csv.DictReader(f)
            for idx, x in enumerate(r):
                print(
                    f"\t{idx + 1}. {x['name']}; {x['date']}; {x['time']}; {x['priority']}; {x['progress']}; "
                    f"{x['category']}; {x['description']}"
                )
                if append:
                    tasks.append(x)
        f.close()
        return tasks
    def addTask(self):

        task = {}
        print("Podaj informacje o nowym zadaniu (* - dane obowiązkowe):")

        while True:
            name = input("Podaj nazwę zadania*:")
            if name != "":
                task["name"] = name
                break
            else:
                print("Wartość wymagana!")

        while True: # todo sprawdznie czy data nie jest przeszla
            date = input(
                "Podaj datę realizacji zadania w formacie rrrr-mm-dd lub wpisz brak*:")
            if re.match("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", date):

                task["date"] = date
                break
            elif date.casefold() == "brak":
                task["time"] = date
                break
            else:
                print("Wartość pusta lub błędny format!")

        while True: # todo sprawdznie czy data nie jest przeszla
            time = input(
                "Podaj czas realizacji zadania w formacie hh:mm lub wpisz brak*:")
            if re.match("([01]?[0-9]|2[0-3]):[0-5][0-9]", time):
                task["time"] = time
                break
            elif time.casefold() == "brak":
                task["time"] = time
                break
            else:
                print("Wartość pusta lub błędny format!")

        while True:
            priority = input("Podaj priorytet (no - normalny, ni - niski, wy - wysoki)*:")
            if priority.casefold() == "no" or priority.casefold() == "ni" or priority.casefold() == "wy":
                task["priority"] = priority
                break
            else:
                print("Wartość pusta bądź w złym formacie!")

        while True:
            try:
                progress = int(input("Podaj stopień realizacji (zakres 0-100)*:"))
                if int(progress) < 0 or int(progress) > 100:
                    print("Podaj wartość z właściwego zakresu!")
                else:
                    task["progress"] = progress
                    break
            except ValueError:
                print("Wartość musi być liczbą!")

        category = input("Podaj kategorię (np. \"praca\", \"hobby\"):")
        task["category"] = category

        description = input("Podaj opis zadania:")
        task["description"] = description

        task["createTime"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        task["updateTime"] = ""

        if os.stat("LZdZ/zadania.csv").st_size == 0:

            with open('LZdZ/zadania.csv', 'w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=Functions.keys)
                w.writeheader()
                w.writerow(task)
            f.close()
        else:
            with open('LZdZ/zadania.csv', 'a', newline='') as f:
                w = csv.DictWriter(f, task.keys())
                w.writerow(task)
            f.close()

        print("Pomyślnie dodano nowe zadanie")

    def delTask(self,tasks):
        if len(tasks) > 0:
            while True:
                i = 0
                try:
                    delete = int(input(f"Które zadanie chcesz usunąć (1-{len(tasks)}):"))
                    if delete > 0 and delete <= len(tasks):
                        with open('LZdZ/zadania.csv', 'w', newline='') as f:
                            w = csv.DictWriter(f, fieldnames=Functions.keys, )
                            w.writeheader()
                            for x in tasks:
                                if i + 1 != delete:
                                    w.writerow(tasks[i])
                                i += 1
                        f.close()
                        break
                    else:
                        print("Podaj liczbe z odpowiedniego zakresu!")
                except ValueError:
                    print("Wartość musi być liczbą!")

        else:
            print("Brak zadań do usunięcia")

    def other(self):
        options = [
            "Zmiana priorytetu", "Zmiana daty i czasu realizacji",
            "Zmiana stopnia realizacji", "Wyświetlanie zadań posortowanych wg daty i czasu utworzenia rosnąco",
            "Wyświetlanie zadań posortowanych wg daty i czasu utworzenia malejąco",
            "Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji rosnąco",
            "Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji malejąco", "Powrót do głównego menu."
        ]
        while True:
            print("Wybierz opcję:")
            for idx, x in enumerate(options):
                print(f"\t{idx + 1}. {x}")
            try:
                option = int(input("Wybierz opceję(1-8):"))
                if option == 1:
                    Functions().other1(Functions().showTasks(True))
                elif option == 2:
                    Functions().other2(Functions().showTasks(True))
                elif option == 3:
                    Functions().other3(Functions().showTasks(True))
                elif option == 4:
                    Functions().other4()
                elif option == 5:
                    Functions().other5()
                elif option == 6:
                    Functions().other6()
                elif option == 7:
                    Functions().other7()
                else:
                    break
            except ValueError:
                print("Wybierz prawidłową opcję")
    def other1(self,tasks):
        if len(tasks) > 0:
            while True:
                i = 0
                try:
                    edit = int(input(f"Wybierz zadanie które chcesz edytować (1-{len(tasks)}):"))
                    if edit > 0 and edit <= len(tasks):
                        with open('LZdZ/zadania.csv', 'w', newline='') as f:
                            w = csv.DictWriter(f, fieldnames=Functions.keys, )
                            w.writeheader()
                            for x in tasks:
                                if i + 1 == edit:
                                    while True:
                                        priority = input("Podaj priorytet (no - normalny, ni - niski, wy - wysoki)*:")
                                        if priority.casefold() != "no" and priority.casefold() != "ni" \
                                                and priority.casefold() != "wy":
                                            print("Wartość pusta bądź w złym formacie!")
                                        else:
                                            tasks[i]["priority"] = priority
                                            tasks[i]["updateTime"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                                            break
                                    w.writerow(tasks[i])
                                else:
                                    w.writerow(tasks[i])
                                i += 1

                        f.close()
                        break
                    else:
                        print("Podaj liczbe z odpowiedniego zakresu!")
                except ValueError:
                    print("Wartość musi być liczbą!")

        else:
            print("Brak zadań do edytacji")
    def other2(self,tasks):
        if len(tasks) > 0:
            while True:
                i = 0
                try:
                    edit = int(input(f"Wybierz zadanie które chcesz edytować (1-{len(tasks)}):"))
                    if edit > 0 and edit <= len(tasks):
                        with open('LZdZ/zadania.csv', 'w', newline='') as f:
                            w = csv.DictWriter(f, fieldnames=Functions.keys, )
                            w.writeheader()
                            for x in tasks:
                                if i + 1 == edit:
                                    while True: # todo sprawdznie czy data nie jest przeszla
                                        date = input(
                                            "Podaj datę realizacji zadania w formacie rrrr-mm-dd lub wpisz brak*:")
                                        if re.match("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", date):

                                            tasks[i]["date"] = date
                                            break
                                        elif date.casefold() == "brak":
                                            tasks[i]["time"] = date
                                            break
                                        else:
                                            print("Wartość pusta lub błędny format!")

                                    while True: # todo sprawdznie czy data nie jest przeszla
                                        time = input(
                                            "Podaj czas realizacji zadania w formacie hh:mm lub wpisz brak*:")
                                        if re.match("([01]?[0-9]|2[0-3]):[0-5][0-9]", time):
                                            tasks[i]["time"] = time
                                            tasks[i]["updateTime"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                                            break
                                        elif time.casefold() == "brak":
                                            tasks[i]["time"] = time
                                            tasks[i]["updateTime"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                                            break
                                        else:
                                            print("Wartość pusta lub błędny format!")
                                    w.writerow(tasks[i])
                                else:
                                    w.writerow(tasks[i])
                                i += 1

                        f.close()
                        break
                    else:
                        print("Podaj liczbe z odpowiedniego zakresu!")
                except ValueError:
                    print("Wartość musi być liczbą!")

        else:
            print("Brak zadań do edytacji")
    def other3(self,tasks):
        if len(tasks) > 0:
            while True:
                i = 0
                try:
                    edit = int(input(f"Wybierz zadanie które chcesz edytować (1-{len(tasks)}):"))
                    if edit > 0 and edit <= len(tasks):
                        with open('LZdZ/zadania.csv', 'w', newline='') as f:
                            w = csv.DictWriter(f, fieldnames=Functions.keys, )
                            w.writeheader()
                            for x in tasks:
                                if i + 1 == edit:
                                    while True:
                                        priority = input("Podaj priorytet (no - normalny, ni - niski, wy - wysoki)*:")
                                        if priority.casefold() == "no" or priority.casefold() == "ni" \
                                                or priority.casefold() == "wy":
                                            tasks[i]["priority"] = priority
                                            tasks[i]["updateTime"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                                            break
                                        else:
                                            print("Wartość pusta bądź w złym formacie!")
                                    w.writerow(tasks[i])
                                else:
                                    w.writerow(tasks[i])
                                i += 1

                        f.close()
                        break
                    else:
                        print("Podaj liczbe z odpowiedniego zakresu!")
                except ValueError:
                    print("Wartość musi być liczbą!")

        else:
            print("Brak zadań do edytacji")
    def other4(self): #todo Wyświetlanie zadań posortowanych wg daty i czasu utworzenia rosnąco
        pass
    def other5(self): #todo Wyświetlanie zadań posortowanych wg daty i czasu utworzenia malejąco
        pass
    def other6(self): #todo Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji rosnąco
        pass
    def other7(self): #todo Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji malejąco
        pass