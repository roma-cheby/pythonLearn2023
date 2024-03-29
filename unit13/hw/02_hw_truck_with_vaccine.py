"""
Пожалуйста, запустите скрипт generate_hw_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы hw.db и в нем таблица table_truck_with_vaccine
Грузовик перевозит очень важную вакцину.

Условия хранения этой вакцины весьма необычные -- в отсеке должна быть температура  -18±2 градуса.
    Если температурный режим был нарушен - вакцина считается испорченной.

Для проверки состояния вакцины применяется датчик, который раз в час измеряет температуру внутри контейнера.
    Если в контейнере было хотя бы 3 часа с температурой, которая находится вне указанного выше диапазона -
    температурный режим считается нарушенным.

Пожалуйста, реализуйте функцию `check_if_vaccine_has_spoiled`,
    которая по номеру грузовика определяет, не испортилась ли вакцина.
"""
import sqlite3


def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    c.execute(f"SELECT COUNT(*) FROM table_truck_with_vaccine "
              f"WHERE truck_number = '{truck_number}' "
              f"AND (temperature_in_celsius > 20 OR temperature_in_celsius < 16)")

    counts_spoiled_times = c.fetchall()[0][0]
    return counts_spoiled_times >= 3

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        truck_number = input("Введите государственный регистрационный номер фургона: ")
        print("Вакцина испорчена!" if check_if_vaccine_has_spoiled(cursor, truck_number) else "Вакцина пригодна к использованию.")