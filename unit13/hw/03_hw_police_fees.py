"""
Вы работаете программистом в IT отделе ГИБДД.
    Ваш отдел отвечает за обслуживание камер,
    которые фиксируют превышения скорости и выписывают автоматические штрафы.
За последний месяц к вам пришло больше тысячи жалоб на ошибочно назначенные штрафы,
    из которых около 100 были признаны и правда ошибочными.

Список из дат и номеров автомобилей ошибочных штрафов прилагается к заданию,
    пожалуйста удалите записи об этих штрафах из таблицы `table_fees`
"""

import sqlite3
import csv

def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file) as f:
        wrong_fees = list(csv.reader(f))[1:]

    for wrong_fee in wrong_fees:
        truck_number = wrong_fee[0]
        timestamp = wrong_fee[1]
        c.execute(f"DELETE FROM table_fees "
                  f"WHERE truck_number = '{truck_number}' "
                  f"AND timestamp = '{timestamp}'")

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
