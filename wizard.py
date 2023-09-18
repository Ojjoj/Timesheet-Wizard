import os
import csv
from prettytable import from_csv, PrettyTable
import time

file_name = "classes.csv"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def prompt(title, options):
    clear_screen()
    print("{:-^50}".format(title))
    for i, option in enumerate(options):
        print("{} - {}".format(i + 1, option))
    print("- " * 25)
    print("{} - {}".format(0, "Exit"))
    print("-" * 50)
    while True:
        try:
            user = int(input("Choose your option number : "))
            if 0 <= user <= len(options):
                break
        except ValueError:
            pass
    return user


def show_all():
    options = ("All", "Classes", "Dates")
    while True:
        user = prompt("Wizard->Show all", options)
        if user == 0:
            break
        if user == 1:
            show_all_all()
        elif user == 2:
            show_all_classes()
        elif user == 3:
            show_all_dates()


def show_all_all():
    try:
        with open(file_name, "r") as fp:
            file = open(file_name, "r")
            x = from_csv(file)
        print(x)
        input()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


def show_all_classes():
    try:
        with open(file_name, "r") as fp:
            file = from_csv(fp)
            header = file.field_names
            class_names = header[1:]
            x = PrettyTable()
            x.field_names = ["Classes"]
            for row in class_names:
                x.add_row([row])
            print(x)
        input()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


def search():
    options = ("Class", "All hours", "All balance")
    while True:
        user = prompt("Wizard->Search", options)
        if user == 0:
            break
        elif user == 1:
            ...
            # search_class()
        elif user == 2:
            search_hours()
        elif user == 3:
            ...
            # search_balance()


def search_hours():
    total_hours = 0

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                for cell in row[1:]:
                    try:
                        total_hours += float(cell)
                    except ValueError:
                        pass
        print("Total hours : {:>36}".format(total_hours))
        input()

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


def show_all_dates():
    try:
        with open(file_name, "r") as fp:
            file = from_csv(fp)
        print(file.get_string(fields=["Dates"]))
        input()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


def main():
    options = ("Show all", "Search", "Update", "Timesheet")
    while True:
        user = prompt("Wizard", options)
        if user == 0:
            break
        elif user == 1:
            show_all()
        elif user == 2:
            search()
        elif user == 3:
            ...
            # update()
        elif user == 4:
            ...
            # timesheet()


if __name__ == "__main__":
    main()
