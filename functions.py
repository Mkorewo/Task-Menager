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
            name = input("Podaj nazwę zadania*:")  # dodanie nazwy zadania
            if name != "":
                task["name"] = name
                break
            else:
                print("Wartość wymagana!")

        while True:
            date = input(
                "Podaj datę realizacji zadania w formacie rrrr-mm-dd lub wpisz brak*:")  # TODO dodac walidacje na "brak"
            if re.match("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", date):
                task["date"] = date  # todo data nie moze byc dzisiejsza
                break
            else:
                print("Wartość pusta lub błędny format!")

        while True:
            time = input(
                "Podaj czas realizacji zadania w formacie hh:mm lub wpisz brak*:")  # TODO dodac walidacje na "brak"
            if re.match("([01]?[0-9]|2[0-3]):[0-5][0-9]", time):
                task["time"] = time
                break
            else:
                print("Wartość pusta lub błędny format!")

        words = ["NO", "WY", "NI"]
        while True:
            priority = input("Podaj priorytet (NO - normalny, NI - niski, WY - wysoki)*:")
            if priority == "NO" in words:
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

    def other(self, option):
        print(f"Wybrano opcę{option}")
        # inne opcje

    def showOther(self):
        print("lista opcji...")  # todo
